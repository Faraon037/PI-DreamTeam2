import streamlit as st
def var5_2():
    st.title('"Титаник"')
    st.header("Вариант №5 выполнила Бессонова А. группа 3 см")
    st.subheader("Задание: Вывести Класс, Имя, Возраст спасенных с именами начинающихся на введенный текст")
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
