import pandas as pd
from data_loaders.base_class.data_loader import DataLoader


class ParquetLoader(DataLoader):
    def __init__(self, file_path: str):
        """
        Initialize the ParquetLoader with a file path.

        :param file_path: Path to the Parquet file to be loaded.
        """
        super().__init__(file_path)

    def load_data(self) -> pd.DataFrame:
        """
        Loads a parquet file

        :return: DataFrame containing the Parquet data.
        """
        try:
            df = pd.read_parquet(self.file_path)
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f'Failed to find the following path {self.file_path}')
        except Exception as e:
            raise RuntimeError(f"Failed to load CSV file with error: {e}")