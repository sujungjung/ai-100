import streamlit as st

st.title('동물 잊미 찾아주기')

title = st.text_input('영어로 동물 이름을 입력하세요')
if st.button('찾아보기'):
    st.write(title)
    st.image