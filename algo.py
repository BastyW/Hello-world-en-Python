def mul_lista(numeros):
    producto = 1

    for numero in numeros:
        producto *= numero

    return producto

numeros = [1, 3, 4 ,5, 8]

print(mult_lista(numeros))
