import manipula as mp

while 1:
    entradas = input('Dados do Cliente: ')

    num_dias, fsem, tipo = mp.converte(entradas)

    def encontra_hotel(num_dias, fsem, tipo):
        hot1 = 0
        hot2 = 0
        hot3 = 0
        if tipo == 0:
            hot1 = 110*num_dias + 90*fsem
            hot2 = 160*num_dias + 60*fsem
            hot3 = 220*num_dias + 150*fsem
        elif tipo == 1:
            hot1 = 80*num_dias + 80*fsem
            hot2 = 110*num_dias + 50*fsem
            hot3 = 110*num_dias + 40*fsem
        print(hot1)
        print(hot2)
        print(hot3)
        if hot3 <= hot2 and hot3 <= hot1:
            return 'Ridgewood'
        elif hot2 <= hot1:
            return 'Bridgewood'
        else:
            return 'Lakewood'


    resultado = encontra_hotel(num_dias, fsem, tipo)
    print(resultado)
