import pandas as pd

from project import encode_genres, GENRES


def test_encode_genres_simple():
    df = pd.DataFrame({
        "Title": ["Test Movie"],
        "Genre": ["Action,Drama"],
    })
    result = encode_genres(df)

    for genre in GENRES:
        expected = 1 if genre in ["Action", "Drama"] else 0
        assert result.loc[0, genre] == expected
