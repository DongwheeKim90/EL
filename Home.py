#Bring Library
import streamlit as st

#Header area
#-제목
st.title("EL Company🔆")
#-부제목
st.subheader("We are :red[the East Light from sun.]")
#-이미지
#--스트림릿 상에서 직접 css 조정을 원할시 unsafe_allow_html 파라메터 True 지정
st.markdown('''
    <img src="C:/EL/elImage/EL_sample_logo.png" alt="EL LOGO" style=""/>
    ''', unsafe_allow_html=True)

#st.image("C:/EL/elImage/EL_sample_logo.png",
#        caption="The EL company LOGO",
#        width=300
#        )