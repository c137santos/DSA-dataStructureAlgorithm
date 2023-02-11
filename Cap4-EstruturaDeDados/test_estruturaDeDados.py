from ExercicioDeFixacaoI import reordenador_de_elementos_em_vetor 


def teste_reordenador_de_elementos_em_vetor():
    esperado = [1 ,3 ,5, 6, 7, 9]
    lista_bagunçada = [9, 7, 1, 5, 3, 6,]
    result = reordenador_de_elementos_em_vetor(lista_bagunçada)
    assert result == esperado

    