import bubble_sort as BS
while True:
    lista = list()
    fin = False
    while True:
        while True:
            e = input("Dime numeros")

            if e == "fin":
                fin = True
                break

            try:
                e = int(e)
                break
            except:
                print("el dato introducido no es un numero")
        if fin:
            break
        if e == -9999 :
            break

        lista.append(e)

    if fin:
        break


    lo = BS.BubbleSort(lista)
    print("lista ordenada", lo.sorted_list)

