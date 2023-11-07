from datetime import datetime

inicio = datetime.now().microsecond
valor = 101
iteracoes = 0

def raizq(x):
    global iteracoes
    raiz = valor ** 0.5 
    if (raiz ** 2) == valor:
        return valor ** 0.5
    else:
        if x == valor:
            x = 1
        while True:
            f = (x ** 2) - valor 
            f_linha = 2*x 
            resultado = x - (f/f_linha) 
            iteracoes += 1
            if abs(resultado - x) <= 0.1: 
                return resultado
            else:
                return raizq(resultado)
            
print(f'A raiz de {valor} é {raizq(valor)}')
print(f'Foram feitas {iteracoes} iterações.')
print(f'O tempo de execução do código foi de {abs(inicio - datetime.now().microsecond)} em milisegundos.')