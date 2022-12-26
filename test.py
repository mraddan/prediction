import streamlit as st
import time
import pandas as pd

# tab1, tab2 = st.tabs(['A','B'])
# with tab1:
#        col1,col2 = st.columns(2)
#        col1.text('p')
#        col2.text('p')
# with tab2:
#        col3,col4 = st.columns(2)
#        col3.text('p')
#        col4.text('p')
df = pd.read_csv("EPLDataset.csv")
