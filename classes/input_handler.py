import pandas as pd
import os
from classes.data_loaders.csv_loader import CSVLoader
from classes.data_loaders.parquet_loader import ParquetLoader


class InputHandler:
    SUPPORTED_EXTENSIONS = {'.csv', '.parquet'}

    def __init__(self):
        self.input_string = None

    def parse_input(self, input_string):
        self.input_string = input_string
        if self.input_string.startswith("manual:"):
            return self._handle_manual_input()
        elif self.input_string.startswith("file:"):
            return self._handle_file_input()
        else:
            raise ValueError("Invalid input string format. Must start with 'manual:' or 'file:'. "
                             "Put your desired string or path to file after the prefix.")

    def _handle_manual_input(self):
        """
        Removes the auxiliary string from the input and splits the rest by the delimiter
        :return:
        """
        return pd.Series(self.input_string[len("manual:"):].strip().split('|'))

    def _handle_file_input(self):
        """
        Removes the auxiliary string from the input and checks the provided path
        :return:
        """
        file_path = self.input_string[len("file:"):].strip()

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file at path {file_path} does not exist.")

        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == '.csv':
            df = CSVLoader(file_path).load_data(index_col=None)
        elif file_extension == '.parquet':
            df = ParquetLoader(file_path).load_data()
        else:
            raise ValueError(
                f"Unsupported file format '{file_extension}'. "
                f"Supported formats are: {', '.join(self.SUPPORTED_EXTENSIONS)}")

        if df.shape[1] != 1:
            raise ValueError('The dataframe passed from file has a wrong format. It should only have one column.')
        return df.iloc[:, 0]
