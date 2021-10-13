# função para gerar email, foi usado dois parametros, um para o nome e outro para o sobrenome
def email (nome, sobrenome):
    #nome no indice [0] para pegar o primeiro caracter do nome.
    # Utilizo a função lower para deixar todos caracteres em caixa baixa
    return 'Sr.(a) ' + nome + ' ' + sobrenome + ', seu email é: ' +(nome[0].lower()+ sobrenome.lower() +'62'+'@algoritmo.com.br')
    # return é utilizado para dar um retorno da função, neste caso exibe uma mensagem com email, utilizo sinal de + para concatenar

# principal
#imprime na tela a função que gera email. E é feita a passagem de parametros, com envio de dados para função
print (email('Nardiele', 'Fraga'))
