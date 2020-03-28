import random

a = []
def lista():
    for i in range(0, 10):
        a.append(random.randint(1, 10))
lista()

def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
 
    return sum/len(lista)

print("Lista: %s" % a)
print("El promedio es: %s" % promediarLista(a))