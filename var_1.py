import streamlit as st


def get_result(data, sex_need, age_min, age_max):
    titanic = {}
    for line in data:
        lst = line.strip().split(',')
        name = lst[3] + " " + lst[4]
        sex = lst[5]
        age = lst[6]
        if age == 'SibSp':
            continue
        if age and (float(age) >= float(age_min)) and (float(age) <= float(age_max)) and sex == sex_need:
            passenger_info = {"sex": sex, "age": age}
            titanic[name] = passenger_info
    return titanic


def var1(data):
    st.header('Вариант 1. Выполнила Александрова Е.В., группа 3-см')
    st.subheader("Задание:")
    st.info('Вывести имя и возраст спасенных детей, указав пол и возраст (от 0 до 18)')
    st.subheader("Результат:")
    sex_select = st.selectbox("Выберите пол пассажира", ('male', 'female'))
    age_select = st.slider("Укажите возрастной диапазон пассажиров", 0, 18, [1, 10])
    min_age = age_select[0]
    max_age = age_select[1]
    result = get_result(data, sex_select, min_age, max_age)
    st.table(result)
