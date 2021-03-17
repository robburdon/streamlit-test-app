import streamlit as st
import numpy as np
import pandas as pd



st.title('What have I done')

st.write("Do you like my table")

data = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': ["I", "have", "a", "problem"]
})

st.write(data)

st.write("And this is where the spiders are:")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [50.07, 14.4],
    columns=['lat', 'lon'])

st.map(map_data)
