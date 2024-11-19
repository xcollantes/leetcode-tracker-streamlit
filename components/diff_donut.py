"""Donut chart."""

import altair as alt
import pandas as pd
import streamlit as st

from constants.colors import EASY_DIFFICULTY, HARD_DIFFICULTY, MED_DIFFICULTY


def diff(df: pd.DataFrame):
    """Render a donut chart visualizing problems by difficulty.

    Args:
        df (pd.DataFrame): DataFrame containing at least 'Problem count' and
        'Difficulty' columns.

    Displays:
        An Altair donut chart using streamlit, illustrating the distribution of
        problem counts across different difficulties.
    """
    chart = (
        (
            alt.Chart(df)
            .mark_arc(innerRadius=95)
            .encode(
                theta=alt.Theta("Problem count:Q"),
                color=alt.Color(
                    "Difficulty:N",
                    scale=alt.Scale(
                        domain=["Easy", "Med", "Hard"],
                        range=[EASY_DIFFICULTY, MED_DIFFICULTY, HARD_DIFFICULTY],
                    ),
                ),
                tooltip=alt.Tooltip(["Difficulty:N", "Problem count:Q"]),
            )
        )
        .properties(title="Problems by Difficulty")
        .configure_legend(
            labelFontSize=22,
            titleFontSize=26,
        )
        .configure_title(fontSize=24)
    )
    st.altair_chart(chart, use_container_width=True)
