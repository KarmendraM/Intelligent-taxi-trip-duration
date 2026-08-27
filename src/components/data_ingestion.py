import sys

import pandas as pd

from src.exception import CustomException
from src.logger import logging


def load_raw_data(path: str) -> pd.DataFrame:
    try:
        logging.info("Starting data ingestion for NYC Taxi Trip Duration dataset")

        df = pd.read_csv(path)

        logging.info(
            f"Loaded {df.shape[0]} rows and {df.shape[1]} columns"
        )

        return df

    except Exception as e:
        logging.error("Failed to load the taxi dataset")
        raise CustomException(e, sys)