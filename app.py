from tkinter import OptionMenu
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from app_china import run_china_app
from app_japan import run_japan_app
from app_korea import run_korea_app

def main() :
    df_food = pd.read_csv('./data/sosangin.csv')
    menu = ["Home", "Korea" , "China" , "Japan"]

    choice = st.sidebar.selectbox("메뉴 선택", menu)

    if choice == menu[0] :
        col1,col2 = st.columns([2,3])
        with col1 :
            st.markdown('# Incheon Restaurant 🍽')
            st.markdown('## ◽ Category List ◽')
        with col2 :
            st.subheader('소상공인시장진흥공단의')
            st.subheader('인천지역 상가정보입니다.')
            st.text('( 2023년 9월 기준 데이터 )')
            st.text("인천에 입점된 식당들을 ")
            st.text('음식 종류에 따라 찾아볼 수 있습니다.😍')
            st.info("메뉴에서 Korea, China, Japan 을 선택해주세요~!")
            
            if st.checkbox('인천지역의 [ 한식 / 중식 / 일식 ] 점포 통계확인') :
                st.subheader('Chart')
            
                df_food = df_food[['상호명','상권업종대분류명','상권업종중분류명','상권업종소분류명','지번주소','건물명','경도','위도']]
                df_food.isna().sum()
                df_food = df_food.fillna('') # NaN 값을 '' 로 대체
                df_food = df_food.reset_index()
                df_food = df_food.drop('index', axis=1)
                df_food = df_food[df_food['상권업종대분류명'] == '음식']
                idx = df_food[df_food['상권업종중분류명'].str.contains('구내식당·뷔페|기타 간이|서양식|비알코올 |주점|동남아시아|기타 외국')].index
                df_food = df_food.drop( idx )

                base_order2 = df_food['상권업종중분류명'].value_counts().index
                base_color = sb.color_palette("pastel")

                fig, ax = plt.subplots()  # figure 객체 생성

                sb.countplot( data = df_food, x = '상권업종중분류명', order= base_order2, palette= base_color)
                plt.title('Food By Type')
                plt.xticks(ticks=range(len(base_order2)), labels=['Korea Food', 'China Food', 'Japan Food'])
                plt.xlabel('')
                ax = plt.gca()

                for p in ax.patches:
                    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='baseline', fontsize=8, color='black', xytext=(0, 5),
                        textcoords='offset points')
                st.pyplot(fig)

                st.success('한식점포 총 15,317개')
                st.info('중식점포 총 1,594개')
                st.info('일식점포 총 1,045개')

                st.subheader('Pie Chart')  # 파이차트 그리기

                fig, ax2 = plt.subplots()  # 두 번째 figure 객체 생성
                df2 = df_food['상권업종중분류명'].value_counts()
                labels_list = ['Korea', 'China', 'Japan']
                colors_list = ['#FFD1DC', '#FFFACD', '#98FB98']
                plt.pie(df2, labels=labels_list, autopct='%.1f', startangle=70, wedgeprops={'width': 0.7}, colors=colors_list)
                plt.legend()
                plt.title('Incheon Food By Type Pie Chart')
                st.pyplot(fig)

                st.warning('한식점포 85.3% / 중식점포 8.9% / 일식점포 5.8%')
        

    else :
            st.text('')

    if choice == menu[1] :
        run_korea_app()

    elif choice == menu[2] :
        run_china_app()

    elif choice == menu[3] :
        run_japan_app()


if __name__ == '__main__' :
    main()