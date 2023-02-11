from estruturaDeSelecao import organizador_crescente, data_valida

def test_organizador_crescente():
    lista = [1,2,3]
    result = organizador_crescente(3,2,1)
    assert lista == result

    
def test_organizador_crescente_dois():
    lista = [1,2,3]
    result = organizador_crescente(2,3,1)
    assert lista == result


def test_organizador_crescente_com_negativo():
    lista = [-11,2,3]
    result = organizador_crescente(2,-11,3)
    assert lista == result

def test_data_valida_dia_invalido_generico():
    msg = 'Dia inválido'
    result = data_valida('30.02.2024')
    assert msg == result


def test_data_valida():
    msg = 'Data válida'
    result = data_valida('30.03.2024')
    assert msg == result


def test_data_valida_em_ano_bissexto():
    msg = 'Data válida'
    result = data_valida('29.02.2024')
    assert msg == result


def test_data_invalida_em_ano_bissexto():
    msg = 'Dia inválido, pois não se trata de ano bissexto'
    result = data_valida('29.02.2023')
    assert msg == result