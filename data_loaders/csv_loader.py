import pandas as pd
from data_loaders.base_class.data_loader import DataLoader


class CSVLoader(DataLoader):
    def __init__(self, file_path: str):
        """
        Initialize the CSVLoader with a file path.

        :param file_path: Path to the CSV file to be loaded.
        """
        super().__init__(file_path)

    def load_data(self) -> pd.DataFrame:
        """
        Load data from a CSV file.

        :return: DataFrame containing the CSV data.
        """
        try:
            df = pd.read_csv(self.file_path)
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f'Failed to find the following path {self.file_path}')
        except Exception as e:
            raise RuntimeError(f"Failed to load CSV file with error: {e}")
