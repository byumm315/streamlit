import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

data=pd.read_csv('ottugi_review_total_1.csv')

st.subheader('Check the reviews by selecting a topic')
  
v_list=list(data['topic'].unique())
var1 = st.selectbox(label = "Choose a Topic", options = v_list,key=0)
title = f"Slect topic: {var1}"

st.DataFrame(data[data['topic']==var1])
