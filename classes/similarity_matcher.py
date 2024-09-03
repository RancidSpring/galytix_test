from classes.data_cleaners.base_class.data_cleaner import DataCleaner
from classes.embedding_generators.embedding_generator import EmbeddingGenerator
from classes.metrics_calculators.base_class import MetricsCalculator
import pandas as pd
import numpy as np


class SimilarityMatcher:
    def __init__(self, cleaner: DataCleaner, embedder: EmbeddingGenerator, metrics_calculator: MetricsCalculator):
        self.cleaner = cleaner
        self.embedder = embedder
        self.metrics_calculator = metrics_calculator

    def find_closest_matches(self, data: pd.Series):
        pass

    @staticmethod
    def extract_lowest_distance(distance_df: pd.DataFrame) -> pd.DataFrame:
        np.fill_diagonal(distance_df.values, np.inf)
        distance_df = distance_df.where(np.triu(np.ones(distance_df.shape), k=1).astype(bool), np.inf)
        best_matches = distance_df.idxmin(axis=1)
        best_match_df = pd.DataFrame(best_matches, index=distance_df.index, columns=["Best Match"])
        return best_match_df

