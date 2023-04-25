import streamlit as st


def var11():
    avr_dead = 0
    avr_alive = 0
    sum_dead = 0
    sum_alive = 0
    count_dead = 0
    count_alive = 0
    with open('data.csv') as file:
        for line in file:
            str=line.split(',')
            if str[1] == '0':
                count_dead += 1
                sum_dead += float(str[10])
            elif str[1] == '1':
                count_alive += 1
                sum_alive += float(str[10])
        avr_dead = sum_dead/count_dead
        avr_alive = sum_alive/count_alive
    st.title('Приложение "Титаник"')
    st.header('Вариант 11. Выполнила Григорьева К.В., группа 3-см')
    st.subheader('Задание: Посчитать среднюю стоимость билета (поле Fare) у пассажиров, указав - спасен или нет.')
    choice = st.radio ('Показатель везения пассажира', options = ['Спасен', 'Погиб'])
    if choice == 'Спасен':
        avr_out = avr_alive
        text_out = 'Средняя стоимость билета спасеннных пассажиров'
    elif choice == 'Погиб':
        avr_out = avr_dead
        text_out = 'Средняя стоимость билета погибших пассажиров'
    st.text (text_out)
    st.text (avr_out)