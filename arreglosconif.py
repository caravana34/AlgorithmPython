"""ARREGLOS UNIDIMENSIONALES"""
"""GUARDAR en un arreglo los numeros pares y en otro arreglo los numeros impares
comprendidos del 1 al 100 e imprimirlos por la pantalla, .append (guardar)"""


par = []
impar = []

for i in range(1,101):
    if i%2==0:
        par.append(i)
    else:
        impar.append(i)

print (par)
print(impar)
