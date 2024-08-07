import os
from openai import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))



st.title('슈퍼시나리오봇🤖')

keyword = st.text_input('키워드를 입력하세요')
if st.button('생성하기'):
    with st.spinner('잠시만용 ...'):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": keyword,
                },
                {
                    "role": "system",
                    "content": "홍보 포스터 만들기",
                }
            ],
            model="gpt-4o",
        )
        reponse = client.images.generate(
            model="dall-e-3",
            prompt="수채화 풍으로 그려줘",
            size="1024x1024",
            quality="standard",
            n=1,
        )
    result = chat_completion.choices[0].message.content
    image_url = reponse.data[0].url
    st.write(result)
    st.write(result)
    
