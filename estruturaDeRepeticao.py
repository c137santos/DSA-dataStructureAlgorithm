# Existem três estruturas de repetição. A que verifica que é enquanto condição for verdade, quando há uma condição de parada dentro do while True, e quando há um número específico de repetições. 

# Lista de fixação 3 página 61

#Quando verifica a condicional no while estamos em um laço do tipo repetição com teste no ínicio. Enquanto.
def advinha_o_numero():
    numero = 16
    chute = 0
    baixo, alto = '', ''
    while chute != numero:
        chute = int(input("diz um numero "))
        if chute > numero:
            alto = chute
        else:
            baixo = chute
        if alto and baixo:
            print(f"O número está entre {baixo} e {alto}")
        elif alto:
            print(f"O numero está abaixo de {alto}")
        elif baixo:
            print(f"O numero acima de {baixo}")

# Construa um algoritmo que verifique se um número fornecido pelo usuário é primo ou não. Esse algoritmo utilizou o for, que é repetição com variável de controle - para Onde o que controlará é o len de lista_de_divisores. 
# Exercício fixação 3.3 - pagina 62
def e_primo(numero: int):
    if numero == 2:
        return "É primo"
    if numero % 2 == 0 or numero < 0 or numero == 0:
        return "Não é primo"
    lista_de_divisores= [num for num in range(3,numero) ]
    for num in lista_de_divisores:
        if numero % num == 0:
            return "Não é primo"
    return "É primo"

#Construa um algoritmo que calcule o fatorial com while com condição de parada. Esse possui um teste final, portanto el será executado ao menos uma vez, pois sua condição de parada reside no final do teste. 

#Exercício fixação 3.5

def fatorial(numero):
    resultado =0
    while True:
        resultado += numero * numero-1
        numero -=1
        if numero < 2:
            return resultado
            
# Exercício proposta - pag 62.
# Exercício 01

def media_pondera_com_pesos(num1,num2,num3,num4,num5):
    notas = [num1,num2,num3,num4,num5]
    total=0
    for i, nota in enumerate(notas):
        total += nota * (i+1)
    media = total/5
    print(media)

