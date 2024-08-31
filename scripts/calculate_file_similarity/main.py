from data_loaders.csv_loader import CSVLoader
from data_loaders.parquet_loader import ParquetLoader
from scripts.calculate_file_similarity.constants import PHRASES_PATH, MODEL_DATA
from similarity_matchers.embedding_generator import EmbeddingGenerator
from data_cleaners.phrases_cleaner import PhrasesCleaner
# from similarity_matchers.similarity_matcher import


def main():
    # ---------------------------- Read the input data ------------------------------------
    phrases = CSVLoader(PHRASES_PATH).load_data(encoding='unicode_escape', index_col=None)
    model_embeddings = ParquetLoader(MODEL_DATA).load_data()

    # ---------------------------- Create embeddings ---------------------------------------
    cleaner = PhrasesCleaner()
    embedding_gen = EmbeddingGenerator(model_embeddings, data_cleaner=cleaner)
    embedded_phrases = embedding_gen.embed_phrases(phrases=phrases['Phrases'], apply_cleaning=True)

    # ---------------------------- Find similarities ---------------------------------------
    # We have found embeddings for every phrase, now move on to calculate the differences.
    print()
