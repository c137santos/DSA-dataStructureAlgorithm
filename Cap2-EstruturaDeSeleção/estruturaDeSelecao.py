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

# Exercício de fixação.
# Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem descrescente. Utilize para tal uma seleção encadeada. 

def organizador_crescente(num1, num2, num3):
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    return [num1, num2,num3]

# ELabore um algoritmo que leia o valor de dois números inteiros e a operação aritmética desejada; calcule, então, a resposta adequada. 

def abaco(num1, num2, operador):
    if operador == '-':
        resultado = num1 - num2
    elif operador == '+':
        resultado = num1 + num2
    elif operador == '*':
        resultado == num1 * num2
    elif operador == '/':
        resultado == num1 / num2
    else: 
        return [num1, num2]
    return resultado

# Estrutura de seleção - pag 62
# Escreva um algoritmo que apresente por extenso o nome do mês ou mês inválido.

def qual_o_mes(mes):
    meses= {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4:'abril', 5:'maio', 6:'junho', 7:'julho', 8:'agosto', 9:'setembro', 10:'outubro', 11:'novembro', 12:'dezembro'}
    if mes in meses:
        print(meses[mes])
    else:
        print("Mês inválido")


def data_valida(data):
    meses= {1: 31, 2: 28, 3: 31, 4: 30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    msg = ''
    if '.' in data:
        data = data.split('.')
    elif '/' in data:
        data = data.split('/')
    else:
        msg = "Data no formato inválido"
    dia, mes, ano = int(data[0]), int(data[1]), int(data[2])
    if ano % 4 == 0:
        bissexto = True
        if not ano % 100 == 0:
            bissexto = True
        else:
            if ano % 400 == 0:
                bissexto = True
            else:
                bissexto= False
    else:
        bissexto = False
    if mes >= 1 and mes <= 12:
        if mes == 2 and bissexto == True:
            meses[2] = 29
        if dia >= 1 and dia <= 31:
            if dia <= meses[mes]:
                msg = "Data válida"
            else:
                if mes == 2 and dia == 29:
                    msg = "Dia inválido, pois não se trata de ano bissexto"
                else:
                    msg = "Dia inválido"
        else:
            msg ="Dia inválido"
    else:
        msg ="Mês inválido"
    return msg





