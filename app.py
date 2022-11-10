from modules.CifraCesar import CifraCesar
from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('reddit')
layout = [
    [sg.Text('Digite a chave da cifra')],
    [sg.Input(key='key')],
    [sg.Text('Insira a mensagem')],
    [sg.Input(key='message')],
    [sg.Text('Criptografia:')],
    [sg.Input(readonly=True, key='cifra')],
    [sg.Button('Criptografar')],
    [sg.Button('Descriptografar')],
]


# Window
janela = sg.Window('Verificação de acesso', layout)
# ler Dados

while True:
    eventos, valores = janela.read()

    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Criptografar':
        try:
            key = int(valores['key'])
            crypt = CifraCesar(key)
            messageEncrypted = crypt.encryptMessage(valores['message'])
            janela['cifra'].update(messageEncrypted)
        except:
            janela['cifra'].update('Utilize apenas números para a chave')

    if eventos == 'Descriptografar':
        try:
            crypt.decryptMessage()
            janela['cifra'].update(crypt.getMessage())
        except:
            janela['cifra'].update('Utilize apenas números para a chave')
