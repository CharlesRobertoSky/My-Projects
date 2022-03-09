def linha(txt='-'):
    if len(txt) == 1:
        return f'{txt}' * 42
    elif len(txt) == 2:
        return f'{txt}' * 21


def cabeçalho(txt=''):
    print(linha('='))
    print(txt.center(42))
    print(linha('='))


def corr(txt=''):
    try:
        while True:
            numero = input(txt).upper()
            if numero.isupper():
                print('\033[31mERRO! Digite uma expressão válida usando "+, -, *, /.\033[m')
            else:
                break
    except:
        print('\033[31mERRO! Digite uma expressão válida usando "+, -, *, /.\033[m')
    else:
        return numero
