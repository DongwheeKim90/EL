import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#헤더 
st.title("The skill Enhancement zone✍🏻")
st.divider()
skill_head_1, skill_head_2 = st.columns([0.8,0.2])
with skill_head_1:
    st.subheader("This page aims to enhance skills.", anchor=False, help=None)
    st.write("You can learn about Python as a programming language and study English.")
    st.write("EL is looking to work with individuals who are committed to continuous growth in self-development and who have a strong passion for the tasks they are assigned. Just act without overthinking.")
    st.subheader("Don't stay stuck in the past or present.", anchor=False, help=None)
    st.write("While you revel in your past achievements or feel content with the present, someone else is continuously developing themselves to keep up with the rapidly changing world. We at EL are a collective and a company of leaders with diverse talents. We don’t just keep up with the pace of a changing world. we lead it.")
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
        
        
        st.subheader("3. N차원 형태 및 사이즈")
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
        
        st.subheader("4. N차원 배열의 타입")
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
        
        st.subheader("5. 정해진 형식의 N차원 배열")
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
        
        st.subheader("6. 특정범위 값을 가지는 N차원 배열")
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
        
        st.subheader("7. 난수로 N 차원 배열 생성")
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
        
        st.subheader("8. Seed 값으로 난수생성 제어")
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
        
        st.subheader("9. Index로 배열 조회")
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
        st.write("조건에 의한 배열 추출 : 6 이상인 요소(arr_2_boolean[arr_2_boolean>=6])")
        arr_2_boolean[arr_2_boolean>=6]
        st.divider()
        
        st.subheader("10. N차원 연산 : 연산하고자 할 때 배열의 shape이 같아야함. 물론 shape이 다르면 broadcasting으로 연산이 가능함")
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
        st.divider()
        
        st.subheader("11. dot : 두 백터를 곱하여 스칼라 산출")
        numpy_37, numpy_38, numpy_39 = st.columns(3)
        with numpy_37:
            arr_dot_1 = np.array([1,2,3])
            st.write("arr_dot_1")
            arr_dot_1
        with numpy_38:
            arr_dot_2 = np.array([4,5,6])
            st.write("arr_dot_2")
            arr_dot_2
        with numpy_39:
            st.write("np.dot(arr_dot_1, arr_dot_2)")
            dot_result = np.dot(arr_dot_1, arr_dot_2)
            dot_result
        st.divider()
        st.code('''
                [[a,b]           [[e,f]            [[ae+bg, af+bh]
                 [c.d]]           [g,h]]            [ce+cg, cf+ch]]
                ''')
        numpy_40, numpy_41, numpy_42 = st.columns(3)
        with numpy_40:
            arr_dot_3 = np.array([[1,2],[3,4]])
            st.write("arr_dot_3")
            arr_dot_3
        with numpy_41:
            arr_dot_4 = np.array([[5,6], [7,8]])
            st.write("arr_dot_4")
            arr_dot_4
        with numpy_42:
            st.write("np.dot(arr_dot_3,arr_dot_4)")
            dot_result_1 = np.dot(arr_dot_3,arr_dot_4)
            dot_result_1
        st.divider()
        
        st.subheader("12. 절대값, 올림, 내림, 반올림, 버림")
        numpy_43, numpy_44, numpy_45, numpy_46, numpy_47 =st.columns(5)
        with numpy_43:
            arr_juldae = np.array([[-1,-2],[-3,-4]])
            st.write("(1)절대갓")
            arr_juldae
            st.write("np.abs(arr_juldae)")        
            arr_juldae_result = np.abs(arr_juldae)
            arr_juldae_result
        with numpy_44:
            st.write("(2)올림")        
            arr_target = np.array([[1.932,-2.339],
                        [-4.145,5.206]])
            arr_target
            st.write("arr_target_ceil = np.ceil(arr_target)")
            #올림
            arr_target_ceil = np.ceil(arr_target)
            arr_target_ceil
        with numpy_45:
            st.write("(3)내림")  
            arr_target = np.array([[1.932,-2.339],
            [-4.145,5.206]])
            arr_target
            st.write("arr_target_floor = np.floor(arr_target)")
            #내림
            arr_target_floor = np.floor(arr_target)
            arr_target_floor
        with numpy_46:
            st.write("(4)반올림")  
            arr_target = np.array([[1.932,-2.339],
            [-4.145,5.206]])
            arr_target
            st.write("arr_target_round = np.round(arr_target)")
            #내림
            arr_target_round = np.round(arr_target)
            arr_target_round
        with numpy_47:
            st.write("(5)버림")  
            arr_target = np.array([[1.932,-2.339],
            [-4.145,5.206]])
            arr_target
            st.write("arr_target_trunc = np.trunc(arr_target)")
            #내림
            arr_target_trunc = np.trunc(arr_target)
            arr_target_trunc
        st.divider()
        
        st.subheader("13. 2차원 배열 최소값, 최대값, 평균값, 표준편차값, 누적값, 중앙값")
        arr_minmax = np.array([[9,8,7],[6,5,4],[3,2,1]])
        arr_minmax
        numpy_48, numpy_49, numpy_50 = st.columns(3)
        with numpy_48:
            st.write("np.min(arr_minmax)")
            min_arr_minmax = np.min(arr_minmax)
            min_arr_minmax
            st.write("np.min(arr_minmax,axis=0)")
            min_arr_minmax_0 = np.min(arr_minmax,axis=0)
            min_arr_minmax_0
            st.write("np.min(arr_minmax,axis=1)") 
            min_arr_minmax_1 = np.min(arr_minmax,axis=1)
            min_arr_minmax_1
        with numpy_49:
            st.write("np.max(arr_minmax)")
            min_arr_max = np.max(arr_minmax)
            min_arr_max
            st.write("np.max(arr_minmax,axis=0)")
            min_arr_max_0 = np.max(arr_minmax,axis=0)
            min_arr_max_0
            st.write("np.max(arr_minmax,axis=1)") 
            min_arr_max_1 = np.max(arr_minmax,axis=1)
            min_arr_max_1
        with numpy_50:
            st.write("np.mean(arr_minmax)")
            min_arr_mean = np.mean(arr_minmax)
            min_arr_mean
            st.write("np.mean(arr_minmax,axis=0)")
            min_arr_mean_0 = np.mean(arr_minmax,axis=0)
            min_arr_mean_0
            st.write("np.mean(arr_minmax,axis=1)") 
            min_arr_mean_1 = np.mean(arr_minmax,axis=1)
            min_arr_mean_1
        numpy_51, numpy_52, numpy_53 = st.columns(3)
        with numpy_51:
            st.write("np.std(arr_minmax)")
            min_arr_std = np.std(arr_minmax)
            min_arr_std
            st.write("np.std(arr_minmax,axis=0)")
            min_arr_std_0 = np.std(arr_minmax,axis=0)
            min_arr_std_0
            st.write("np.std(arr_minmax,axis=1)") 
            min_arr_std_1 = np.std(arr_minmax,axis=1)
            min_arr_std_1
        with numpy_52:
            st.write("np.cumsum(arr_minmax)")
            min_arr_cumsum = np.cumsum(arr_minmax)
            min_arr_cumsum
        with numpy_53:
            st.write("np.median(arr_minmax)")
            min_arr_median = np.median(arr_minmax)
            min_arr_median
            st.write("np.median(arr_minmax,axis=0)") 
            min_arr_median_0 = np.median(arr_minmax,axis=0)
            min_arr_median_0
            st.write("np.median(arr_minmax,axis=1)") 
            min_arr_median_1 = np.median(arr_minmax,axis=1)
            min_arr_median_1
        st.divider()
        
        st.subheader("14. 2차원 배열간 비교")
        numpy_54, numpy_55 = st.columns(2)
        with numpy_54:
            arr_compare_1 = np.array([[1,2,3,4],
                        [5,6,7,8]])
            st.write("arr_compare_1")
            arr_compare_1
            arr_compare_2 = np.array([[9,10,11,12],
                                    [13,14,15,16]])
            st.write("arr_compare_2")
            arr_compare_2
        with numpy_55:
            st.write("True면 체크, False면 공란")
            st.write("arr_compare_1 == arr_compare_2")
            arr_compare_1 == arr_compare_2
            st.write("np.equal(arr_compare_1, arr_compare_2)")
            equal = np.equal(arr_compare_1, arr_compare_2)
            equal
            st.write("arr_compare_1 >= arr_compare_2")
            arr_compare_1 >= arr_compare_2
            st.write("arr_compare_1 <= arr_compare_2")
            arr_compare_1 <= arr_compare_2
        st.divider()
        
        st.subheader("15. 삼각함수")
        st.write("np.array([[1,2,3], [4,5,6], [7,8,9]])")
        arr_triangle = np.array([[1,2,3],
                        [4,5,6],
                        [7,8,9]])
        arr_triangle
        numpy_56, numpy_57, numpy_58 = st.columns(3)
        with numpy_56:
            st.write("np.sin(arr_triangle)")
            sin_arr = np.sin(arr_triangle)
            sin_arr
        with numpy_57:
            st.write("np.cos(arr_triangle)")
            sin_cos = np.cos(arr_triangle)
            sin_cos
        with numpy_58:
            st.write("np.tan(arr_triangle)")
            tan_arr = np.tan(arr_triangle)
            tan_arr
        st.divider()
        
        st.subheader("16. Broadcasting : 배열간 shape이 달라도 연산 가능")
        numpy_59, numpy_60 = st.columns(2)
        with numpy_59:
            arr_broad_1 = np.array([[1,2,3],
                        [4,5,6],
                        [7,8,9]])
            arr_broad_2 = np.array([1,2,3])
            st.write("np.array([[1,2,3], [4,5,6], [7,8,9]])")
            arr_broad_1
            st.write("np.array([1,2,3])")
            arr_broad_2
            st.write("arr_broad_1 + arr_broad_2")
            broad12_result = arr_broad_1 + arr_broad_2
            broad12_result
        with numpy_60:
            arr_broad_3 = np.array([[1,1,1]])
            arr_broad_4 = np.array([[10], [10], [10]])
            st.write("np.array([[1,1,1]])")
            arr_broad_3
            st.write("np.array([[10], [10], [10]])")
            arr_broad_4
            st.write("arr_broad_3 + arr_broad_4")
            broad34_result = arr_broad_3 + arr_broad_4
            broad34_result
        st.divider()
        
        st.subheader("17. N차원 배열의 정렬")
        numpy_61, numpy_62, numpy_63 = st.columns(3)
        with numpy_61:
            arr_sort = np.random.randint(100,size=50)
            st.write("arr_sort = np.random.randint(100,size=50)")
            arr_sort
        with numpy_62:
            asc_arr_sort = np.sort(arr_sort)
            st.write("np.sort(arr_sort)")
            asc_arr_sort
        with numpy_63:
            desc_arr_sort = np.sort(arr_sort)[::-1]
            st.write("np.sort(arr_sort)[::-1]")
            desc_arr_sort
        numpy_64, numpy_65, numpy_66 = st.columns(3)
        with numpy_64:
            arr_sort_2 = np.random.randint(9, size=(3,3))
            st.write("arr_sort_2 = np.random.randint(9, size=(3,3))")
            arr_sort_2
        with numpy_65:
            arr_sort_2_0 = np.sort(arr_sort_2, axis=0)
            st.write("np.sort(arr_sort_2, axis=0)")
            arr_sort_2_0
        with numpy_66:
            arr_sort_2_1 = np.sort(arr_sort_2, axis=1)
            st.write("np.sort(arr_sort_2, axis=1)")
            arr_sort_2_1
        st.divider()
        
        st.subheader("18. argsort : 배열의 원래 인덱스를 반환")
        numpy_67, numpy_68 = st.columns(2)
        with numpy_67:
            argsort_arr = np.random.randint(9, size=(3,3))
            st.write("argsort_arr = np.random.randint(9, size=(3,3))")
            argsort_arr
        with numpy_68:
            argsort_arr_sort = np.sort(argsort_arr,axis=0)
            st.write("np.sort(argsort_arr,axis=0)")
            argsort_arr_sort
            
            argsort_arr_sort_origin = np.argsort(argsort_arr,axis=0)
            st.write("np.argsort(argsort_arr, axis=0)")
            argsort_arr_sort_origin
        st.divider()
        
        st.subheader("19. N차원 배열의 형태변경")
        st.write('''
                    reshape(): 원본 배열의 총 요소 수를 변경하지 않으며, 데이터가 보존됩니다. 새로운 배열은 원본 배열의 뷰로, 같은 데이터를 공유합니다.
                    resize(): 배열의 크기를 조정하며, 필요하면 데이터가 반복되거나 잘려나갑니다. 새로운 배열이 생성되며, 원본 배열과 데이터가 다를 수 있습니다.
                 ''')
        numpy_68, numpy_69, numpy_70 = st.columns(3)
        with numpy_68:
            arr_reshape_1 = np.arange(12)
            st.write("arr_reshape_1 = np.arange(12)")
            st.write(f"차원 : {arr_reshape_1.ndim}")
            arr_reshape_1
        with numpy_69:
            arr_reshape_2 = arr_reshape_1.reshape(6,2)
            st.write("arr_reshape_2 = arr_reshape_1.reshape(6,2)")
            st.write(f"차원 : {arr_reshape_2.ndim}")
            arr_reshape_2
        with numpy_70:
            arr_reshape_3 = arr_reshape_1.reshape((2,3,2))
            st.write("arr_reshape_3 = arr_reshape_1.reshape((2,3,2))")
            st.write(f"차원 : {arr_reshape_3.ndim}")
            
        numpy_71, numpy_72, numpy_73 = st.columns(3)
        with numpy_71:
            arr_resize_1 = np.arange(12)
            st.write("arr_resize_1 = np.arange(12)")
            arr_resize_1
        with numpy_72:
            arr_resize_1.resize(3,4)
            st.write("arr_resize_1.resize(3,4)")
            arr_resize_1
        with numpy_73:
            st.write("1차원으로 다시 변경 : arr_resize_1.ravel()")
            arr_resize_1_rabel = arr_resize_1.ravel()
            arr_resize_1_rabel
        st.divider()
        
        st.subheader("20. 차원추가")
        numpy_74, numpy_75, numpy_76 = st.columns(3)
        with numpy_74:
            arr_expand = np.array([1,2])
            st.write("arr_expand = np.array([1,2])")
            arr_expand
            st.write(f"차원 : {arr_expand.ndim}")
        with numpy_75:
            st.write("np.expand_dims(arr_expand, axis=1)")
            arr_expand_1 = np.expand_dims(arr_expand, axis=1)
            st.write(arr_expand_1)
            st.write(f"차원 : {arr_expand_1.ndim}")
        with numpy_76:
            st.write("np.expand_dims(arr_expand, axis=0)")
            arr_expand_0 = np.expand_dims(arr_expand, axis=0)
            st.write(arr_expand_0)
            st.write(f"차원 : {arr_expand_0.ndim}")
        st.divider()    
            
        st.subheader("21. 배열제거 후 차원축소")
        numpy_76, numpy_77, numpy_78 = st.columns(3)
        with numpy_76:
            st.code('''
                    arr_squeeze_1 = np.array([[1,2,3]])
                    np.squeeze(arr_squeeze_1,axis=0)
                    ''')
        with numpy_77:
            st.code('''
                    arr_squeeze_2 = np.array([[[1],
                                            [2],
                                            [3]]])
                    np.squeeze(arr_squeeze_2, axis=0)
                    ''')
        with numpy_78:
            st.code('''
                    arr_squeeze_3 = np.array([[[1,2,3]]])
                    np.squeeze(arr_squeeze_3, axis=1)                    
                    ''')
        st.divider()    
            
        st.subheader("22. 전치행렬")
        numpy_79, numpy_80 = st.columns(2)
        with numpy_79:
            arr_junchi_1 = np.array([[1,2,3],
                       [4,5,6],
                       [7,8,9]])
            st.write('arr_junchi_1 = np.array([[1,2,3], [4,5,6], [7,8,9]])')
            arr_junchi_1
        with numpy_80:
            arr_junchi_1_result = np.transpose(arr_junchi_1)
            st.write('np.transpose(arr_junchi_1)')
            arr_junchi_1_result
        
        numpy_81, numpy_82 = st.columns(2)
        with numpy_81:
            arr_junchi_2 = np.array([[1,2],
                       [3,4],
                       [5,6]])
            st.write('arr_junchi_2 = np.array([[1,2], [3,4], [5,6]])')
            arr_junchi_2
        with numpy_82:
            arr_junchi_2_result = np.transpose(arr_junchi_2)
            st.write('np.transpose(arr_junchi_2)')
            arr_junchi_2_result
        st.divider()    
        
        st.subheader("23. 배열 특정 위치에 값 추가")
        numpy_83, numpy_84 = st.columns(2) 
        with numpy_83:
            arr_add_value_1 = np.arange(1,9)
            st.write("arr_add_value_1 = np.arange(1,9)")
            arr_add_value_1
        with numpy_84:
            np.insert(arr_add_value_1,2,10)
            st.write("np.insert(arr_add_value_1,2,10)")
            arr_add_value_1_result = np.insert(arr_add_value_1,2,10)
            arr_add_value_1_result
        numpy_85, numpy_86 = st.columns(2) 
        with numpy_85:
            arr_add_value_2 = np.arange(1,13)
            st.write("arr_add_value_2 = np.arange(1,13)")
            arr_add_value_2
        with numpy_86:
            arr_add_value_2_0 = np.insert(arr_add_value_2,2,50,axis=0)
            st.write("np.insert(arr_add_value_2,2,50,axis=0)")
            arr_add_value_2_0
        st.divider()
        
        st.subheader("24. 배열병합")
        numy_87, numpy_88, numpy_89 = st.columns(3)
        with numy_87:
            arr_append_1 = np.arange(1,13).reshape(3,4)
            arr_append_2 = np.arange(13,25).reshape(3,4)
            st.write("arr_append_1 = np.arange(1,13).reshape(3,4)")
            arr_append_1
            st.write("arr_append_2 = np.arange(13,25).reshape(3,4)")
            arr_append_2
        with numpy_88:
            arr_append_120 = np.append(arr_append_1, arr_append_2, axis=0)
            st.write("arr_append_120 = np.append(arr_append_1, arr_append_2, axis=0)")
            arr_append_120
            st.write("arr_append_con_0 = np.concatenate([arr_append_1, arr_append_2], axis=0)")
            arr_append_con_0 = np.concatenate([arr_append_1, arr_append_2], axis=0)
            arr_append_con_0
        with numpy_89:
            arr_append_121 = np.append(arr_append_1, arr_append_2, axis=1)
            st.write("arr_append_121 = np.append(arr_append_1, arr_append_2, axis=1)")
            arr_append_121
            st.write("arr_append_con_1 = np.concatenate([arr_append_1, arr_append_2], axis=1)")
            arr_append_con_1 = np.concatenate([arr_append_1, arr_append_2], axis=1)
            arr_append_con_1
        st.divider()
        
        st.subheader("25. VSTACK, HSTACK")    
        numpy_90, numpy_91 = st.columns(2)
        with numpy_90:
            arr_vh_1 = np.arange(1,7).reshape(2,3)
            arr_vh_2 = np.arange(7,13).reshape(2,3)
            st.write("arr_vh_1 = np.arange(1,7).reshape(2,3)")
            arr_vh_1
            st.write("arr_vh_2 = np.arange(7,13).reshape(2,3)")
            arr_vh_2
        with numpy_91:
            arr_vh_v = np.vstack((arr_vh_1,arr_vh_2))
            arr_vh_h = np.hstack((arr_vh_1,arr_vh_2))
            st.write("arr_vh_v = np.vstack((arr_vh_1,arr_vh_2))")
            arr_vh_v
            st.write("arr_vh_h = np.hstack((arr_vh_1,arr_vh_2))")
            arr_vh_h
        st.divider()    
        
        st.subheader("26. VSPLIT, HSPLIT")
        numpy_92, numpy_93, numpy_94 = st.columns(3)
        with numpy_92:
            arr_vh_2 = np.arange(1,13).reshape(3,4)
            st.write("arr_vh_2 = np.arange(1,13).reshape(3,4)")
            arr_vh_2
        with numpy_93:
            arr_vh_2_v = np.vsplit(arr_vh_2,3)
            st.write("arr_vh_2_v = np.vsplit(arr_vh_2,3)")
            arr_vh_2_v
        with numpy_94:
            arr_vh_2_h = np.hsplit(arr_vh_2,2)
            st.write("arr_vh_2_h = np.hsplit(arr_vh_2,2)")
            arr_vh_2_h