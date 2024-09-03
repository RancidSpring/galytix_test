"""
This part I decided to make a script as it is used as a one time thing to load the dataset of embeddings
"""

from scripts.load_embeddings.functions import preprocess_embeddings
from scripts.load_embeddings.constants import PATH_TO_RAW_CSV, PATH_TO_CLEAN_PARQUET, logger
from classes.data_loaders.csv_loader import CSVLoader


def main():
    logger.info('Loading the raw embeddings')
    raw_embeddings = CSVLoader(PATH_TO_RAW_CSV).load_data(skip_rows=1, delimiter=' ', index_col=0)

    logger.info('Applying processing to embeddings')
    processed_embeddings = preprocess_embeddings(raw_embeddings)

    logger.info('Saving the processed dataset to parquet')
    processed_embeddings.to_parquet(PATH_TO_CLEAN_PARQUET)
