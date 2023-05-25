from var_4 import name_cena


def test_10():
    data = ["0,1,2,Test,Test,5,6,7,8,9,30", "1,1,2,Test,Test,5,6,7,8,9,60", "2,1,2,Test,Test,5,6,7,8,9,90"]
    assert name_cena(data, 10) == ["TestTest", "TestTest", "TestTest"]

    
def test_50():
    data = ["0,1,2,Test,Test,5,6,7,8,9,45", "1,1,2,Test,Test,5,6,7,8,9,60", "2,1,2,Test,Test,5,6,7,8,9,20"]
    assert name_cena(data, 50) == ["TestTest"]


def test_80():
    data = ["0,1,2,Test,Test,5,6,7,8,9,45", "1,1,2,Test,Test,5,6,7,8,9,60", "2,1,2,Test,Test,5,6,7,8,9,20"]
    assert name_cena(data, 80) == []
