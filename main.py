import streamlit as st

st.set_page_config(
    page_title="전태환의 시각화",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get help': "https://docs.streamlit.io",
        'Report a bug': "https://streamlit.io",
        'About': "## 하정훈 교수\n- [홍익대학교 산업·데이터공학과](https://ie.hongik.ac.kr/ie/020)"
    }
)
st.sidebar.title("다양한 사이드바 위젯들")

st.sidebar.checkbox("외국인 포함")
st.sidebar.checkbox("고령인구 포함")
st.sidebar.divider()
st.sidebar.radio('데이터 타입',['남성','여성'])



st.write('# 아')
st.write('이앱은 Streamlit을 활용한 시각화 대시보드 예시입니당')
