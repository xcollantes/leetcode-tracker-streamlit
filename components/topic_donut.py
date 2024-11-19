"""Donut chart."""

import altair as alt
import pandas as pd
import streamlit as st


def topic(df: pd.DataFrame):
    """Render a donut chart visualizing problems by topic.

    Args:
        df (pd.DataFrame): DataFrame containing at least 'Problem count' and
        'Topic' columns.

    Displays:
        An Altair donut chart using streamlit, illustrating the distribution of
        problem counts across different topics.
    """
    chart = (
        (
            alt.Chart(df)
            .mark_arc(innerRadius=95)
            .encode(
                theta=alt.Theta("Problem count:Q"),
                color=alt.Color(
                    "Topic:N",
                ),
                tooltip=alt.Tooltip(["Difficulty:N", "Problem count:Q"]),
            )
        )
        .properties(title="Problems by Topic")
        .configure_legend(
            labelFontSize=22,
            titleFontSize=26,
        )
        .configure_title(fontSize=24)
    )
    st.altair_chart(chart, use_container_width=True)
