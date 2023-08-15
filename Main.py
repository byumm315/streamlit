import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
st.set_page_config(
    page_title="Home"
)
st.title('Product Review Analysis') #홈페이지 제목추가
st.header('Topic Modeling - Using BERTopic')
st.image('http://img.choroc.com/newshop/goods/009179/009179_1.jpg')
st.subheader('Data samples')
data=pd.read_csv('ottugi_review_topic_1.csv')
st.write(data.head(20))
