from classes.similarity_matcher import SimilarityMatcher
from classes.embedding_generators.embedding_generator import EmbeddingGenerator
from classes.data_cleaners.phrases_cleaner import PhrasesCleaner
from classes.data_loaders.csv_loader import CSVLoader
from classes.data_loaders.parquet_loader import ParquetLoader
from classes.metrics_calculators.cosine_metrics_calculator import CosineDistanceCalculator
from classes.metrics_calculators.euclidian_metrics_calculator import L2DistanceCalculator
from utils import initialize_logger
from classes.input_handler import InputHandler
from tabulate import tabulate


def main(path_to_model: str, path_to_baseline_phrases: str, metrics: str):
    # Initialize the application
    logger = initialize_logger("Matching Application")

    input_handler = InputHandler()
    logger.info('InputHandler is initialized.')

    data_cleaner = PhrasesCleaner()
    logger.info('Data Cleaner is initialized.')

    model_embeddings = ParquetLoader(path_to_model).load_data()
    embedder = EmbeddingGenerator(model_embeddings)
    logger.info('EmbeddingGenerator is initialized.')

    baseline_phrases = CSVLoader(path_to_baseline_phrases).load_data(
        encoding='unicode_escape', index_col=None
    )['Phrases']

    logger.info('Baseline phrases are loaded.')

    if metrics == 'euclidian':
        metrics_calculator = L2DistanceCalculator()
    elif metrics == 'cosine':
        metrics_calculator = CosineDistanceCalculator()
    logger.info('Metrics calculator is initialized.')

    similarity_matcher = SimilarityMatcher(
        cleaner=data_cleaner, embedder=embedder, metrics_calculator=metrics_calculator,
        baseline_phrases=baseline_phrases
    )

    logger.info('The application initialization is finished.')

    while True:
        user_input = input("Enter input string (type 'exit' to quit): ")

        if user_input.lower() == "exit":
            logger.info("Exiting...")
            break

        try:
            result = input_handler.parse_input(user_input)
            matching_result = similarity_matcher.find_closest_matches(result)

            logger.info(f"Mathing result:\n {tabulate(matching_result, headers='keys', tablefmt='psql')}")
        except Exception as e:
            logger.info(f"Error: {e}")

