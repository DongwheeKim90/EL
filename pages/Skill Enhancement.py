import streamlit as st
import numpy as np

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

st.divider()
#Python, English
study_zone_1, study_zone_2 = st. tabs(["Python","English"])
#Python zone
with study_zone_1:
    select_value_python = st.radio("Choice Python library what you want.",
            [":rainbow[***PANDAS***]",":rainbow[***NUMPY***]",":rainbow[***Pythorch***]"]
            )
    if select_value_python == ":rainbow[***PANDAS***]":
        st.subheader("Pandas Intro")        
    
    
    
    
    
    
    
    elif select_value_python == ":rainbow[***NUMPY***]":
        st.subheader("About Numpy")
        intro_container = st.container()
        with intro_container:
            st.write("NumPy is a powerful Python library used for numerical computations. It provides support for arrays and matrices, along with a collection of mathematical functions to operate on these data structures efficiently. It's widely used in data science, machine learning, and scientific computing for its speed and versatility.")
            st.code("pip install numpy")
            
        numpy_1, numpy_2 = st.columns(2)
        st.subheader("1.N차원 배열")
        arr1 = np.array([1,2,3])
        st.code('''
                    #1차원
                    arr1 = np.array([1,2,3])
                ''')
        st.write(arr1)
        
        arr2 = np.array([[1,2,3],
                        [4,5,6]])
        st.code('''
                #2차원
                arr2 = np.array([1,2,3],
                            [4,5,6]))
        ''')
        st.write(arr2)
        
        st.subheader("2.차원 생성")
        tuple_arr1 = (4,5,6)
        tuple_arr1_result = np.array(tuple_arr1)
        st.code('''
                #튜플로 1차원
                tuple_arr1 = (4,5,6)
                tuple_arr1_result = np.array(tuple_arr1)
        ''')
        st.write(tuple_arr1_result)

        lst_1 = [1,2,3]
        arr_lst1 = np.array(lst_1)
        st.code('''
        lst_1 = [1,2,3]
        arr_lst1 = np.array(lst_1)
                #리스트로 1차원
                lst_1 = [1,2,3]
                arr_lst1 = np.array(lst_1)
                ''')
        st.write(arr_lst1)

        lst_2 = [[1,2,3],[4,5,6]]
        arr_list2 = np.array(lst_2)            
        st.code('''
                #리스트로 2차원
                lst_2 = [[1,2,3],[4,5,6]]
                arr_list2 = np.array(lst_2)
                ''')
        st.write(arr_list2)    
        
        
        st.subheader("2.N차원 형태 및 사이즈")
        st.code('''
            #1차원/차원/형태/크기
            shape_arr1 = np.array([1,2,3])
            shape_arr1.ndim
            shape_arr1.shape
            shape_arr1.size
                ''')
        shape_arr2 = np.array([[1,2,3],[4,5,6]])
        st.code('''
            #2차원/차원/형태/크기
            shape_arr2 = np.array([[1,2,3],[4,5,6]])
            shape_arr2.ndim
            shape_arr2.shape
            shape_arr2.size
                ''')