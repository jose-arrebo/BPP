##############
# APARTADO 1 #
##############
import pdb
pdb.set_trace()


def apartado1(lista_listas):
    result = []
    lista_depurada = []
    # Elimino listas vacias para que no den problemas con la funcion max
    for l in lista_listas:
        if l != []:
            lista_depurada.append(l)
    if lista_depurada != []:
        result = list(map(max,lista_depurada))
    return result

##############
# APARTADO 2 #
##############
import math


def esPrimo(x):
    result = False
    if not (x in [0,1]):
        # Solo es necesario explorar divisores hasta la raiz cuadrada
        lim = math.ceil((math.sqrt(x)))
        div = 0
        for i in range(1, lim + 1):
            if (x%i) == 0:
                div += 1
        result = div == 1
    return result


def apartado2(lista):
    return list(filter(esPrimo, lista))

if __name__ == "__main__":
    print(apartado1([[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]))
    print(apartado1([[], [1,2,3,4,5,6,7,8], [100,250,43]]))
    print(apartado2([3, 4, 8, 5, 5, 22, 13]))