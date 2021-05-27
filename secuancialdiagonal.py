"""en la aprte alta de la esquina de una habitación se instala una camara que detecta el movimeinto. Para su configuración
se requiere conocer la distancia más lejana que hay entre esta y la parte inferiorde la esquina opuesta a la cámara para que sto sea posible se requeire leer el largo, el ancho
y el alto de la habitación. Se recomienda utilizar la fórmula de la diagonal de un rectangulo. diagonal = raiz de (alto)*2 + (ancho)*2 + (largo)*2"""


import math

la=10
an = 5
al= 10

di= math.sqrt(al**2+an**2+la**2)
print ("diagonal= " + str(di))
