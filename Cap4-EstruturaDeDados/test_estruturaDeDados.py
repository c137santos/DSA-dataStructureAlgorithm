from ExercicioDeFixacaoI import reordenador_de_elementos_por_selecao_direta, reordencador_por_bubble_sort


def teste_reordenador_de_elementos_em_vetor():
    esperado = [1 ,3 ,5, 6, 7, 9]
    lista_baguncada = [9, 7, 1, 5, 3, 6,]
    result = reordenador_de_elementos_por_selecao_direta(lista_baguncada)
    assert result == esperado


def teste_reordenador_de_elementos_em_vetor_com_numero_repetido():
    esperado = [1 ,1 ,5, 6, 15, 19]
    lista_baguncada = [19, 1, 5, 1, 15, 6,]
    result = reordenador_de_elementos_por_selecao_direta(lista_baguncada)
    assert result == esperado

def teste_reordencador_por_bubble_sort():
    esperado = [1 ,3 ,5, 6, 7, 9]
    lista_baguncada = [9, 7, 1, 5, 3, 6,]
    result = reordencador_por_bubble_sort(lista_baguncada)
    assert result == esperado
    