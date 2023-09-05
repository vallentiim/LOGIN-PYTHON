import PySimpleGUI as sg
from getpass import getpass

layout = [[sg.Text('Usuário')],[sg.Input(key = 'usuario')],[sg.Text('Senha')],[sg.Input(key = 'senha')],[sg.Button('login')],[sg.Text('',key = 'mensagem')],]
window = sg.Window('Login', layout = layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_correta = '12345678'
        usuario_correto = 'Valentim'
        usuario = values['usuario']
        senha = values['senha']
        if usuario == usuario_correto and senha == senha_correta:
            window['mensagem'].update('Login feito com sucesso')
        else:
            window['mensagem'].update('Usuário ou senha incorreto')