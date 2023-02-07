# Estrutura de seleção significa a execução dos blocos de códigos que são executados caso condições sejam verdadeiras. 

# Seleção composta utilizada quando temos situações em que duas alternativas dependem de uma mesma condição. Nunca a variável atenderá as duas condições dentro dos blocos. 


# Seleção encadeada. Utilizada quando é preciso agrupar várias seleções. Será executado se um grande numero de condições for verdadeira. 
def selecao_encadeada_homogenea(idade, emprego, morar_so):
    if idade >= 18:
        if emprego:
            if morar_so:
                return 'Adulto indepente'

def test_selecao_encadeada_homogenea_positiva():
    idade = 18
    emprego = True
    morar_so = True
    msg = 'Adulto indepente'
    result = selecao_encadeada_homogenea(idade, emprego, morar_so)
    assert msg == result


def test_selecao_encadeada_homogenea_negativa():
    idade = 17
    emprego = True
    morar_so = True
    msg = 'Adulto indepente'
    result = selecao_encadeada_homogenea(idade, emprego, morar_so)
    assert None == result

#Ela pode ser homogêna, quando condições verdadeiras levam a conclusão da ação. Os operadores lógicos que compõe ela pode ser o e. 

def selecao_encadeada_homogenea_com_operadores(idade, emprego, morar_so):
    if idade > 18 and emprego and morar_so:
        print('Adulto indepente')

def test_selecao_encadeada_homogenea_com_operadores_positiva():
    idade = 18
    emprego = True
    morar_so = True
    msg = 'Adulto indepente'
    result = selecao_encadeada_homogenea(idade, emprego, morar_so)
    assert msg == result

def test_selecao_encadeada_homogenea_com_operadores_negativo():
    idade = 18
    emprego = True
    morar_so = False
    result = selecao_encadeada_homogenea(idade, emprego, morar_so)
    assert None == result

# Caso haja teste seja da mesma variável com o else, equivalente ao código de escolha. 

def selecao_encadeada_homogenea_sem_escolha(codigo):
    if codigo == 1:
        produto = 'Nordeste'
    else:
        if codigo == 2:
            produto = 'Sul'
        else:
            if codigo == 3:
                produto = 'Centroeste'
            else:
                if codigo == 4:
                    produto = 'Norte'
    return produto

def test_encadeada_homogenea_sem_escolha():
    codigo = 3
    produto = 'Centroeste'
    result = selecao_encadeada_homogenea_sem_escolha(codigo)
    assert produto == result

def selecao_encadeada_homogenea_com_escolha(codigo):
    if codigo:
        if codigo == 1:
            produto = 'Nordeste'
        if codigo == 2:
            produto = 'Sul'
        if codigo == 3:
            produto = 'Centroeste'
        else:
            produto = 'Norte'
    return produto

def test_encadeada_homogenea_com_escolha():
    codigo = 3
    produto = 'Centroeste'
    result = selecao_encadeada_homogenea_com_escolha(codigo)
    assert produto == result

#  ou heterogêna, onde não é possível identificar um padrão lógico de contrução da seleção encadeada. 