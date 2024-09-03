import pandas as pd
from abc import ABC


class DataCleaner(ABC):
    def apply_cleaning(self, data: pd.Series) -> pd.Series:
        """
        We take the input series data and output it in the series format

        Parameters:
        data pandas.Series: the data to be cleaned

        Returns:
        pandas.Series: The cleaned data. The type is forced to be Series.
        """
        pass
