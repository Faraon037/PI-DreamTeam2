from var_5 import pas_save

def test_alive_iv():
    data = ['0,1,2,"Ivanov,Out"', '1,1,2,"Petrov,Out"', '2,1,1,"Ivan,Out"']
    assert pas_save(data, "Iva") == ['"IvanovOut"','"IvanOut"']


def test_alive_ru():
    data = ['0,1,2,"Ruanor,Out"', '1,1,2,"Rutrov,Out"', '2,0,1,"Rubov,Out"']
    assert pas_save(data, "ru") == ['"RuanorOut"','"RutrovOut"']

