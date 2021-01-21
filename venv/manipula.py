# Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)
import datetime as dt

def conv_mes(mes):
    if mes == 'Jan':
        return 1
    elif mes == 'Fev':
        return 2
    elif mes == 'Mar':
        return 3
    elif mes == 'Abr':
        return 4
    elif mes == 'Mai':
        return 5
    elif mes == 'Jun':
        return 6
    elif mes == 'Jul':
        return 7
    elif mes == 'Ago':
        return 8
    elif mes == 'Set':
        return 9
    elif mes == 'Out':
        return 10
    elif mes == 'Nov':
        return 11
    elif mes == 'Dez':
        return 12

def converte(entradas):
    a = 7
    if entradas[0:a] == 'Rewards':
        tipo = 1
    else:
        tipo = 0
    a = 9
    data_i = entradas[a]
    while entradas[a] != ')':
        a = a + 1
        data_i = data_i + entradas[a]
    a = len(entradas)
    b = len(entradas) - 1
    while entradas[b] != ' ':
        b = b - 1
    b = b + 1
    data_f = entradas[b:a]
    c = 0
    fsem = 0
    while c < (len(entradas)-1):
        sem = ''
        while entradas[c] != '(':
            c = c + 1
        c = c + 1
        while entradas[c] != ')':
            sem = sem + entradas[c]
            c = c + 1
        if sem == 'sat' or sem == 'sun':
            fsem = fsem + 1
    dia_i = int(data_i[0:2])
    mes_i = data_i[2:5]
    ano_i = int(data_i[5:9])
    dia_f = int(data_f[0:2])
    mes_f = data_f[2:5]
    ano_f = int(data_f[5:9])

    mes_i = conv_mes(mes_i)
    mes_f = conv_mes(mes_f)
    delta = dt.date(ano_f, mes_f, dia_f) - dt.date(ano_i, mes_i, dia_i)
    num_dias = delta.days + 1
    num_dias = num_dias - fsem
    return num_dias, fsem, tipo
