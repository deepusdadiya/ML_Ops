import re

import numpy as np
import pandas as pd


def _get_first_cabin(row):
    try:
        return row.split()[0]
    except Exception:
        return np.nan


def _get_title(passenger) -> str:
    line = passenger
    if re.search("Mrs", line):
        return "Mrs"
    elif re.search("Mr", line):
        return "Mr"
    elif re.search("Miss", line):
        return "Miss"
    elif re.search("Master", line):
        return "Master"
    else:
        return "Other"


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = df.copy()

    df_copy = df_copy.replace("?", np.nan)
    df_copy["cabin"] = df_copy["cabin"].apply(_get_first_cabin)
    df_copy["title"] = df_copy["name"].apply(_get_title)
    df_copy["fare"] = df_copy["fare"].astype("float")
    df_copy["age"] = df_copy["age"].astype("float")
    df_copy.drop(
        labels=["name", "ticket", "boat", "body", "home.dest"], axis=1, inplace=True
    )

    return df_copy