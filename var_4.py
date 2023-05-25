import streamlit as st

def name_cena(data, cena):
    n = []
    for line in data:
#        lst = line.rstrip().split(',')
        if line.split(",")[0] == "PassengerId":
            continue
        if float(line.split(",")[10]) > float(cena):
            n += [line.split(",")[3] + line.split(",")[4]]
    return n
#        if float(line.split(",")[10]) > float(cena):
#           name = [lst[3] + lst[4]]
 #           name_out = ", ".join(name[1:-1])
 #       return name_out

def var4(data):
    st.header('Вариант 4. Выполнила Беляева М.М., группа 3-см')
    st.subheader("Задание:")
    st.info("Вывести имена пассажиров, стоимость билета которых была выше указанной")
    st.subheader("Результат:")
    cena = st.text_input("Введите стоимость билета", 10000)
    for line in data:
        st.text(name_cena(data, cena))
