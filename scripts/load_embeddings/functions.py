import gensim
import pandas as pd
from gensim.models import KeyedVectors
from scripts.load_embeddings.constants import PATH_TO_BINARY, PATH_TO_RAW_CSV
import numpy as np
from nltk.corpus import stopwords
import nltk
import re


def load_embeddings_from_binary() -> None:
    wv = KeyedVectors.load_word2vec_format(PATH_TO_BINARY, binary=True, limit=1000000)
    wv.save_word2vec_format(PATH_TO_RAW_CSV)


def clean_index(index):
    return re.sub(r'[^a-zA-Z\s]', '', index)


def preprocess_embeddings(raw_embeddings: pd.DataFrame) -> pd.DataFrame:

    # --------------------------- Remove duplicates -------------------------------
    embeddings = raw_embeddings[~raw_embeddings.index.duplicated(keep='first')]

    # -------------------------- Remove weird characters ------------------------------
    embeddings = embeddings[~embeddings.index.isna()]
    embeddings.index = embeddings.index.map(clean_index)
    embeddings = embeddings[embeddings.index != ""]

    # --------------------------- Remove stopwords ---------------------------------
    # try:
    #     stop_words = set(stopwords.words('english'))
    # except LookupError:
    #     nltk.download('stopwords')
    #     stop_words = set(stopwords.words('english'))
    #
    # embeddings = embeddings[~embeddings.index.isin(stop_words)]

    # --------------------------- Remove outliers ----------------------------------
    # I chose to remove vectors with a high magnitude
    magnitude = np.linalg.norm(embeddings.values, axis=1)
    min_magnitude = np.percentile(magnitude, 1)  # Remove the bottom 1% as outliers
    max_magnitude = np.percentile(magnitude, 99)  # Remove the top 1% as outliers

    embeddings = embeddings[(magnitude >= min_magnitude) & (magnitude <= max_magnitude)]
    return embeddings


