import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#헤더 
st.title("The skill Enhancement zone✍🏻")
st.divider()
skill_head_1, skill_head_2 = st.columns([0.7,0.3])
with skill_head_1:
    st.subheader("This page aims to enhance skills.", anchor=False, help=None)
    st.write("You can learn about Python as a programming language and study English. EL is looking to work with individuals who are committed to continuous growth in self-development and who have a strong passion for the tasks they are assigned. Just act without overthinking.")
    st.subheader("Don't stay stuck in the past or present.", anchor=False, help=None)
    st.write("While you revel in your past achievements or feel content with the present, someone else is continuously developing themselves to keep up with the rapidly changing world. We at EL are a collective and a company of leaders with diverse talents. We don’t just keep up with the pace of a changing world. we lead it.")
with skill_head_2:
    st.subheader("", anchor=False, help=None) 
    st.subheader("", anchor=False, help=None)
    st.subheader("", anchor=False, help=None)
    st.image("useData/EL_img/EL_STUDY_COUPLE.png")

st.divider()
#Python, English
study_zone_1, study_zone_2 = st. tabs(["Python","English"])
#Python zone
with study_zone_1:
    select_value_python = st.radio("Choice Python library what you want.",
            [":rainbow[***PANDAS***]",":rainbow[***NUMPY***]",":rainbow[***Pytorch***]"]
            )
    
# PANDAS section
    if select_value_python == ":rainbow[***PANDAS***]":
        st.subheader("About PANDAS")        
        st.write('''Pandas is a widely-used Python library for data manipulation and analysis. It's especially useful for handling tabular data, similar to Excel spreadsheets, and provides a data structure called DataFrame. With Pandas, you can easily read, write, filter, and manipulate data. It's a powerful tool for data analysis, preprocessing, statistical analysis, and more.''')
        st.write("(1)Data Reading/Writing: You can easily read from and write to various data formats such as CSV, Excel files, SQL databases, and more.")
        st.write("(2)Data Filtering and Selection: You can select or filter data based on specific conditions.")
        st.write("(3)Data Transformation: You can transform data, add or remove columns, handle missing values, and more.")
        st.write("(4)Grouping and Aggregation: You can group data and calculate aggregate statistics or summaries.")
        st.write("(5)Time Series Data Handling: Pandas has powerful features for working with date and time data.")
        st.write("(6)Install library")
        st.code('''
                pip install pandas
                ''')
        st.write("(7)Import library")
        st.code('''
                import pandas as pd
                ''')
        st.write("참고링크 : https://github.com/minsuk-heo/pandas/blob/master/Pandas_Cheatsheet.ipynb")
        st.divider()

        st.subheader("1. 데이터 불러오기 및 조회")
        pandas_col_1, pandas_col_2 = st.columns(2)
        with pandas_col_1:
            st.code('''
            friend_df = pd.read_csv("경로/friend_list.csv")
            st.dataframe(friend_df)
            ''')
            friend_df = pd.read_csv("useData/EL_data/pandas/friend_list.csv")
            st.dataframe(friend_df, use_container_width=True)
        with pandas_col_2:
            st.code('''
            head_friend_df = friend_df.head()
            tail_friend_df = friend_df.tail()
            ''')
            head_friend_df = friend_df.head()
            tail_friend_df = friend_df.tail()
            st.write("(1) 상위 5개행 조회", anchor=False, help=None)
            st.dataframe(head_friend_df, use_container_width=True)
            st.write("(2) 하위 5개행 조회")
            st.dataframe(tail_friend_df, use_container_width=True)
        st.divider()

        st.subheader("2. 데이터프레임과 시리즈", anchor=False, help=None)
        st.write("데이터 프레임은 2개 이상의 시리즈로 구성돼어 있는 형태임. Series는 1차원 배열과 같은 객체로, 정수, 문자열, 실수 등 어떤 데이터 유형도 담을 수 있음. DataFrame은 2차원 테이블 형태의 데이터 구조로, 여러 개의 Series로 구성되며 DataFrame의 각 열이 Series임.")
        pandas_col_3, pandas_col_4 = st.columns(2)
        with pandas_col_3:
            st.code('''
            friend_df = pd.read_csv("경로/friend_list.csv")
            st.dataframe(friend_df)
            ''')
            friend_df = pd.read_csv("useData/EL_data/pandas/friend_list.csv")
            st.dataframe(friend_df, use_container_width=True)
        with pandas_col_4:
            st.write("(1)name 열 타입")
            st.code("type(friend_df['name'])")
            st.write(f"{type(friend_df['name'])}")
            st.write("(2)age 열 타입")
            st.code("type(friend_df['age'])")
            st.write(f"{type(friend_df['age'])}")
            st.write("(3)friend_df 타입")
            st.code("type(friend_df)")
            st.write(f"{type(friend_df)}")
        st.divider()

        st.subheader("3. 데이터프레임과 시리즈 만들기", anchor=False, help=None)
        pandas_col_5, pandas_col_6 = st.columns(2)
        with pandas_col_5:
            st.write("(1) 데이터프레임 생성")
            st.code('''
                a_df = pd.DataFrame({
                "컬럼1":["a",'b',"c"],
                "컬럼2":[1,2,3]
            })
                    ''')
            a_df = pd.DataFrame({
                "컬럼1":["a",'b',"c"],
                "컬럼2":[1,2,3]
            })
            st.dataframe(a_df, use_container_width=True)
            st.write("(2) 딕셔너리로 데이터프레임 생성")
            st.code('''
                    friend_dict_list = [
                                {"name":"john","age":25, "job":"sturdent"},
                                {"name":"nate","age":305, "job":"teacher"}
                                ]
                    new_f_dict = pd.DataFrame(friend_dict_list)
                    ''')
            friend_dict_list = [
                                {"name":"john","age":25, "job":"sturdent"},
                                {"name":"nate","age":305, "job":"teacher"}
                                ]
            new_f_dict = pd.DataFrame(friend_dict_list)
            st.dataframe(new_f_dict, use_container_width=True)
        with pandas_col_6:
            st.write("(3) 시리즈 생성")
            st.code('''
                    a1 = ["a","b","c"]
                    col1 = pd.Series(a1)
                    b1 = ["d","e","f"]
                    col2 = pd.Series(b1)
                    ''')
            a1 = ["a","b","c"]
            col1 = pd.Series(a1)
            b1 = ["d","e","f"]
            col2 = pd.Series(b1)
            st.write(f"{type(col1)}")
            st.write(col1)
            st.write(f"{type(col2)}")
            st.write(col2)
        st.divider()

        st.subheader("4. 컬럼명(헤더) 없는 데이터프레임 불러오기 및 컬럼 지정", anchor=False, help=None)
        st.write("컬럼이 지정되지 않은 CSV 파일을 열면 행이 밀려 컬럼명으로 들어감. 이를 방지하기 위해 아래와 같이 진행.")
        pandas_col_7, pandas_col_8 = st.columns(2)
        with pandas_col_7:
            nohead_df = pd.read_csv("useData/EL_data/pandas/friend_list_no_head.csv", header=None)
            st.write("(1) 데이터 불러오기")
            st.code('''
                   st.dataframe(nohead_df, use_container_width=True)
                    ''')
            st.dataframe(nohead_df, use_container_width=True)
            st.write("(2) 컬럼명 지정")
            st.code('''
                    nohead_df.columns = ["name", "age", "job"]  
                    ''')
            nohead_df.columns = ["name", "age", "job"]
            st.dataframe(nohead_df, use_container_width=True)
        with pandas_col_8:
            st.write("(1) 데이터 불러올때 직접 지정하기")
            st.code('''
                    direct_nohead = pd.read_csv("경로/friend_list_no_head.csv", header=None, names=["name","age","job"])
                   ''')
            direct_nohead = pd.read_csv("useData/EL_data/pandas/friend_list_no_head.csv", header=None, names=["name","age","job"])
            st.dataframe(direct_nohead, use_container_width=True)
        st.divider()
        
        st.subheader("5. Index를 활용하여 행 선택", anchor=False, help=None)
        pandas_col_9, pandas_col_10 = st.columns(2)
        with pandas_col_9:
            st.write("(1) 데이터 불러오기")
            friend_raw_data = pd.read_csv("useData/EL_data/pandas/friend_list.csv")
            st.dataframe(friend_raw_data, use_container_width=True)
        with pandas_col_10:
            st.write("(2) 인덱스 활용해서 특정 행 조회")
            st.code('''
                    friend_raw_data.loc[3]
                    ''')
            st.dataframe(friend_raw_data.loc[3],use_container_width=True)
            st.write("(3) 인덱스 활용해서 특정범위 행 조회(loc, iloc 활용하여 특정 위치의 데이터 추출가능)")
            st.code('''friend_raw_data[1:3]''')
            st.dataframe(friend_raw_data[1:3],use_container_width=True)
            st.code('''friend_raw_data.loc[[0,2]]''')
            st.dataframe(friend_raw_data.loc[[0,2]],use_container_width=True)
        st.divider()

        st.subheader("6. 필드(컬럼) 조건을 활용한 데이터 조회", anchor=False, help=None)
        pandas_col_11, pandas_col_12 = st.columns(2)
        with pandas_col_11:
            st.write("(1) 데이터 불러오기")
            friend_raw_data = pd.read_csv("useData/EL_data/pandas/friend_list.csv")
            st.dataframe(friend_raw_data, use_container_width=True)
        with pandas_col_12:
            st.write("(2) age 가 25 이상인 데이터")
            st.code('''
                    friend_raw_data[friend_raw_data['age']>=25]
                    ''')
            st.dataframe(friend_raw_data[friend_raw_data['age']>=25])
            st.write("(3) age 가 25 보다 위이고 name이 Nate인 데이터")
            st.code('''
                    friend_raw_data[(friend_raw_data["age"]>25) & (friend_raw_data["name"]=="Nate")]
                    ''')
            st.dataframe(friend_raw_data[(friend_raw_data["age"]>25) & (friend_raw_data["name"]=="Nate")])
        st.divider()

        st.subheader("7. iloc를 활용한 데이터 조회", anchor=False, help=None)
        pandas_col_13, pandas_col_14 = st.columns(2)
        with pandas_col_13:
            st.write("(1) 데이터 불러오기")
            friend_raw_data = pd.read_csv("useData/EL_data/pandas/friend_list.csv")
            st.dataframe(friend_raw_data, use_container_width=True)
        with pandas_col_14:
            st.write("**iloc는 loc와 다르게 행/열의 인덱스를 활용하여 데이터를 조회하는 방식임.")
            st.write("(2) 전체 행과 첫번째 열, 세번째 열")
            st.code('''
                    friend_raw_data.iloc[:,[0,2]]
                    ''')
            st.dataframe(friend_raw_data.iloc[:,[0,2]])
            st.write("(3) 첫번째 - 세번째 행과 세번째 열")
            st.code('''
                    friend_raw_data.iloc[0:2,2]
                    ''')
            st.dataframe(friend_raw_data.iloc[0:2,2])
            st.write("(3) 세번째 행과 세번째 열")
            st.code('''
                    friend_raw_data.iloc[2, 2]
                    ''')
            st.text(friend_raw_data.iloc[2, 2])
        st.divider()

        st.subheader("8. filter를 활용한 데이터 조회", anchor=False, help=None)
        pandas_col_15, pandas_col_16 = st.columns(2)
        with pandas_col_15:
            st.write("(1) 데이터 불러오기")
            friend_raw_data = pd.read_csv("useData/EL_data/pandas/friend_list.csv")
            st.dataframe(friend_raw_data, use_container_width=True)
        with pandas_col_16:
            st.write("(2) name과 age 필드 불러오기")
            st.code('''
                    #filter 사용
                    friend_raw_data.filter(items=["name","age"])
                    ''')
            st.dataframe(friend_raw_data.filter(items=["name","age"]))
            st.code('''
                    #filter 외 다른 방법
                    friend_raw_data[["name","age"]]
                    ''')
            st.dataframe(friend_raw_data[["name","age"]])
            
            st.write("(3) 필드명이 a가 포함됀 열")
            st.code('''
                    friend_raw_data.filter(like="a", axis=1)
                    ''')
            st.dataframe(friend_raw_data.filter(like="a", axis=1))

            st.write("(4) 필드명이 b가 포함됀 열을 정규표현으로 추출")
            st.code('''
                    friend_raw_data.filter(regex='b$',axis=1)
                    ''')
            st.dataframe(friend_raw_data.filter(regex='b$',axis=1))
        st.divider()

        st.subheader("9. drop row", anchor=False, help=None)
        pandas_col_17, pandas_col_18 = st.columns(2)
        with pandas_col_17:
            st.write("(1) 데이터 불러오기 **name 필드를 인덱스로 지정하여 부름")
            friend_raw_data = pd.read_csv("useData/EL_data/pandas/friend_list.csv", index_col="name")
            st.dataframe(friend_raw_data, use_container_width=True)
        with pandas_col_18:
            st.write("(2) John, Jenny, Julia 행 제거")
            st.code('''
                    friend_raw_data.drop(["John", "Jenny", "Julia"])
                    ''')
            st.dataframe(friend_raw_data.drop(["John", "Jenny", "Julia"]), use_container_width=True)
            st.write("(3) drop + inplace : inplace=True 는 현재 데이터에 바로 적용함을 의미")
            st.code('''
                    friend_raw_data.drop(['Brian'], inplace = True)
                    friend_raw_data
                    ''')
            friend_raw_data.drop(['Brian'], inplace = True)
            st.dataframe(friend_raw_data, use_container_width=True)
        st.divider()

        st.subheader("10. drop/add/update column", anchor=False, help=None)
        pandas_col_19, pandas_col_20 = st.columns(2)
        with pandas_col_19:
            st.write("(1) 데이터 불러오기")
            friend_raw_data = pd.read_csv("useData/EL_data/pandas/friend_list.csv")
            st.dataframe(friend_raw_data, use_container_width=True)
        with pandas_col_20:
            st.write("(2) age 컬럼 drop")
            friend_raw_data = friend_raw_data.drop('age', axis=1)
            st.code('''friend_raw_data.drop('age', axis=1)''')
            st.dataframe(friend_raw_data,use_container_width=True)
            st.write("(3) salary 컬럼 생성")
            st.code('''
                    friend_raw_data["salary"] = None
                    ''')
            friend_raw_data["salary"] = None
            st.dataframe(friend_raw_data,use_container_width=True)
            st.write("(4) salary 컬럼 값 수정")
            st.code('''
                    friend_raw_data["salary"] = 10000        
                    ''')
            friend_raw_data["salary"] = 10000
            st.dataframe(friend_raw_data)
            st.write("(5) numpy를 활용하여 업데이트 : np.where()")
            st.code('''
                    friend_raw_data["salary"] = np.where(friend_raw_data["job"] == 'developer', 1000000, 500 )
                    ''')
            st.dataframe(friend_raw_data)
        st.divider()

        st.subheader("11. 컬럼간 연산", anchor=False, help=None)
        pandas_col_21, pandas_col_22 = st.columns(2)
        with pandas_col_21:
            st.write("(1) 데이터프레임")
            new_df = pd.DataFrame({
                "name": ["a","b","c","d","e"],
                "mid_score" : [20,30,40,50,60],
                "final_score": [50,60,70,80,90]
            })
            st.dataframe(new_df,use_container_width=True)
        with pandas_col_22:
            st.write("(2) 신규컬럼 생성")
            st.code('''
                    new_df["total"] = new_df["mid_score"]+new_df["final_score"]
                    new_df["avg_score"] = new_df["total"] / 2
                    ''')
            new_df["total"] = new_df["mid_score"]+new_df["final_score"]
            new_df["avg_score"] = new_df["total"] / 2
            st.dataframe(new_df, use_container_width=True)
        st.divider()

        st.subheader("12. apply 함수", anchor=False, help=None)
        pandas_col_23, pandas_col_24 = st.columns(2)
        with pandas_col_23:
            st.write("(1) 데이터프레임")
            date_df = pd.DataFrame({
                "YYYY-MM-DD" : ["2001-01-01", "2002-02-02", "2003-03-03", "2004-04-04", "2005-05-05"]
            })
            st.dataframe(date_df, use_container_width=True)
            st.write("(2) 함수정의")
            st.code('''
                    #년도 뽑기
                    def extract_year(row):
                    return row.split('-')[0]                    
                    #나이 구하기
                    def get_old(row, current_year):
                    return int(row) - current_year
                    ''')
            def extract_year(row):
                return row.split('-')[0]
            
            def get_old(row, current_year):
                return int(row) - current_year

        with pandas_col_24:
            st.write("(3) apply함수를 활용하여 데이터 신규 필드 생성")
            st.code('''
                    date_df[신규컬럼명] = date_df["YYYY-MM-DD"].apply(함수명)
                    ''')
            date_df["YYYY"] = date_df["YYYY-MM-DD"].apply(extract_year)
            st.dataframe(date_df, use_container_width=True)
            st.code('''
                    date_df["YYYY"].apply(get_old, current_year=2000)
                    ''')
            date_df["age"] = date_df["YYYY"].apply(get_old, current_year=2000)
            st.dataframe(date_df, use_container_width=True)
        st.divider()

        st.subheader("13. Map 함수-1", anchor=False, help=None)
        pandas_col_25, pandas_col_26 = st.columns(2)
        with pandas_col_25:
            st.write("(1) 데이터프레임")
            date_df = pd.DataFrame({
                "YYYY-MM-DD" : ["2001-01-01", "2002-02-02", "2003-03-03", "2004-04-04", "2005-05-05"]
            })
            st.dataframe(date_df, use_container_width=True)
            st.write("(2) 함수정의")
            st.code('''
                    #년도 뽑기
                    def extract_year(row):
                    return row.split('-')[0]                    
                    #나이 구하기
                    def get_old(row, current_year):
                    return int(row) - current_year
                    ''')
            def extract_year(row):
                return row.split('-')[0]
            def get_old(row, current_year):
                return int(row) - current_year
            
        with pandas_col_26:
            st.write("(3) map + 함수")
            st.code('''
                    date_df['year'] = date_df['YYYY-MM-DD'].map(extract_year)
                    ''')
            date_df['year'] = date_df['YYYY-MM-DD'].map(extract_year)
            st.dataframe(date_df,use_container_width=True)
            st.code('''
                    ate_df["age"] = date_df['year'].map(lambda x: get_old(x, current_year=1990))
                    ''')
            date_df["age"] = date_df['year'].map(lambda x: get_old(x, current_year=1990))
            st.dataframe(date_df,use_container_width=True)
        st.divider()

        st.subheader("14. Map 함수-2", anchor=False, help=None)
        pandas_col_27, pandas_col_28 = st.columns(2)
        with pandas_col_27:
            st.write("(1) 데이터프레임")
            job_list = [{'age': 20, 'job': 'student'},
                    {'age': 30, 'job': 'developer'},
                    {'age': 30, 'job': 'teacher'}]
            job_df = pd.DataFrame(job_list)
            st.dataframe(job_df, use_container_width=True)
        with pandas_col_28:
            st.write("(2) map 함수 활용")
            st.code('''
                    job_df["job_code"] = job_df.job.map({"student":1,"developer":2,"teacher":3})
                    st.dataframe(job_df, use_container_width=True)
                    ''')
            job_df["job_code"] = job_df.job.map({"student":1,"developer":2,"teacher":3})
            st.dataframe(job_df, use_container_width=True)
        st.divider()

        st.subheader("15. Applymap", anchor=False, help=None)
        pandas_col_29, pandas_col_30 = st.columns(2)
        with pandas_col_29:
            st.write("(1) 데이터프레임 생성")
            x_y = [{'x': 5.5, 'y': -5.6},
                    {'x': -5.2, 'y': 5.5},
                    {'x': -1.6, 'y': -4.5}]
            applymap_df = pd.DataFrame(x_y)
            st.dataframe(applymap_df,use_container_width=True)
        with pandas_col_30:
            st.write("(2) applymap 적용")
            st.code('''
                    applymap_df = applymap_df.applymap(np.around)
                    ''')
            applymap_df = applymap_df.applymap(np.around)
            st.dataframe(applymap_df, use_container_width=True)
        st.divider()

        st.subheader("16. Group by", anchor=False, help=None)
        pandas_col_31, pandas_col_32 = st.columns(2)
        with pandas_col_31:
            st.write("(1) 데이터프레임 생성")
            student_list = [{'name': 'John', 'major': "Computer Science", 'sex': "male"},
                            {'name': 'Nate', 'major': "Computer Science", 'sex': "male"},
                            {'name': 'Abraham', 'major': "Physics", 'sex': "male"},
                            {'name': 'Brian', 'major': "Psychology", 'sex': "male"},
                            {'name': 'Janny', 'major': "Economics", 'sex': "female"},
                            {'name': 'Yuna', 'major': "Economics", 'sex': "female"},
                            {'name': 'Jeniffer', 'major': "Computer Science", 'sex': "female"},
                            {'name': 'Edward', 'major': "Computer Science", 'sex': "male"},
                            {'name': 'Zara', 'major': "Psychology", 'sex': "female"},
                            {'name': 'Wendy', 'major': "Economics", 'sex': "female"},
                            {'name': 'Sera', 'major': "Psychology", 'sex': "female"}
                    ]
            student_df = pd.DataFrame(student_list, columns = ['name', 'major', 'sex'])
            st.dataframe(student_df, use_container_width=True)            
        with pandas_col_32:
            st.write("(2) major 그룹바이")
            st.code('''
                    groupby_major = student_df.groupby('major')
                    groupby_major.groups
                    ''')
            groupby_major = student_df.groupby('major')
            groupby_major.groups
            st.code('''
                    groupby_major.count()
                    ''')
            st.dataframe(groupby_major.count(), use_container_width=True)
        st.divider()

        st.subheader("17. Null, NaN 처리", anchor=False, help=None)
        pandas_col_33, pandas_col_34 = st.columns(2)
        with pandas_col_33:
            st.write("(1) 데이터프레임 생성")
            school_id_list = [{'name': 'John', 'job': "teacher", 'age': 40},
                            {'name': 'Nate', 'job': "teacher", 'age': None},
                            {'name': 'Yuna', 'job': None, 'age': 37},
                            {'name': 'Abraham', 'job': "student", 'age': None},
                            {'name': 'Brian', 'job': "student", 'age': 12},
                            {'name': 'Janny', 'job': None, 'age': 11},
                            {'name': 'Nate', 'job': "teacher", 'age': None},
                            {'name': 'John', 'job': "student", 'age': None}
                    ]
            school_df = pd.DataFrame(school_id_list, columns = ['name', 'job', 'age'])
            st.dataframe(school_df, use_container_width=True)     
        with pandas_col_34:
            st.write("(2) isna() : null 또는 None은 True 반환")
            st.code('''
                    school_df.isna()
                    ''')
            st.dataframe(school_df.isna(), use_container_width=True)
            st.write("(3) isnull() : null 또는 None은 True 반환")
            st.code('''
                    school_df.isnull()
                    ''')
            st.dataframe(school_df.isnull(), use_container_width=True)
            st.write("(4) 특정열의 Null 또는 None 값 채우기")
            st.code('''
                    school_df["age"] = school_df["age"].fillna(0)
                    school_df["job"] = school_df["job"].fillna("student")
                    ''')
            school_df["age"] = school_df["age"].fillna(0)
            school_df["job"] = school_df["job"].fillna("student")
            st.dataframe(school_df, use_container_width=True)
        st.divider()

        st.subheader("18. concat", anchor=False, help=None)
        pandas_col_35, pandas_col_36 = st.columns(2)
        with pandas_col_35:
            st.write("(1) 데이터프레임")
            l1 = [{'name': 'John', 'job': "teacher"},
                {'name': 'Nate', 'job': "student"},
                {'name': 'Jack', 'job': "developer"}]
            l2 = [{'age': 25, 'country': "U.S"},
                {'age': 30, 'country': "U.K"},
                {'age': 45, 'country': "Korea"}]
            st.write("**데이터프레임 l1")
            l1 = pd.DataFrame(l1)
            l2 = pd.DataFrame(l2)
            st.dataframe(l1, use_container_width=True)
            st.write("**데이터프레임 l2")
            st.dataframe(l2, use_container_width=True)

        with pandas_col_36:
            st.write("(2) 병합 : axis=1 은 열 방향, axis=0 은 행 방향")
            st.code('''
                    result_1 = pd.concat([l1, l2], axis=1, ignore_index=True)
                    result_2 = pd.concat([l1, l2], axis=0, ignore_index=True)                    
                    ''')
            result_1 = pd.concat([l1, l2], axis=1, ignore_index=True)
            st.dataframe(result_1)
            result_2 = pd.concat([l1, l2], axis=0, ignore_index=True)
            st.dataframe(result_2)

# Numpy Section
    elif select_value_python == ":rainbow[***NUMPY***]":
        st.subheader("About NUMPY")
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

#Pytorch section
    elif select_value_python == ":rainbow[***Pytorch***]":
        st.subheader("About Pytorch")
        st.write("PyTorch는 주로 딥러닝 연구 및 개발을 위해 사용되는 오픈 소스 딥러닝 프레임워크임. PyTorch는 Facebook AI Research (FAIR)에서 개발되었으며, Python과 C++로 작성되어 있음. PyTorch는 특히 다음과 같은 이유로 인기를 얻음.")
        pytorch_feature = '''
        동적 계산 그래프 (Dynamic Computation Graph):
        PyTorch는 동적 계산 그래프를 사용합니다. 이는 계산 그래프가 실행 중에 정의되고 변경될 수 있음을 의미합니다. 이 방식은 코드 디버깅을 용이하게 하고, 복잡한 모델을 쉽게 작성할 수 있게 해줌.
        TensorFlow와 같은 일부 다른 프레임워크는 정적 계산 그래프를 사용하여, 그래프를 미리 정의하고 실행함. PyTorch의 동적 그래프는 더욱 유연한 모델 작성 및 실험에 적합함.

        Pythonic:
        PyTorch는 Python과 깊이 통합되어 있어 Python 사용자에게 친숙함. Pythonic한 인터페이스 덕분에 사용자가 익숙한 Python 코드 스타일로 모델을 작성할 수 있음.
        또한, NumPy와 유사한 문법과 연산을 제공하여, Tensor 연산을 매우 직관적으로 수행할 수 있음.

        자동 미분 (Autograd):
        PyTorch는 자동 미분 기능을 제공함. 이는 모델의 역전파 과정에서 그래디언트를 자동으로 계산해주는 기능임. 덕분에 사용자들은 직접 복잡한 미분 연산을 구현할 필요 없이 모델의 학습을 진행할 수 있음.

        광범위한 지원:
        PyTorch는 다양한 신경망 레이어, 손실 함수, 최적화 알고리즘, 데이터 로더, 변환 등 딥러닝 개발에 필요한 도구들을 제공함.
        또한, GPU 가속을 지원하여 대규모 연산을 효율적으로 수행할 수 있음.

        커뮤니티와 생태계:
        PyTorch는 활발한 개발자 커뮤니티와 강력한 생태계를 가지고 있음. 다양한 튜토리얼, 오픈 소스 프로젝트, 연구 논문 등이 PyTorch를 기반으로 제공되며, 빠르게 발전하고 있음.
        PyTorch 생태계에는 PyTorch Lightning, TorchServe, Hugging Face Transformers와 같은 다양한 확장 라이브러리도 포함되어 있어, 모델 개발, 배포 등을 쉽게 할 수 있음.

        활용 분야
        PyTorch는 주로 딥러닝 모델의 연구, 프로토타이핑, 그리고 실제 서비스 배포에 사용됨. 특히 다음과 같은 분야에서 널리 사용됨.

        컴퓨터 비전: 이미지 분류, 객체 탐지, 세그멘테이션 등
        자연어 처리 (NLP): 텍스트 분류, 언어 모델링, 번역, 감정 분석 등
        강화 학습: 에이전트 학습 및 시뮬레이션 환경에서의 활용
        생성 모델: GANs, VAE 등 생성적 모델 연구 및 개발
        결론적으로, PyTorch는 유연성과 사용 편의성 덕분에 연구자와 개발자 사이에서 널리 사용되는 딥러닝 프레임워크로 자리잡고 있음.
        '''
        pytorch_intro_1 = st.container(border=True)
        with pytorch_intro_1:
            st.write(pytorch_feature)
        st.divider()
        st.subheader("Pytorch and Tensorflow")
        pytorch_intro_2 = st.container(border=True)
        with pytorch_intro_2:
            st.write("PyTorch와 TensorFlow는 딥러닝에서 널리 사용되는 두 주요 프레임워크임. TensorFlow는 Google에서 개발했으며, 정적 계산 그래프를 사용하다가 이후 동적 계산 그래프(Eager Execution)를 도입했습니다. 대규모 배포와 확장에 강점을 가지며, TensorFlow Serving, TensorFlow Lite 등의 다양한 배포 옵션을 제공함. PyTorch는 Facebook에서 개발했으며, 처음부터 동적 계산 그래프를 채택하여 Python 사용자에게 친숙한 인터페이스를 제공합니다. 연구 및 프로토타이핑에 강점이 있으며, 최근에는 산업 배포 도구(TorchServe 등)도 발전함. 두 프레임워크는 각자의 장점이 있으며, 상호 경쟁하면서도 발전을 이뤄가고 있는 중 임.")
        st.divider()
        st.subheader("Pytorch and Tensor")
        pytorch_intro_3 = st.container(border=True)
        with pytorch_intro_3:
            st.write('''PyTorch와 Tensor는 밀접한 관계가 있음. PyTorch는 텐서 연산을 중심으로 하는 딥러닝 프레임워크이며, 텐서(Tensor)는 PyTorch의 기본 데이터 구조임. 이를 좀 더 구체적으로 설명하면 다음과 같음.\n
                    1. Tensor의 정의 : Tensor는 다차원 배열(n-dimensional array) 또는 일반화된 행렬로, 숫자 데이터를 담는 컨테이너임. 텐서는 1차원 배열(벡터)부터 2차원 배열(행렬), 더 나아가 고차원의 배열까지 다양한 형태를 가짐. 텐서는 NumPy의 ndarray와 유사한 개념이지만, GPU 가속 연산을 지원하며, 자동 미분 기능이 포함된다는 점에서 차이가 있음.\n
    2. PyTorch에서의 Tensor : PyTorch에서 Tensor는 모든 데이터 및 모델의 기본 구조로 사용됨. 모델의 입력 데이터, 가중치, 손실 함수 등 모든 것이 텐서로 표현됨. PyTorch의 텐서는 CPU뿐만 아니라 GPU에서도 연산을 수행할 수 있음. 이를 통해 대규모 데이터와 복잡한 연산을 효율적으로 처리할 수 있음.\n
    3. Tensor의 기능 : PyTorch의 Tensor는 다양한 수학적 연산을 지원함. 예를 들어, 행렬 곱셈, 요소별 연산, 트랜스포즈, 역행렬 계산 등을 할 수 있음. 자동 미분(Autograd)과 같이 PyTorch의 텐서는 자동 미분 기능을 통해 역전파(Backpropagation) 중 그래디언트를 자동으로 계산할 수 있음. 이는 딥러닝 모델의 학습에 매우 유용함. 텐서는 GPU에서의 병렬 연산을 통해 연산 속도를 크게 높일 수 있음.\n
    4. Tensor와 PyTorch의 관계 요약 : PyTorch는 Tensor를 기반으로 한 연산을 제공하는 딥러닝 프레임워크임. Tensor는 PyTorch에서 모든 데이터 구조의 기본이 되며, PyTorch의 강력한 기능(예: 자동 미분, GPU 연산)을 통해 딥러닝 모델 개발을 지원함. PyTorch의 사용자는 Tensor를 통해 데이터를 관리하고 연산하며, 이 과정을 통해 모델을 구축하고 학습시킬 수 있음.''')
    st.divider()