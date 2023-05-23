import streamlit as st


def var10():
    st.title('Приложение "Титаник"')
    st.header("Вариант №10 \n Выполнил Кузнецов Н.В. гр. 3 см")
    st.subheader("Задание \n Посчитать долю выживших среди пассажиров указанного пола.")
    female_i = 0
    male_i = 0 
    i = 0
    res = float(0)
    sex = st.selectbox("Пол выжеыших пассажиров", ["Мужской", "Женский"])
    with open("data.csv") as file:
        for line in file:
            lst = line.rstrip().split(',')
            if lst[1] == "1" or lst[1] == "0":
                i += 1
            if lst[1] == "1" and lst[5] == "female":
                female_i += 1
            if lst[1] == "1" and lst[5] == "male":
                male_i += 1
    res = float(0)
    if sex == "Мужской":
        res = (male_i/i)*100
    if sex == "Женский":
        res = (female_i/i)*100
    st.text("Доля выживших указанного пола - " + str(round(res,2)) + " %")

