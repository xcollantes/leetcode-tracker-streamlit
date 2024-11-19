"""Google sheets data source."""

import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection


@st.cache_data(show_spinner="Getting Google Sheets data...")
def get_sheet_data() -> pd.DataFrame:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
    return df
