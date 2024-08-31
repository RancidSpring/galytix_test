from utils import initialize_logger


PATH_TO_BINARY = 'data/GoogleNews-vectors-negative300.bin'
PATH_TO_RAW_CSV = 'data/vectors.csv'
PATH_TO_CLEAN_PARQUET = 'data/vectors_cleaned.parquet'

logger = initialize_logger('EMBEDDINGS_LOADER')
