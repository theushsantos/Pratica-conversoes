import manipulacao_lista

lista_opçoes = ['Localizar','Alterar','Remover','Adicionar','Sair']

lista_numeros = []
def linha():
    return print('-------------------')

inicio = True
while inicio:
    linha()
    print(lista_numeros)
    linha()
    for o in range(0,len(lista_opçoes)):
        print('{:d} : {:s}'.format(o,lista_opçoes[o]))

    opcao = int(input("Qual a opção deseja? "))
    if opcao == 0:
        manipulacao_lista.localizar(lista_numeros)
    elif opcao == 1:
        manipulacao_lista.alterar(lista_numeros)
    elif opcao == 2:
        manipulacao_lista.remover(lista_numeros)
    elif opcao == 3:
        manipulacao_lista.adicionar(lista_numeros)
    elif opcao == 4:
        inicio = False
    else:
        print('Ops! opção invalida, tente novamente!')


