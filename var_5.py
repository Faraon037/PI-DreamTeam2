
def pas_save(data,save,name):
#    st.header("Вариант 5. Выполнила Бессонова А.А., группа 3-см")
#    st.info("Вывести Класс, Имя, Возраст спасенных пассажиров с именами, начинающимися на введенный текст")
#    st.subheader("Результат:")
#    name = st.text_input("Введите первые буквы имени спасенного пассажира")
    n = []
    y = []
    ln_name = len(name)
    for line in data:
        lst = line.rstrip().split(',')
        fio = lst[3] + lst[4]
        fio1 = fio[1:ln_name + 1]
        if fio1 == name.capitalize() and int(lst[1]) == int(save) and ln_name > 0:
            y += [fio]
    return y

def var5(data):
    st.header("Вариант 5. Выполнила Бессонова А.А., группа 3-см")
    st.info("Вывести Класс, Имя, Возраст спасенных пассажиров с именами, начинающимися на введенный текст")
    st.subheader("Результат:")
    name = st.text_input("Введите первые буквы имени спасенного пассажира")
    ln_name = len(name)
st.table(pas_save(data,save,name))
