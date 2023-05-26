from var_5 import pas_save

def test_alive_iv():
    data = ['0,1,2,"Ivanov,Out"', '1,1,2,"Petrov,Out"', '2,1,1,"Ivan,Out"']
    assert var5(data, 1, "Iva") == ['"IvanovOut"','"IvanOut"']


def test_deatha_ru():
    data = ['0,0,2,"Ruanor,Out"', '1,0,2,"Rutrov,Out"', '2,1,1,"Ribov,Out"']
    assert var5(data, 0, "ru") == ['"RuanorOut"','"RutrovOut"']

