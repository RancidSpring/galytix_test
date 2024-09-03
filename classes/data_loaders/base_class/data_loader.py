from abc import ABC


class DataLoader(ABC):
    def __init__(self, file_path: str):
        """
        Initializes an abstract loader

        :param file_path: Path to the file to be loaded.
        """
        self.file_path = file_path

    def load_data(self):
        """
        Method to load data from a file.
        This should be implemented by subclasses.
        """
        pass