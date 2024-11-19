"""Default template for user."""

import streamlit as st

from components import calendar
from components.breakdown_diff import breakdown_bar
from components.diff_donut import diff
from components.topic_donut import topic
from data_sources.sheets import get_sheet_data
from modules.page_config import PageConfig


def user_template(tab_name: str) -> None:
    """Default template for user.

    Args:
        tab_name (str): Name of tab.

    Returns:
        Streamlit object.
    """
    PageConfig(page_title=tab_name).get_config()

    st.header(tab_name)

    df = get_sheet_data()
    tab_df = df[df["Tab"] == tab_name]

    calendar.calendar(tab_df)

    col1, col2 = st.columns(2)
    with col1:
        topic(tab_df)

    with col2:
        diff(tab_df)

    breakdown_bar(tab_df)

    st.dataframe(tab_df, use_container_width=True, hide_index=True)
