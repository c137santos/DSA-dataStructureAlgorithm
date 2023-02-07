from PySimpleGUI import PySimpleGUI as sg

#Biblioteca gráfica que representa os comando do python. Onde tudo será resumido em linhas e colunas. 

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#Janela
janela =sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Maria' and valores['senha'] == 'maria':
            print("Fez sua tela!")
