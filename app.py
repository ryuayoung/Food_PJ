import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from app_china import run_china_app
from app_japan import run_japan_app
from app_korea import run_korea_app

def main() :

    st.title('인천 음식점 카테고리 대시보드')

    menu = ["Home", "Korea" , "China" , "Japan"]
    choice = st.sidebar.selectbox("메뉴 선택", menu)

    if choice == menu[1] :
        run_korea_app()

    elif choice == menu[2] :
        run_china_app()

    elif choice == menu[3] :
        run_japan_app()


if __name__ == '__main__' :
    main()