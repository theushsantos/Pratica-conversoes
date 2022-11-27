#Modulo para manipulação de lista simples

def localizar(lista_numeros):
    valor = float(input("Qual valor deseja localizar? "))
    for i in range(0,len(lista_numeros)):
        if lista_numeros[i] == valor:
            print(f'Valor localizado na posição {i}: {valor}')
            return
        print('Valor não localizado.')
        return

def alterar(lista_numeros):
    pos = int(input('Qual a posição que quer alterar? '))
    if pos >= 0 and pos < len(lista_numeros):
        valor = float(input("Qual o novo valor? "))
        lista_numeros[pos] = valor
        print(f'Valor alterado na posição {pos}')
    else:
        print(f'Posição {pos} invalida!')
    return

def remover(lista_numeros):
    pos = int(input("Qual posição deseja remover? "))
    if pos>=0 and pos<len(lista_numeros):
        valor = lista_numeros.pop(pos)
        print(f'Valor ({valor}) da posição {pos} removida!')
    else:print(f'Posição {pos} invalida!')
    return

def adicionar(lista_numeros):
    valor = float(input("Qual valor deseja adicionar ? "))
    lista_numeros.append(valor)
    print(f'Valor {valor} foi adicionado.')

