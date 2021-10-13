# importa a função random
import random
# cria a lista
lista = []
#valida a opcao, e enquanto for veradeira faz o cadastro de novos participantes do sorteio
while True:
    opcao = str(input('Cadastrar? S/N? '))
    # solicita ao usuario se deseja cadastrar, então pede nome e valor doado.
    if opcao == 'S' or opcao == 's':
        nome = str(input('Nome: '))
        valor = float(input('Valor R$: '))
        # pega somente a parte inteira do resultado da divisão
        vezes = int(valor // 10)
        # este laço ira repetir ate que a variavel x seja maior que a variavel vezes, e adiciona o nome
        # a lista para sorteio. A funçao append insere nome cadastrato na lista
        x = 1
        while x <= vezes:
            lista.append(nome[:])
            x = x + 1
    #se a opcao escolhida for n, o cadastro se encerra e imprime a lista de particiantes do sorteio, na
    # sequencia embaralha a lista com a função shuffle, e a função choice para sortear o ganhador.
    else:
        if opcao == 'n' or opcao == 'N':
            break
print('Lista de participantes do sorteio:{} '.format(lista))
embaralha = random.shuffle(lista)
print('Lista de nomes embaralhada:{} '.format(lista))
sorteia = random.choice(lista)
print('Nome sorteado: {}'.format(sorteia))
