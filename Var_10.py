import streamlit as st


def var10():
    st.title('Приложение "Титаник"')
    st.header("Вариант №10 \n Выполнил Кузнецов Н.В. гр. 3 см")
    st.subheader("Задание \n Посчитать долю выживших среди пассажиров указанного пола.")
    female_i = 0
    male_i = 0 
    i = 0
    i_female = 0
    i_male = 0
    res = float(0)
    sex = st.selectbox("Пол выживших пассажиров", ["Мужской", "Женский"])
    with open("data.csv") as file:
        for line in file:
            lst = line.rstrip().split(',')
            if lst[1] == "1" and lst[5] == "female":
                female_i += 1
                i_female += 1
            elif lst[1] == "0" and lst[5] == "female":
                i_female += 1
            if lst[1] == "1" and lst[5] == "male":
                male_i += 1
                i_male += 1
            elif lst[1] == "0" and lst[5] == "male":
                i_male += 1
    res = float(0)
    if sex == "Мужской":
        res = (male_i/i_male)*100
    if sex == "Женский":
        res = (female_i/i_female)*100
    st.text("Доля выживших указанного пола - " + str(round(res,2)) + " %")

