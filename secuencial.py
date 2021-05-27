ta = eval (input ("hola ingrese usuario tiempo ="))
da = eval(input("Ingrese distancia recorrida ="))

ti = (ta * 0.7) + ta
di = (da * 0.55) + da


print("tiempo anterior = " + str(ta) + "h")
print("distancia anterior = " + str(da) + "km")
print("tiempo incremento = " + str(ti) + "h")
print("distancia incremento = " + str(di) + "km")


# haremos un segundo secuencial

import math
la = 10
an = 5
al =10
di = math.sqrt(al**2 + an**2 + la**2)
print("Diagonal =" + str(di))
