import streamlit as st

st.title('동물 이미지 찾아주기')

title = st.text_input('영어로 동물 이름을 입력하세요')
if st.button('찾아보기'):
    url = 'http://edu.spartacodingclub.kr/random/?'+ title
    st.image(url)
