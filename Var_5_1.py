import streamlit as st


def var5_1():
    st.header('Вариант 5. Выполнил Кузнецов Н.В., группа 3-см')
    st.subheader("Задание:")
    st.info("Вывести Класс, Имя, Возраст спасенных с именами, начинающимися на введенный текст")
    st.subheader("Результат:")
    i = 0
    tecst = st.text_input("Введите первые буквы имени спасенного пассажира")
    ln_tecst = len(tecst)
    with open("data.csv") as file:
        for line in file:
            lst = line.rstrip().split(',')
            fio = lst[3] + lst[4]
            fio1 = fio[1:ln_tecst + 1]
            if lst[5] == "female":
                pol = "ЖЕН"
            else:
                pol = "МУЖ"
            if ln_tecst > 0 and fio1 == tecst.capitalize() and lst[1] == "1":
                i += 1
                x = ", ".join([pol,"Возраст" + ' - ' + lst[6]])
                clas = lst[2]
                n = lst[3] + lst[4]
                res = (clas + "-" + "Класс" + ", " + n[1:-1] + ", " + x)
                st.text(res)
        if i == 0:
            st.text("Нет спасенных пассажиров с именами, отвечающими условиям поиска")
    st.text("Найдено = " + str(i))
