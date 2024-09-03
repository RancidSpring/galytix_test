import pandas as pd
from abc import ABC, abstractmethod


class MetricsCalculator(ABC):
    @abstractmethod
    def compute_pairwise_distances(self, embeddings) -> pd.DataFrame:
        """
        Abstract method to compute pairwise distances.
        This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def compute_distances_from(self, target_embeddings, baseline_embeddings):
        """
        Abstract method to compute distances of the target phrases from the baseline phrases.
        This method must be implemented by subclasses.
        """
        pass
