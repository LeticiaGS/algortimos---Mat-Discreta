num = int(input("Informe um número de parada: "))

div = []
vetor = []
primo = False
count = 0

raiz = int( num ** 0.5)

for j in range (2,raiz + 1):
    cont = 0 
    for i in range (2,j):
        cont +=1
        break
    if cont == 0:
        vetor.append(j)

print("Os primos até a raiz inteira é: ",vetor)

for l in vetor:
    if num % l == 0:
        div.append(l)
        count += 1

print("A raiz inteira é: ", raiz)

if count > 0:
    print("O número ",num," não é primo")
else:
    print("O número ",num," é primo")