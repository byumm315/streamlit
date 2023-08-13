import streamlit as st
import pandas as pd
from datetime import date

df = pd.read_csv("avocado.csv")
df['date'] = df['date'].apply(lambda x: date.fromisoformat(x))

# [TODO] 달력창이 뜨는 수정가능한 테이블 삽입
new_df = st.data_editor(df,
                        column_config={
                            "date":st.column_config.DateColumn('Date')
                        })
#테이블 안에 그래프, 체크박스, 이미지 등을 넣을 수 있도록 돕는 기능
