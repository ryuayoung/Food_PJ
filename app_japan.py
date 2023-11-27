import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def run_japan_app() :

    st.subheader('📌Japan')

    df = pd.read_csv('./data/sosangin.csv')

    df = df[['상호명','상권업종대분류명','상권업종중분류명','상권업종소분류명','지번주소','건물명']]
    df.isna().sum()
    df = df.fillna('') # NaN 값을 '' 로 대체

    df_japan=df[df['상권업종중분류명'] == '일식']
    df_japan = df_japan.reset_index()
    df_japan = df_japan.drop('index', axis=1)
    
    # 일식
    if st.checkbox('인천 일식당 전체 보기') :
            st.dataframe( df_japan )
    else :
            st.text('')

    choice = st.selectbox('일식 카테고리를 선택하세요. ✔',set(df_japan['상권업종소분류명']))

    if choice == '일식 면 요리':
            selected_df = df_japan[df_japan['상권업종소분류명'] == '일식 면 요리']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '기타 일식 음식점' :
            selected_df = df_japan[df_japan['상권업종소분류명'] == '기타 일식 음식점']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '일식 카레/돈가스/덮밥' :
            selected_df = df_japan[df_japan['상권업종소분류명'] == '일식 카레/돈가스/덮밥']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '일식 회/초밥' :
            selected_df = df_japan[df_japan['상권업종소분류명'] == '일식 회/초밥']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    else :
           st.text('')
