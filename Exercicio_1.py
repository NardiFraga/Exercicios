# solicita ao usuário se deseja continuar, S/N
opcao = str(input('Inserir dados? S/N '))
#Laço de repetição, que irá repetir sempre que o usuário digitar S
while ( opcao == 's' or opcao == 'S'):
    #solicita ao usuário para digitar nome do aluno e sua nota
    aluno = str(input('Nome do aluno: '))
    #valida a nota, caso o usuario digite letras o sistema informa o erro e pede novamnete que digite uma nota
    while True:
        try:
            nota = float(input('Nota final: '))
            break
        except ValueError:
            print('Nota invalida!')
    #Esta condição testa em qual conceito o aluno se enquadra
    if (nota >= 9.0):
        conceito = 'A'
        print('O aluno(a) {} tirou nota {} e se enquadra no conceito {}.'.format(aluno.upper(), nota, conceito))
    elif ( nota < 9.0 and nota >= 7.0):
        conceito = 'B'
        print('O aluno(a) {} tirou nota {} e se enquadra no conceito {}.'.format(aluno.upper(), nota, conceito))
    elif (nota < 7.0 and nota >= 5.0):
        conceito = 'C'
        print('O aluno(a) {} tirou nota {} e se enquadra no conceito {}.'.format(aluno.upper(), nota, conceito))
    elif(nota < 5.0 and nota >= 3.0):
        conceito = 'D'
        print('O aluno(a) {} tirou nota {} e se enquadra no conceito {}.'.format(aluno.upper(), nota, conceito))
    elif(nota < 3.0):
        conceito = 'E'
        print('O aluno(a) {} tirou nota {} e se enquadra no conceito {}.'.format(aluno.upper(), nota, conceito))
    else:
        print('Nota invalida!')
    #Solicita se deseja continuar
    opcao = str(input('Inserir dados? S/N '))
#Se o usuário optar por N ou qualquer outro caractere, o programa é encerrado
else:
    print('Encerrando programa ... ')
