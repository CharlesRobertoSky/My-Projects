def form(txt=''):
    print(txt)
    num = txt.replace('/', ' / ').replace('*', ' * ').replace('+', ' + ').replace('-', ' - ').split()
    return num


def calc(numero=''):
    expressao = form(numero)
    while True:
        cont = 0
        for key, value in enumerate(expressao):
            if value == '*':
                res1, res2 = expressao.pop(key-1), expressao.pop(key)
                res = float(res1) * float(res2)
                expressao.remove('*')
                expressao.insert(key-1, str(res))
                cont += 1
                break
            if value == '/':
                res1, res2 = expressao.pop(key-1), expressao.pop(key)
                res = float(res1) / float(res2)
                expressao.remove('/')
                expressao.insert(key - 1, str(res))
                cont += 1
                break
        if cont == 0:
            for key, value in enumerate(expressao):
                if value == '+':
                    res1, res2 = expressao.pop(key - 1), expressao.pop(key)
                    res = float(res1) + float(res2)
                    expressao.remove('+')
                    expressao.insert(key - 1, str(res))
                    break
                if value == '-':
                    res1, res2 = expressao.pop(key - 1), expressao.pop(key)
                    res = float(res1) - float(res2)
                    expressao.remove('-')
                    expressao.insert(key - 1, str(res))
                    break
        if len(expressao) <= 2:
            break
    return str(expressao)
