"""Leetcode tracker data viz."""

import logging

import numpy as np
import pandas as pd
import streamlit as st

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

st.set_page_config(
    page_title="Leetcode tracker",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    st.title("")
    st.header("Show graphs")
    st.subheader("Graphs")
    st.write("**Markdown supported**")

    df = pd.DataFrame(
        [
            [(c[0] / 100) + 47.66676293891633, ((c[1] / 100) + 117.40216206237741) * -1]
            for c in np.random.randn(20, 2)
        ],
        columns=["lat", "lon"],
    )
    st.map(df)

    if st.checkbox("Show data"):
        st.write(df)


if __name__ == "__main__":
    main()
