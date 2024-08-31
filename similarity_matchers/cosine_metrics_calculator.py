import pandas as pd
from similarity_matchers.base_class.metrcis_calculator import MetricsCalculator
from sklearn.metrics.pairwise import cosine_distances


class CosineDistanceCalculator(MetricsCalculator):
    def compute_pairwise_distances(self) -> pd.DataFrame:
        """
        Compute pairwise cosine distances between all phrases in the embedding DataFrame.

        Returns:
        pd.DataFrame: A DataFrame where the indices and columns are phrases, and each cell
                      contains the cosine distance between the corresponding pair of phrases.
        """
        distance_matrix = cosine_distances(self.embeddings)
        distance_df = pd.DataFrame(distance_matrix, index=self.phrases, columns=self.phrases)
        return distance_df
