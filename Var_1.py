import streamlit as st


def var1():
    st.title("Титаник")
    st.header('Вариант 1. Выполнила Александрова Е.В., группа 3-см')
    st.subheader('Задание: Вывести имя и возраст спасенных детей, указав пол и возраст (от 0 до 18)')
    sex_select = st.selectbox("sex", ('male', 'female'))
    age_select = st.slider("age", 0, 18, [1, 10])
    age_min = age_select[0]
    age_max = age_select[1]

    titanic = {}
    with open("data.csv") as data_file:
        next(data_file)
        for line in data_file:
            lst = line.strip().split(',')

            name = lst[3] + lst[4]
            sex = lst[5]
            age = lst[6]

            if age and (float(age) >= float(age_min)) and (float(age) <= float(age_max)) and sex == sex_select:
                passenger_info = {"sex": sex, "age": age}
                titanic[name[1: -1]] = passenger_info
    #sex == "male" and age and
    st.table(titanic)