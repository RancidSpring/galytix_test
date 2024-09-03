from classes.data_cleaners.base_class.data_cleaner import DataCleaner
from classes.embedding_generators.embedding_generator import EmbeddingGenerator
from classes.metrics_calculators.base_class.metrcis_calculator import MetricsCalculator
import pandas as pd
import numpy as np


class SimilarityMatcher:
    def __init__(self, baseline_phrases: pd.Series, cleaner: DataCleaner,
                 embedder: EmbeddingGenerator, metrics_calculator: MetricsCalculator):
        self.cleaner = cleaner
        self.embedder = embedder
        self.metrics_calculator = metrics_calculator
        self.baseline_embeddings = self.embedder.embed_phrases(baseline_phrases)

    def find_closest_matches(self, phrases: pd.Series, mode: str = 'target') -> pd.DataFrame:
        cleaned_phrases = self.cleaner.apply_cleaning(phrases)
        embedded_target_phrases = self.embedder.embed_phrases(phrases=cleaned_phrases)
        distances_from_baseline = self.metrics_calculator.compute_distances_from(
            embedded_target_phrases, self.baseline_embeddings
        )
        best_matches = self.extract_lowest_distance(distances_from_baseline, how=mode)
        return best_matches

    @staticmethod
    def extract_lowest_distance(distance_df: pd.DataFrame, how='target') -> pd.DataFrame:
        """
        Findes the minimum distance for every index phrase according to the distance value in one of the columns.
        Supports pairwise and target modes. In target mode it assumes that we are finding the best matches for the
        passed input phrases, in pairwise mode we assume matching phrases with each other and finding the closest match.
        :param distance_df: dataframe, where index are phrases to be matched and columns are phrases to match with
        :param how: mode (see above)
        :return:
        """
        if how == 'pairwise':
            np.fill_diagonal(distance_df.values, np.inf)
            distance_df = distance_df.where(np.triu(np.ones(distance_df.shape), k=1).astype(bool), np.inf)
        elif how == 'target':
            pass
        else:
            raise ValueError('unsupported extract lowest distance mode. Supported: target and pairwise')
        best_matches = distance_df.idxmin(axis=1)
        best_match_df = pd.DataFrame(best_matches, index=distance_df.index, columns=["Best Match"])
        return best_match_df

