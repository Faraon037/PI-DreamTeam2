import streamlit as st

def name_cena(data,cena):
    for line in data:
        lst = line.rstrip().split(',')
        if lst[0] == "PassengerId":
            continue
        if float(lst[10])  > float(cena):
            n = lst[3] + lst[4]
            x = ", ".join([lst[2], n[1:-1], lst[6]])
        return x
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
    st.text(name_cena(data,cena))
