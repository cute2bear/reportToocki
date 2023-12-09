# ppomppu_toocki 프로젝트의 메인 파일입니다.
# ppomppu_toocki.xlsx 파일에는 크롤링한 결과가 있습니다.
# streamlit과 pandas를 이용하여 만들자
# 라이브러리 로드
import streamlit as st
import pandas as pd


def ReadData():
    # 데이터 로드
    df = pd.read_excel('ppomppu_toocki.xlsx', index_col=0)
    return df


# main function
if __name__ == '__main__':
    # 데이터 로드
    df = ReadData()
    # 사이드바
    st.sidebar.title('뽐뿌 & toocki')

    # 메인 화면
    st.title('뽐뿌 & toocki')
    st.write(df)