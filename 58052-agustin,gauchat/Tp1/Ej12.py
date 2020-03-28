import random
import operator
 
A = {1 : None, 2 : None, 3 : None, 4 : None, 5 : None}
 
for i in range (1, 6):
    A[i] = random.randint(1, 10)
 
print("Diccionario inicial:")
for i in range(1, 6):
    if i == 5:
        print(str(A[i])+ "\n")
    else:
        print(str(A[i]) + ", ", end="")

Aord = sorted(A.items(), key=operator.itemgetter(1), reverse=True)

print("Diccionario ordenado:")
for j in range(0, 5):
    a = Aord[j][1]
    if j == 4:
        print(str(a)+ "\n")
    else:
        print(str(a) + ", ", end="")