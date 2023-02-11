from estruturaDeSelecao import organizador_crescente

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