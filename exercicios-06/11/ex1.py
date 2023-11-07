num = int(input("\nInforme um número: "))

div = []
vetor = []
numPrimo = False

raiz = int( num ** 0.5)

for j in range (2, raiz + 1):
    divisivel = False 
    for i in range (2, j):
        if j % i == 0 :
           divisivel = True
           break
    if not(divisivel):
        vetor.append(j)

for l in vetor:
    if num % l == 0:
        div.append(l)
        numPrimo = True


print("\nA raiz inteira é: ",raiz)
print("Os primos até a raiz inteira são: ",vetor)

if numPrimo:
    print(f'O número {num} não é primo pois é divisível por {div}\n')
else:
    print(f'O número {num} é primo pois não é divisível por nenhum dos primos de sua raiz inteira.\n')