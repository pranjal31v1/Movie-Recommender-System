# -*- coding: utf-8 -*-
"""Utility functions for the movie recommender project."""

from __future__ import annotations

import pandas as pd

# List of genres used in the original notebook
GENRES = [
    "Action",
    "Comedy",
    "Sci-Fi",
    "Adventure",
    "Drama",
    "Horror",
    "Thriller",
    "Animation",
    "Romance",
    "Fantasy",
    "Family",
    "History",
    "Biography",
    "Music",
    "Mystery",
    "Crime",
]

def encode_genres(df: pd.DataFrame, column: str = "Genre") -> pd.DataFrame:
    """Return a copy of ``df`` with binary columns for each genre.

    Parameters
    ----------
    df:
        DataFrame containing a column with genre strings.
    column:
        Name of the column in ``df`` containing the genre information.

    Returns
    -------
    DataFrame
        Copy of ``df`` with additional columns for each genre listed in
        :data:`GENRES`. Each new column contains ``1`` if the genre is present
        in ``column`` and ``0`` otherwise.
    """
    df = df.copy()
    for genre in GENRES:
        df[genre] = df[column].str.contains(genre).astype(int)
    return df

if __name__ == "__main__":
    # Example usage on the provided dataset. This block mirrors the behaviour of
    # the original script while being safe to import in tests.
    dataset = pd.read_csv("IMDB-Movie-Data.csv")
    encoded = encode_genres(dataset)
    print(encoded.head())
