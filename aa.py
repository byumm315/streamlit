import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
st.set_page_config(
    page_title="Home"
)
st.title('Wind Speed Predictor') #홈페이지 제목추가
st.header('Wind Data')
st.image('https://images.nationalgeographic.org/image/upload/t_edhub_resource_key_image/v1652340973/EducationHub/photos/wind-farm.jpg')
data=pd.read_csv('wind_train.csv') #해당 데이터는 github에 업로드하면 파일 경로가 필요없다.
data=data.drop('ID',axis=1)

change_names=['월','일','시간대','섭씨온도','절대온도','이슬점','상대습도','대기압','포화증기압','실제증기압','증기압부족량',
              '수증기함량','공기밀도','풍향','풍속']
for i,j in zip(data.columns,change_names):
    data.rename(columns={i:j},inplace=True)

st.write(data.head(20))
#히스토그램 그리기

st.subheader('The Histogram of Wind data')
vari1 = st.selectbox(label = "Choose a Variable", options = data.drop(['월','일','시간대'],axis=1).columns,key=1)
fig4 = px.histogram(data,x=vari1,nbins=100)
st.plotly_chart(fig4)
#막대그래프 그리기

st.subheader('The Bar plots of Wind data')
v2_list = ['섭씨온도','절대온도','이슬점','상대습도','대기압','포화증기압','실제증기압','증기압부족량',
              '수증기함량','공기밀도','풍향','풍속']
vari2 = st.selectbox(label = "Choose a Variable", options = v2_list,key=1)
title = f"The Bar plot of Month, Time Zone and {vari2}"
fig = px.bar(data, x = '월', y = vari2,color="시간대", barmode = 'group',title=title)
st.plotly_chart(fig)
