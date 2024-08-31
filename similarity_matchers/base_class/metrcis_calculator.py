import pandas as pd
from abc import ABC, abstractmethod


class MetricsCalculator(ABC):
    def __init__(self, embedding_df: pd.DataFrame):
        self.embedding_df = embedding_df
        self.embeddings = embedding_df.values
        self.phrases = embedding_df.index

    @abstractmethod
    def compute_pairwise_distances(self) -> pd.DataFrame:
        """
        Abstract method to compute pairwise distances.
        This method must be implemented by subclasses.
        """
        pass