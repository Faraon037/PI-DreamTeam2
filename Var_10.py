import streamlit as st


def var10():
    def sex_deadh (data, sex):
        pas_i = 0
        i_all = 0
        res = float(0)
        for line in data:
            lst = line.rstrip().split(',')
            if lst[1] == "1" and lst[5] == sex:
                pas_i += 1
                i_all += 1
            elif lst[1] == "0" and lst[5] == sex:
                i_all += 1
#        res = round((pas_i / i_all) * 100, 2)
        return round((pas_i / i_all) * 100, 2)

    st.title('Приложение "Титаник"')
    st.header("Вариант №10 \n Выполнил Кузнецов Н.В. гр. 3 см")
    st.subheader("Задание \n Посчитать долю выживших среди пассажиров указанного пола.")
    with open("data.csv") as file:
        data = file.readlines()
        sex_in = st.selectbox("Пол выживших пассажиров", ["Мужской", "Женский"])
    if sex_in == "Мужской":
        sex = "male"
    if sex_in == "Женский":
        sex = "female"
    print(sex_deadh(data, sex))
