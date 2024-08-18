import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
        st.write("NumPy is a powerful Python library used for numerical computations. It provides support for arrays and matrices, along with a collection of mathematical functions to operate on these data structures efficiently. It's widely used in data science, machine learning, and scientific computing for its speed and versatility.")
        st.write("(1)Install library")
        st.code("pip install numpy")
        st.write("(2)Import library")
        st.code("import numpy as np")
        st.divider()
            
        st.subheader("1. N차원 배열")
        numpy_1, numpy_2 = st.columns(2)
        with numpy_1:
            arr1 = np.array([1,2,3])
            st.code('''
                        #1차원
                        arr1 = np.array([1,2,3])
                    ''')
            st.write(arr1)
        with numpy_2:
            arr2 = np.array([[1,2,3],
                            [4,5,6]])
            st.code('''
                    #2차원
                    arr2 = np.array([1,2,3], [4,5,6]))
            ''')
            st.write(arr2)
        st.divider()
        
        st.subheader("2. 차원 생성")
        numpy_3, numpy_4 = st.columns(2)
        with numpy_3:
            tuple_arr1 = (4,5,6)
            tuple_arr1_result = np.array(tuple_arr1)
            st.code('''
                    #튜플로 1차원
                    tuple_arr1 = (4,5,6)
                    tuple_arr1_result = np.array(tuple_arr1)
            ''')
            st.write(tuple_arr1_result)
        with numpy_4:
            lst_1 = [1,2,3]
            arr_lst1 = np.array(lst_1)
            st.code('''
            #리스트로 1차원
            lst_1 = [1,2,3]
            arr_lst1 = np.array(lst_1)''')
            st.write(arr_lst1)

        lst_2 = [[1,2,3],[4,5,6]]
        arr_list2 = np.array(lst_2)            
        st.code('''
                #리스트로 2차원
                lst_2 = [[1,2,3],[4,5,6]]
                arr_list2 = np.array(lst_2)
                ''')
        st.write(arr_list2)    
        st.divider()
        
        
        st.subheader("4. N차원 형태 및 사이즈")
        numpy_5, numpy_6 = st.columns(2)
        with numpy_5:
            shape_arr1 = np.array([1,2,3])
            st.code('''
                #1차원/차원/형태/크기
                shape_arr1 = np.array([1,2,3])
                shape_arr1.ndim
                shape_arr1.shape
                shape_arr1.size
                    ''')
            st.write(shape_arr1)
            st.write(f"차원 : {shape_arr1.ndim}")
            st.write(f"형태 : {shape_arr1.shape}")
            st.write(f"크기 : {shape_arr1.size}")
            
        with numpy_6:
            shape_arr2 = np.array([[1,2,3],[4,5,6]])
            st.code('''
                #2차원/차원/형태/크기
                shape_arr2 = np.array([[1,2,3],[4,5,6]])
                shape_arr2.ndim
                shape_arr2.shape
                shape_arr2.size
                    ''')
            st.write(shape_arr2)
            st.write(f"차원 : {shape_arr2.ndim}")
            st.write(f"형태 : {shape_arr2.shape}")
            st.write(f"크기 : {shape_arr2.size}")
        st.divider()
        
        st.subheader("5. N차원 배열의 타입")
        numpy_7, numpy_8 = st.columns(2)
        with numpy_7:
            st.code('''
                    normal_arr = np.array([1,2,3])
                    normal_arr
                    normal_arr.dtype
                    ''')
            normal_arr = np.array([1,2,3])
            normal_arr
            normal_arr.dtype
            st.write(f"타입 : {normal_arr.dtype}")
            
        with numpy_8:
            st.code('''
                    float_arr = np.array([1,2,3], dtype=np.float64)
                    float_arr
                    float_arr.dtype
                    ''')
            float_arr = np.array([1,2,3], dtype=np.float64)
            float_arr
            float_arr.dtype
            st.write(f"타입 : {float_arr.dtype}")
        st.code('''
            int_float_arr = np.array([1.1,2.2,3.3], dtype=np.int64)
            int_float_arr
            int_float_arr.dtype
            #타입변경 : .astype
            int_float_arr.astype(np.float64)
        ''')
        int_float_arr = np.array([1.1,2.2,3.3], dtype=np.int64)
        int_float_arr
        int_float_arr.dtype
        st.write(f"타입 : {int_float_arr.dtype}")
        st.divider()
        
        st.subheader("6. 정해진 형식의 N차원 배열")
        st.write("(1) 1차원")
        numpy_9, numpy_10, numpy_11 = st.columns(3)
        with numpy_9:
            st.code('''
                    zero_arr = np.zeros([2,2])
                    ''')
            zero_arr = np.zeros([2,2])    
            st.write(zero_arr)
        
        with numpy_10:
            st.code('''
                    ones_arr = np.ones([3,5])
                    ''')
            ones_arr = np.ones([3,5])
            st.write(ones_arr)

        with numpy_11:
            st.code('''
                    full_arr = np.full((2,3), 5)
                    ''')
            full_arr = np.full((2,3), 5)  
            st.write(full_arr)
        
        
        st.write("(2) 2차원")
        st.code('''
                def_arr_2 = np.array([[1,2,3],
                    [4,5,6]])
                def_arr_2_zero = np.zeros_like(def_arr_2)
                def_arr_2_ones = np.ones_like(def_arr_2)
                def_arr_2_full = np.full_like(def_arr_2, 9)
                ''')
        numpy_12, numpy_13, numpy_14 = st.columns(3)
        
        def_arr_2 = np.array([[1,2,3],
                [4,5,6]])
        with numpy_12:
            st.write("zeros_like")
            def_arr_2_zero = np.zeros_like(def_arr_2)
            st.write(def_arr_2_zero)
        with numpy_13:
            st.write("ones_like")
            def_arr_2_ones = np.ones_like(def_arr_2)
            st.write(def_arr_2_ones)
        with numpy_14:
            st.write("full_like")
            def_arr_2_full = np.full_like(def_arr_2, 9)
            st.write(def_arr_2_full)
        st.divider()
        
        st.subheader("7. 특정범위 값을 가지는 N차원 배열")
        numpy_15, numpy_16 = st.columns(2)
        with numpy_15:
            st.code('''
                     arr_arange = np.arange(9)
                     ''')
            arr_arange = np.arange(9)
            st.write(arr_arange)
        with numpy_16:
            st.code('''
                     arr_arange_start = np.arange(3,12)
                     ''')
            arr_arange_start = np.arange(3,12)
            st.write(arr_arange_start)
        
        numpy_17, numpy_18 = st.columns(2)
        with numpy_17:
            st.code('''
                     arr_arange_step = np.arange(start = 0, stop = 10, step = 2)
                     ''')
            arr_arange_step = np.arange(start = 0, stop = 10, step = 2)
            st.write(arr_arange_step)
        with numpy_18:
            st.code('''
                     arr_arange_linspace = np.linspace(0,100,11) #지정한 개수만큼 출력
                     ''')
            arr_arange_linspace = np.linspace(0,100,11) #지정한 개수만큼 출력
            st.write(arr_arange_linspace)
        st.code('''
                #1: 시작 지수 (로그 스케일에서).
                #10: 끝 지수 (로그 스케일에서).
                #10: 생성할 숫자의 개수.
                #base=2: 로그 스케일의 밑(base)을 2로 설정.
                arr_arange_loogspace = np.logspace(1,10,10, base=2) #10개원소와 2부터 시작
                ''')
        arr_arange_loogspace = np.logspace(1,10,10, base=2)
        st.write(arr_arange_loogspace)
        st.divider()
        
        st.subheader("8. 난수로 N 차원 배열 생성")
        numpy_19, numpy_20 = st.columns(2)
        with numpy_19:
            st.code('''
                    #정규분포에서 표본 추출 (평균, 표준편차, 사이즈)
                    arr_random = np.random.normal(0, 1, 10)     
                    ''')
            arr_random = np.random.normal(0, 1, 10)  
            st.write(arr_random)
        with numpy_20:
            st.code('''
                    #정규분포에서 표본 추출 (평균, 표준편차, 사이즈)
                    arr_random = np.random.normal(0, 1, (3,3))  
                    ''')
            arr_random = np.random.normal(0, 1, (3,3))  
            st.write(arr_random)
        st.write("rand() : 0과 1 사이에서 균등 분포(Uniform Distribution)를 따르는 난수를 생성")
        st.code('''
                arr_rand = np.random.rand(1000)
                plt.hist(arr_rand,bins=100)
                plt.show()
                ''')    
        arr_rand = np.random.rand(1000)
        # 히스토그램 그리기
        fig, ax = plt.subplots()
        ax.hist(arr_rand, bins=100, color='blue', edgecolor='black')
        # Streamlit을 통해 히스토그램 출력
        st.pyplot(fig)
        
        st.write("randn() : 함수는 평균이 0이고 표준편차가 1인 표준 정규분포(Normal Distribution)를 따르는 난수를 생성")
        st.code('''
                arr_randn = np.random.randn(1000)
                plt.hist(arr_randn,bins=100)
                plt.show()
                ''')    
        arr_randn = np.random.randn(1000)
        # 히스토그램 그리기
        fig1, ax = plt.subplots()
        ax.hist(arr_randn, bins=100, color='blue', edgecolor='black')
        # Streamlit을 통해 히스토그램 출력
        st.pyplot(fig1)
        
        numpy_21, numpy_22 = st.columns(2)
        with numpy_21:
            st.code('''
                    #randint 정수로 랜덤한값
                    arr_randint = np.random.randint(low=1,high=5, size=10)
                    arr_randint
                    ''')
            arr_randint = np.random.randint(low=1,high=5, size=10)
            st.write(arr_randint)
        with numpy_22:
            st.code('''
                    arr_randint = np.random.randint(low=1,high=10, size=(3,4))
                    arr_randint
                    ''')
            arr_randint = np.random.randint(low=1,high=10, size=(3,4))
            st.write(arr_randint)
        st.code('''
                #히스토그램 100~200 1000개
                arr_hiso = np.random.randint(100,200,1000)
                plt.hist(arr_hiso, bins=100)
                plt.show()
                ''')
        arr_hiso = np.random.randint(100,200,1000)
        # 히스토그램 그리기
        fig2, ax = plt.subplots()
        ax.hist(arr_hiso, bins=100, color='blue', edgecolor='black')
        # Streamlit을 통해 히스토그램 출력
        st.pyplot(fig2)
        st.divider()
        
        st.subheader("9. Seed 값으로 난수생성 제어")
        numpy_23, numpy_24= st.columns(2)
        with numpy_23:
            st.code('''
                    arr_nansoo = np.random.rand(10)
                    st.write(arr_nansoo)
                    ''')
            arr_nansoo = np.random.rand(10)
            st.write(arr_nansoo)
        with numpy_24:
            st.code('''
                    np.random.seed(10)
                    arr_nansoo_1 = np.random.rand(10)
                    ''')
            np.random.seed(10)
            arr_nansoo_1 = np.random.rand(10)
            st.write(arr_nansoo_1)
        st.divider()
        
        st.subheader("10. Index로 배열 조회")
        numpy_25, numpy_26 = st.columns(2)
        with numpy_25:
            st.code('''arr_1_index = np.arange(10)
            arr_1_index[1]
            arr_1_index[0]
            arr_1_index[9]
            arr_1_index[-1]
            arr_1_index[3:8]''')
            arr_1_index = np.arange(10)
            st.write(arr_1_index)
            st.write(f"인덱스 1 : {arr_1_index[1]}")
            st.write(f"인덱스 0 : {arr_1_index[0]}")
            st.write(f"인덱스 9 : {arr_1_index[9]}")
            st.write(f"인덱스 -1 : {arr_1_index[-1]}")
            st.write(f"인덱스 3~8 : {arr_1_index[3:8]}")
        with numpy_26:
            st.code('''arr_2_index = np.array([[1,2,3,4,5],
                        [6,7,8,9,10],
                        [11,12,13,14,15]])
                        arr_2_index[0,:]
                        arr_2_index[0,3]
                        arr_2_index[-1,3]
                        arr_2_index[0:2,2:4]''')
            arr_2_index = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
            st.write(arr_2_index)
            st.write(f"인덱스 0행 전체 열  : {arr_2_index[0,:]}")
            st.write(f"인덱스 0행 3열 : {arr_2_index[0,3]}")
            st.write(f"인덱스 마지막 행 3열 : {arr_2_index[-1,3]}")
            st.write(f"인덱스 0-1행, 2-3열 : {arr_2_index[0:2,2:4]}")
        st.write("**fancy indexing : 특정 인덱스를 여러개 선택하여 탐색")
        numpy_27, numpy_28 = st.columns(2)
        with numpy_27:
            st.code('''
                    arr_1_fancy = np.arange(10)
                    arr_1_fancy[[0,4,8]]
                    ''')
            arr_1_fancy = np.arange(10)
            st.write(arr_1_fancy)
            st.write(f"인덱스 0번째, 4번쨰, 8번쨰")
            arr_1_fancy[[0,4,8]]
        with numpy_28:
            st.code('''
                    arr_2_fancy = np.array([[5,10,15,20],
                        [25,30,35,40],
                        [45,50,55,60]])
                        arr_2_fancy[[0,2],2:]
                    ''')    
            arr_2_fancy = np.array([[5,10,15,20],
                        [25,30,35,40],
                        [45,50,55,60]])
            st.write(arr_2_fancy)
            st.write("인덱스 행 0, 2번쨰, 열 2번째부터 전부")
            arr_2_fancy[[0,2],2:]
        st.write("**boolean indexing : True 요소 선택, False 요소 제외")
        st.code('''
                arr_1_boolean = np.arange(10)
                arr_1_boolean[[True,False,True,False,True,False,True,False,True,False]]
                ''')
        arr_1_boolean = np.arange(10)
        st.write(arr_1_boolean)
        st.write("arr_1_boolean[[True,False,True,False,True,False,True,False,True,False]]")
        arr_1_boolean[[True,False,True,False,True,False,True,False,True,False]]
        st.code('''
                arr_2_boolean = np.array([[1,2,3,4],
                         [5,6,7,8],
                         [9,10,11,12]])
                ''')
        arr_2_boolean = np.array([[1,2,3,4],
                         [5,6,7,8],
                         [9,10,11,12]])
        st.write(arr_2_boolean)
        st.write("arr_2_boolean[[False,True,False],True]")
        arr_2_boolean[[False,True,False],True]
        st.write("조건에 의한 배열 추출 : 6 이상인 요소")
        arr_2_boolean[arr_2_boolean>=6]
        st.divider()
        
        st.subheader("11. N차원 연산 : 연산하고자 할 때 배열의 shape이 같아야함. 물론 shape이 다르면 broadcasting으로 연산이 가능함")
        arr_cal_2 = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12]])
        st.write(arr_cal_2)
        arr_cal_2_other = np.array([[2,2,2],
                        [2,2,2],
                        [2,2,2],
                        [2,2,2]])
        st.write(arr_cal_2_other)
        st.code('''
                np.add(arr_cal_2,arr_cal_2_other)
                np.subtract(arr_cal_2,arr_cal_2_other)
                np.multiply(arr_cal_2,arr_cal_2_other)
                np.divide(arr_cal_2,arr_cal_2_other)
                ''')
        numpy_29, numpy_30, numpy_31, numpy_32 = st.columns(4)
        with numpy_29:
            st.write("np.add(arr_cal_2,arr_cal_2_other)")
            npadd = np.add(arr_cal_2,arr_cal_2_other)
            npadd
        with numpy_30:
            st.write("np.subtract(arr_cal_2,arr_cal_2_other)")
            npsub = np.subtract(arr_cal_2,arr_cal_2_other)
            npsub
        with numpy_31:
            st.write("np.multiply(arr_cal_2,arr_cal_2_other)")
            npmul = np.multiply(arr_cal_2,arr_cal_2_other)
            npmul
        with numpy_32:
            st.write("np.divide(arr_cal_2,arr_cal_2_other)")
            npdiv = np.divide(arr_cal_2,arr_cal_2_other)
            npdiv
        st.divider()
        arr_cal_2
        st.code('''
                #제곱
                np.square(arr_cal_2)
                #또는 arr_cal_2 ** 3
                #제곱근
                np.sqrt(arr_cal_2)
                #몫
                arr_cal_2 // 2
                #나머지
                arr_cal_2 % 2
                ''')
        numpy_33, numpy_34, numpy_35, numpy_36 = st.columns(4)
        with numpy_33:
            st.write("np.square(arr_cal_2)")
            arrsq = np.square(arr_cal_2)
            arrsq
        with numpy_34:
            st.write("np.sqrt(arr_cal_2)")
            arrsqrt = np.sqrt(arr_cal_2)
            arrsqrt
        with numpy_35:
            st.write("arr_cal_2 // 2")
            arrcal_1 = arr_cal_2 // 2
            arrcal_1
        with numpy_36:
            st.write("arr_cal_2 % 2")
            arrcal_2 = arr_cal_2 % 2
            arrcal_2