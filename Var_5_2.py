import streamlit as st
def var5_2():
    st.header("Вариант 5. Выполнила Бессонова А.А., группа 3-см")
    st.info("Вывести Класс, Имя, Возраст спасенных пассажиров с именами, начинающимися на введенный текст")
    st.subheader("Результат:")
    name = st.text_input("Введите первые буквы имени спасенного пассажира")
    ln_name = len(name)
    with open("data.csv") as file:
        for line in file:
            lst = line.rstrip().split(',')
            fio = lst[3] + lst[4]
            fio1 = fio[1:ln_name + 1]
            if fio1 == name.capitalize() and lst[1] == "1" and ln_name > 0:
                n = lst[3] + lst[4]
                x = ", ".join([lst[2], n[1:-1], lst[6]])
                st.text(x)
