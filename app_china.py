import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def run_china_app() :

    st.subheader('China')

    df = pd.read_csv('./data/sosangin.csv')

    df = df[['상호명','상권업종대분류명','상권업종중분류명','상권업종소분류명','지번주소','건물명']]
    df.isna().sum()
    df = df.fillna('') # NaN 값을 '' 로 대체

    df_china=df[df['상권업종중분류명'] == '중식']
    df_china = df_china.reset_index()
    df_china = df_china.drop('index', axis=1)

    # 중식
    if st.checkbox('중식 데이터 프레임 보기') :
            st.dataframe( df_china )
    else :
            st.text('')

    choice = st.selectbox('중식 카테고리 선택',set(df_china['상권업종소분류명']))
    
    if choice == '중국집':
           # 중국집 선택 시 출력
            selected_df = df_china[df_china['상권업종소분류명'] == '중국집']
            st.dataframe(selected_df)
    elif choice == '마라탕/훠궈' :
           # 마라탕/훠궈 선택 시 출력
            selected_df = df_china[df_china['상권업종소분류명'] == '마라탕/훠궈']
            st.dataframe(selected_df)
    else :
           st.text('')