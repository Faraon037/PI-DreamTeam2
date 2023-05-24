from Var_1 import get_result


def test_var1_male():
    data = ['0,3,3,aa,bb,male,7', '0,3,3,2,1,male,6', '0,1,2,6,7,ddd,4', '0,3,3,5,6,female,3', '0,1,2,0,1,male,5']
    tst = get_result(data, 'male', 0, 18)
    assert len(tst) == 3


def test_var1_female():
    data = ['0,3,3,0,2,female,6', '0,3,3,4,5,male,5', '0,1,2,3,4,male,8', '0,3,3,2,6,female,1', '0,1,2,7,8,fff,0',
            '0,1,2,1,1,female,4']
    tst = get_result(data, 'female', 0, 18)
    assert len(tst) == 3
