"""Breakdown of problems by difficulty."""

import altair as alt
import pandas as pd
import streamlit as st

from constants.colors import EASY_DIFFICULTY, HARD_DIFFICULTY, MED_DIFFICULTY


def breakdown_bar(df: pd.DataFrame):
    """Render a bar chart visualizing problems by difficulty.

    Args:
        df (pd.DataFrame): DataFrame containing at least 'Problem count' and
        'Difficulty' columns.

    Displays:
        An Altair bar chart using streamlit, illustrating the distribution of
        problem counts across different difficulties.
    """
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("Difficulty:N", sort=alt.SortField("_difficulty_enum:O")),
            y=alt.Y("Problem count:Q", axis=alt.Axis(tickMinStep=1)),
            color=alt.Color("Topic:N"),
            tooltip=alt.Tooltip(["Difficulty:N", "Problem count:Q"]),
        )
    )

    text = chart.mark_text(align="center", baseline="middle").encode(
        text=alt.Text("Problem count:Q")
    )

    st.altair_chart(
        alt.layer(chart.mark_bar(), text)
        .properties(title="Breakdown of Problems")
        .configure_axis(
            labelFontSize=22,
            titleFontSize=18,
        )
        .configure_legend(
            labelFontSize=22,
            titleFontSize=26,
        )
        .configure_title(fontSize=24),
        use_container_width=True,
    )
