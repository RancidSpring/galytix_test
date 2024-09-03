import pandas as pd
from classes.metrics_calculators.base_class.metrcis_calculator import MetricsCalculator
from sklearn.metrics.pairwise import cosine_distances


class CosineDistanceCalculator(MetricsCalculator):
    def compute_pairwise_distances(self, embeddings: pd.DataFrame) -> pd.DataFrame:
        """
        Compute pairwise cosine distances between all phrases in the embedding DataFrame.

        Returns:
        pd.DataFrame: A DataFrame where the indices and columns are phrases, and each cell
                      contains the cosine distance between the corresponding pair of phrases.
        """
        distance_matrix = cosine_distances(embeddings)
        distance_df = pd.DataFrame(distance_matrix, index=embeddings.index, columns=embeddings.index)
        return distance_df

    def compute_distances_from(self, target_embeddings: pd.DataFrame, baseline_embeddings:  pd.DataFrame):
        """
        Compute cosine distances between all embeddins in target_embeddings from the baseline embeddings

        Returns:
        pd.DataFrame: A DataFrame where the indices and columns are phrases, and each cell
                      contains the cosine distance between the corresponding pair of phrases.
        """
        target_embedding_arr = target_embeddings.values.reshape(len(target_embeddings), -1)
        distances = cosine_distances(baseline_embeddings, target_embedding_arr).T
        distance_series = pd.DataFrame(data=distances, index=target_embeddings.index, columns=baseline_embeddings.index)
        return distance_series
