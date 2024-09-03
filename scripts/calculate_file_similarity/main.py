from data_loaders.csv_loader import CSVLoader
from data_loaders.parquet_loader import ParquetLoader
from scripts.calculate_file_similarity.constants import PHRASES_PATH, MODEL_DATA, OUTPUT_PATH
from similarity_matchers.embedding_generator import EmbeddingGenerator
from data_cleaners.phrases_cleaner import PhrasesCleaner
from similarity_matchers.cosine_metrics_calculator import CosineDistanceCalculator
# from similarity_matchers.similarity_matcher import


def main():
    # ---------------------------- Read the input data ------------------------------------
    phrases = CSVLoader(PHRASES_PATH).load_data(encoding='unicode_escape', index_col=None)
    model_embeddings = ParquetLoader(MODEL_DATA).load_data()

    # ---------------------------- Create embeddings ---------------------------------------
    cleaned_data = PhrasesCleaner().apply_cleaning(phrases['Phrases'])
    embedding_gen = EmbeddingGenerator(model_embeddings)
    embedded_phrases = embedding_gen.embed_phrases(phrases=cleaned_data)

    # ---------------------------- Find similarities ---------------------------------------
    # We have found embeddings for every phrase, now move on to calculate the differences.
    metrics_calculator = CosineDistanceCalculator()
    distances = metrics_calculator.compute_pairwise_distances(embedded_phrases)

    # ---------------------------- Save to the output --------------------------------------
    distances.to_parquet(OUTPUT_PATH)
    print()
