from data_cleaners.base_class.data_cleaner import DataCleaner
import pandas as pd
import re


class PhrasesCleaner(DataCleaner):
    def apply_cleaning(self, data) -> pd.Series:
        """
        Removes all nonalphabetical characters from the input pandas Series.

        Parameters:
        data (pd.Series): The pandas Series to be cleaned.

        Returns:
        pd.Series: A pandas series
        """
        return data.apply(lambda x: re.sub(r'[^a-zA-Z ]', '', x))
