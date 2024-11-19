"""Github-like calendar heatmap."""

import datetime
from email.policy import default

import july
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from july.utils import date_range


def calendar(df: pd.DataFrame):
    """Render matplotlib figure of Github-like heatmap."""

    now: datetime.datetime = datetime.datetime.now()
    start_default: datetime.datetime = now - datetime.timedelta(days=90)

    default_dates: list = date_range(
        start_default.strftime("%Y-%m-%d"), now.strftime("%Y-%m-%d")
    )
    default_data: list[int] = [0] * len(default_dates)

    fig, ax = plt.subplots(figsize=(2, 2))

    july.heatmap(
        dates=(df["Date"] if len(df["Date"]) > 1 else default_dates),
        data=(df["Problem count"] if len(df["Date"]) > 1 else default_data),
        # dates=df["Date"],
        # data=df["Problem count"],
        month_grid=True,
        cmap="github",
        horizontal=True,
        value_label=False,
        date_label=False,
        weekday_label=True,
        month_label=True,
        year_label=True,
        colorbar=False,
        fontfamily="monospace",
        fontsize=5,
        titlesize="small",
        ax=ax,
    )

    # Display the plot in the Streamlit app.
    st.pyplot(fig, use_container_width=False)
