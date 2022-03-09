import PySimpleGUI as sg
from time import sleep
from code import operador, menu

from PySimpleGUI.PySimpleGUI import Input


#layout
layout = [ 
[sg.Text('Calc:', size=(5,0)), sg.Input(size=(25,0))],
[sg.Text('Resp:', size=(5,0)), sg.Output(size=(25,0))],
[sg.Button(f'{"1": ^7}'),sg.Button(f'{"2": ^7}'),sg.Button(f'{"3": ^7}'),sg.Button(f'{"+": ^7}')],
[sg.Button(f'{"4": ^7}'),sg.Button(f'{"5": ^7}'),sg.Button(f'{"6": ^7}'),sg.Button(f'{"-": ^7}')],
[sg.Button(f'{"7": ^7}'),sg.Button(f'{"8": ^7}'),sg.Button(f'{"9": ^7}'),sg.Button(f'{"%": ^7}')],
[sg.Button(f'{"*": ^7}'),sg.Button(f'{"0": ^7}'),sg.Button(f'{"/": ^7}'),sg.Button(f'{"=": ^7}')]
]
#window
window = sg.Window('CalculadoraV3', layout)
while True:
        #Extract data from Screen
        events, values = window.read()
#    menu.cabeçalho('CalculadoraV2')
#    numero = menu.corr('Digite a operação: ')
#    resp = operador.calc(numero)
#    print(f'A resposta é {resp}')
#    continuar = ''
#    while True:
#        continuar = str(input('Você quer continuar?(S/N) ')).strip().upper()[0]
#        if continuar in 'SN':
#            break
#        else:
#            print('\033[31mOpção inválida!\033[m', end=' ')
#    if continuar in 'N':
#        print('\033[34mEncerrando programa\033[m', end='')
#        sleep(0.3), print('.', end=''), sleep(0.3), print('.', end=''), sleep(0.3), print('.'), sleep(0.5)
#        break
window.close()
