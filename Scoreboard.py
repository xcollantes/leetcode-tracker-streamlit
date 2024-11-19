"""Leetcode tracker data viz."""

import logging

import altair as alt
import pandas as pd
import streamlit as st

from components import calendar
from constants.colors import EASY_DIFFICULTY, HARD_DIFFICULTY, MED_DIFFICULTY
from data_sources.sheets import get_sheet_data
from modules.page_config import PageConfig

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

PageConfig().get_config()


def main():
    st.title("Leetcode Scoreboard")

    df: pd.DataFrame = get_sheet_data()

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("Problem count:Q", axis=alt.Axis(format="d")),
            y=alt.Y("Tab:N", sort="-x"),
            color=alt.Color(
                "Difficulty:N",
                scale=alt.Scale(
                    domain=["Easy", "Med", "Hard"],
                    range=[EASY_DIFFICULTY, MED_DIFFICULTY, HARD_DIFFICULTY],
                ),
            ),
            # color=alt.Color(
            #     "Difficulty:N",
            #     sort=alt.SortField("_difficulty_enum:O", order="ascending"),
            #     scale=alt.Scale(scheme="redyellowgreen"),
            # ),
            tooltip=alt.Tooltip(["Tab:N", "Difficulty:N", "Problem count:Q"]),
        )
        .configure_title(fontSize=20)
        .configure_axis(
            labelFontSize=26,
            titleFontSize=18,
        )
        .configure_legend(
            labelFontSize=22,
            titleFontSize=26,
        )
        .properties(width=600, height=400)
    )

    st.altair_chart(chart, use_container_width=True)

    calendar.calendar(df)

    # Display DataFrame.
    st.dataframe(df, use_container_width=True, hide_index=True)


def style_dataframe(val):
    color = "green" if val > 20 else "orange" if val > 10 else "red"
    return f"background-color: {color};"


if __name__ == "__main__":
    main()
