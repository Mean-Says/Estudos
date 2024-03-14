def maximo(a,b):
    if a > b:
        return a
    else:
        if a == b:
            return 0
        else:
            return b

def test_respostacorreta():
    assert maximo(2,4) == 4

def test_respostacorreta2():
    assert maximo(8,4) == 8

def test_numeros_iguais():
    assert maximo(5,5) == 0


