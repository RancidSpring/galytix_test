from data_cleaners.base_class.data_cleaner import DataCleaner
from similarity_matchers.embedding_generator import EmbeddingGenerator
from similarity_matchers.base_class.metrcis_calculator import MetricsCalculator
import pandas as pd


class SimilarityMatcher():
    def __init__(self, data: pd.Series, cleaner: DataCleaner, embedder: EmbeddingGenerator, metrics_calculator: MetricsCalculator):
        self.data = data
        self.cleaner = cleaner
        self.embedder = embedder
        self.metrics_calculator = metrics_calculator

    def find_closest_match(self):
        pass

