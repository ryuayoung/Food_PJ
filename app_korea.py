import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def run_korea_app () :

    st.subheader('📌Korea')
    
    df = pd.read_csv('./data/sosangin.csv')
    
    df = df[['상호명','상권업종대분류명','상권업종중분류명','상권업종소분류명','지번주소','건물명']]
    df.isna().sum()
    df = df.fillna('') # NaN 값을 '' 로 대체

    # df_food = df[df['상권업종대분류명'] == '음식']
    df_korea=df[df['상권업종중분류명'] == '한식']
    df_korea = df_korea.reset_index()
    df_korea = df_korea.drop('index', axis=1)


# 굳이 안넣어도 되려나

      #  한식
    if st.checkbox('인천 한식당 전체 보기') :
            st.dataframe( df_korea )
    else :
            st.text('')

    choice = st.selectbox('한식 카테고리를 선택하세요. ✔',set(df_korea['상권업종소분류명']))

    if choice == '해산물 구이/찜':
            selected_df = df_korea[df_korea['상권업종소분류명'] == '해산물 구이/찜']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1            
            st.dataframe(selected_df)
    elif choice == '소고기 구이/찜' :
            selected_df = df_korea[df_korea['상권업종소분류명'] == '소고기 구이/찜']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '닭/오리고기 구이/찜' :
            selected_df = df_korea[df_korea['상권업종소분류명'] == '닭/오리고기 구이/찜']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '횟집' :
            selected_df = df_korea[df_korea['상권업종소분류명'] == '횟집']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '복 요리 전문' :
            selected_df = df_korea[df_korea['상권업종소분류명'] == '복 요리 전문']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '냉면/밀면' :
            selected_df = df_korea[df_korea['상권업종소분류명'] == '냉면/밀면']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '전/부침개' :
            selected_df = df_korea[df_korea['상권업종소분류명'] == '전/부침개']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '국/탕/찌개류' :
            selected_df = df_korea[df_korea['상권업종소분류명'] == '국/탕/찌개류']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '백반/한정식' :
            selected_df = df_korea[df_korea['상권업종소분류명'] == '백반/한정식']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '기타 한식 음식점' :
            selected_df = df_korea[df_korea['상권업종소분류명'] == '기타 한식 음식점']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '곱창 전골/구이' :
            selected_df = df_korea[df_korea['상권업종소분류명'] == '곱창 전골/구이']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '족발/보쌈' :
            selected_df = df_korea[df_korea['상권업종소분류명'] == '족발/보쌈']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    elif choice == '돼지고기 구이/찜' :
            selected_df = df_korea[df_korea['상권업종소분류명'] == '돼지고기 구이/찜']
            selected_df = selected_df.reset_index(drop=True)   
            selected_df.index += 1
            st.dataframe(selected_df)
    else :
           st.text('')

