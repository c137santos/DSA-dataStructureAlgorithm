# Exercício de fixação 75
#1.4 Desenvolva um algoritmo que leia um vetor de 20 posições inteira e coloque em ordem crescente, utilizando a seguinte estratégia de ordenação.
# Selecione o elemento do vetor de 20 posições que apresenta o menor valor, troque este elemento pelo primeiro. Repita a operação envolvendo apenas os 19 elementos restantes.

def reordenador_de_elementos_por_selecao_direta(lista_para_ordernar):
    menor = 10000000
    for i in range(len(lista_para_ordernar)):
        for indice_de_lista, item in enumerate(lista_para_ordernar[i:]):
            if item < menor:
                indice_do_menor = indice_de_lista + i
                menor = item
        lista_para_ordernar[i], lista_para_ordernar[indice_do_menor] = lista_para_ordernar[indice_do_menor], lista_para_ordernar[i]
        menor = 10000000
    return lista_para_ordernar

def reordencador_por_bubble_sort(lista_para_ordernar):
    for i in range(len(lista_para_ordernar)):
        for i in range(len(lista_para_ordernar)-1):
            if lista_para_ordernar[i] > lista_para_ordernar[i+1]:
                lista_para_ordernar[i], lista_para_ordernar[i+1] = lista_para_ordernar[i+1], lista_para_ordernar[i]
    return lista_para_ordernar