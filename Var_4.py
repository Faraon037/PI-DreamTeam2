import streamlit as st
def var4():
st.header('Вариант 4. Выполнила Беляева М.М., группа 3-см')
st.subheader("Задание:")
st.info("Вывести имена пассажиров, стоимость билета которых была выше указанной")
st.subheader("Результат:")
cena = st.text_input("Введите стоимость билета", 10000)
with open("data.csv") as file:
    for line in file:
        if line.split(",")[0] == "PassengerId":
            continue
        if float(line.split(",")[10]) > float(cena):
            fare = (line.split(",")[10])
            name = line.split(",")[3] + line.split(",")[4]
            res  = (name[1:-1] + ", " + "Цена билета " + "- " + fare)
            st.text(res)
