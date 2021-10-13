#importa o itemgetter
from operator import itemgetter
#cria lista e dicionario
lista = []
cadastro = {}
#solicita ao usuario o que deseja fazer, e se digitar uma opcao diferente o programa pede novamente ate que a
# opção seja satisfeita
while True:
    opcao = int(input('Cadastrar Produto: 0 - Não  1 - Sim : '))
    #insere os dados dentro da lista em forma de dicionario
    if opcao == 1:
        #cria no dicionario, com as chaves codigo, estoque e mínimo
        cadastro['codigo'] = int(input('Codigo: '))
        #se o usuario digitar 0, informa que o valor nao é valido e encera o programa
        if cadastro['codigo'] == 0:
            print( 'Valor invalido! Encerrando programa...')
            break
        cadastro['estoque'] = int(input('Estoque: '))
        cadastro['minimo'] = int(input('Mínimo: '))
       #adiciona os dados na lista, copiando os valores para cada chave do dicionário respectivamente
        lista.append(cadastro.copy())
    #se a opção digita for zero, sistema para e apresenta a tabela com produtos cadastrados
    else:
        if opcao == 0:
            break
print('_'*37)
# verifica se a lista é maior que zero, ou seja se ha itens cadastrados
if len(lista) > 0:
    print('     Lista de produtos ordenada:')
    print('_' * 37)
    #imprime os campos da tabela em uma linha com espaço centralizando, o end recebe aspa sem espaço, para
    # continuar na mesma linha
    # para nao quebrar linha
    print('Código'.center(12), end='')
    print('Estoque'.center(12), end='')
    print('Mínimo'.center(12))
    print('|'+'-' * 10 + '|' + '-'*11 +'|' + '-'*12 + '|')
    #a condiçao for é usada para verificar os itens, no dicionario cadastro, colcando em ordem crescente a chave có-digo
    # que estao na lista, enquanto houver produtos essa condição irá acontecer
    for cadastro in sorted(lista, key=itemgetter('codigo')):
        #imprime ordenado os dados dentro de cada chave respectivamente, e o end recebe aspas sem espaço
        # para continuar na mesma a linha
        print(str(cadastro['codigo']).center(12), end='')
        print(str(cadastro['estoque']).center(12), end='')
        print(str(cadastro['minimo']).center(12))
        #imprime a separação entre as linhas e colunas da tabela
        print('|'+'-' * 10 + '|' + '-'*11 +'|' + '-'*12 + '|')
        # se nao houver produtos cadastrados ira imprimir a mensagem de cadastro vazio
else:
    print('Cadastro vazio!')
