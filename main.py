import streamlit as st
import var_1
import var_4
import var_5
import var_11
import var_10
with open("data.csv") as file:
    data = file.readlines()
st.title('Веб-приложение "ТИТАНИК" (разработка PI-DreamTeam2)')
option = st.selectbox('Выберите исполнителя', ('Григорьева К.В.',
                                               'Александрова Е.В', 'Кузнецов Н.В.', 'Беляева М.М.', 'Бессонова А.А.'))
if option == 'Григорьева К.В.':
    var_11.run_result(data)
if option == 'Александрова Е.В':
    var_1.var1(data)
if option == 'Кузнецов Н.В.':
    var_10.var10(data)
if option == 'Беляева М.М.':
    var_4.var4(data)
if option == 'Бессонова А.А.':
    var_5.var5(data)
