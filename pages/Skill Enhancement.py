import streamlit as st

#헤더 
st.title("The skill Enhancement zone✍🏻")
st.divider()
skill_head_1, skill_head_2 = st.columns([0.7,0.3])
with skill_head_1:
    st.write("This page aims to enhance skills.")
    st.write("You can learn about Python as a programming language and study English.")
    st.write("EL is looking to work with individuals who are committed to continuous growth in self-development and who have a strong passion for the tasks they are assigned. Just act without overthinking.")
with skill_head_2:
    st.image("useData/EL_img/EL_STUDY_COUPLE.png")

#Python, English
study_zone_1, study_zone_2 = st. tabs(["Python","English"])
#Python zone
with study_zone_1:
    select_value_python = st.radio("Choice Python library what you want.",
            [":rainbow[***PANDAS***]",":rainbow[***NUMPY***]"])
    if select_value_python == ":rainbow[***PANDAS***]":
        st.subheader("Pandas Intro")
        