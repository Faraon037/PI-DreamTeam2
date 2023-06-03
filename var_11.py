import streamlit as st


def var11(file, attribute):
    avr_dead_alive = 0
    sum_dead_alive = 0
    count_dead_alive = 0
    for line in file:
        str = line.split(',')
        if str[1] == attribute:
            count_dead_alive += 1
            sum_dead_alive += float(str[10])
    avr_dead_alive = sum_dead_alive / count_dead_alive
    return avr_dead_alive


# Сим комментарием доказываю, что я, Григорьева Ксения, сама внесла изменения в данный файл
# в 23:53 по Красноярску 03.06.2023.

def run_result(data):

    st.header('Вариант 11')
    st.header('Выполнила Григорьева К.В., группа 3-см')
    st.subheader("Задание:")
    st.info('Посчитать среднюю стоимость билета (поле Fare) у пассажиров, указав - спасен или нет.')
    st.subheader("Результат:")

    choice = st.radio('Показатель везения пассажира', options=['Спасен', 'Погиб'])
    if choice == 'Спасен':
        avr_out = var11(data, '1')
        text_out = 'Средняя стоимость билета спасенных пассажиров'
    elif choice == 'Погиб':
        avr_out = var11(data, '0')
        text_out = 'Средняя стоимость билета погибших пассажиров'
    st.text(text_out)
    st.success(avr_out)
