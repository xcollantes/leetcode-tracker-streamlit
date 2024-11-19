"""Google sheets data source."""

import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection


@st.cache_data(show_spinner="Getting Google Sheets data...")
def get_sheet_data() -> pd.DataFrame:
    """Get data from Sheet by name of tab which is also name of user.

    Best to call the entire sheet at once since it is cached. Post filtering is
    done for each user.
    """

    conn = st.connection("gsheets", type=GSheetsConnection)

    df: pd.DataFrame = pd.concat(
        [
            conn.read(worksheet="Xavier"),
            conn.read(worksheet="Sam"),
        ],
        ignore_index=True,
    )

    df = df.dropna(subset=["Difficulty"])  # Effectively requires Difficulty column.

    df["Problem count"] = 1

    df["_difficulty_enum"] = df["Difficulty"].apply(lambda x: diff_enum(x))

    # Types.
    df["Date"] = pd.to_datetime(df["Date"])

    return df.reset_index(drop=True)


def diff_enum(value: str) -> int:
    """Assign ordinal values to difficulty."""

    value = value.lower()
    if value == "easy":
        return 1
    elif value.startswith("med"):
        return 2
    elif value == "hard":
        return 3
    else:
        return None
