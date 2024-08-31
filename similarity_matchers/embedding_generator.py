import numpy as np
import pandas as pd

from data_cleaners.base_class.data_cleaner import DataCleaner
from typing import Union
import fuzzymatcher


class EmbeddingGenerator:
    def __init__(self, embedding_model_data: pd.DataFrame, data_cleaner: DataCleaner):
        self.model = embedding_model_data
        self.cleaner = data_cleaner

    def get_normalized_phrase_embedding(self, phrase: str):
        words = phrase.split()
        word_vectors = self.model[self.model.index.isin(words)]

        if not word_vectors.empty:
            word_vectors = word_vectors.apply(lambda x: x / np.linalg.norm(x), axis=1)
            phrase_embedding = word_vectors.sum(axis=0)
            return phrase_embedding / np.linalg.norm(phrase_embedding)
        else:
            return np.zeros(self.model.shape[1])

    def get_normalized_phrase_embedding_lev(self, phrase: str):
        """
        Tried levenstein, it is too slow to make fuzzy match to the whole dataframe, should stick to word by word
        :param phrase:
        :return:
        """
        words = phrase.split()
        words_df = pd.DataFrame(words, columns=["word"])
        model_words_df = pd.DataFrame(self.model.index).rename(columns={'</s>': 'model_word'})
        matched_df = fuzzymatcher.fuzzy_left_join(words_df, model_words_df, left_on="word", right_on="model_word")
        matched_words = matched_df.loc[:, ['left_word', 'best_match_right_word']]
        matched_words = matched_words[matched_words['best_match_right_word'].notnull()]
        matched_vectors = self.model.loc[matched_words['best_match_right_word']]
        normalized_vectors = matched_vectors.apply(lambda x: x / np.linalg.norm(x), axis=1)
        if not normalized_vectors.empty:
            phrase_embedding = normalized_vectors.sum(axis=0)
            return phrase_embedding / np.linalg.norm(phrase_embedding)
        else:
            return np.zeros(self.model.shape[1])

    def embed_phrases(self, phrases: Union[pd.Series, str], apply_cleaning=False) -> pd.DataFrame:
        """
        Takes a pandas Series as an input and outputs the DataFrame with the DataFrame with phrases as an index
        and columns representing vectors of the embedded phrase
        :param phrases: series with the phrases for every row
        :param apply_cleaning: flag whether we want to apply cleaning
        :return:
        """
        if isinstance(phrases, str):
            phrases = pd.Series([phrases])

        if apply_cleaning:
            phrases = self.cleaner.apply_cleaning(phrases)

        phrases_tokens = phrases.apply(self.get_normalized_phrase_embedding)
        phrases_embedded_df = pd.DataFrame(phrases_tokens)
        phrases_embedded_df['Phrases'] = phrases
        phrases_embedded_df = phrases_embedded_df.set_index('Phrases')
        return phrases_embedded_df
