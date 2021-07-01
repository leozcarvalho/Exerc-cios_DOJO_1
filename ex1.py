respostasPositivas = ['s' ,'sim','Sim','SIM' ]
    
respostaNegativas = ['n' ,'nao' ,'Não','não','NÃO','NAO']

def perguntar(pergunta):

    resposta = ''

    while True:

        resposta = input(pergunta)

        if resposta in respostasPositivas or resposta in respostaNegativas:

            return resposta

        else:

            print('Reposta Invalida!')

respostas = []

sim = 0

nao = 0

print('Ocorreu um assasinato e você está sendo interrogado.\nResponda as perguntas com (S)im ou (N)ão ')

respostas.append(perguntar('Telefonou para a vitima? '))

respostas.append (perguntar('Esteve no local do crime? '))

respostas.append (perguntar('Mora perto do local do crime? '))

respostas.append (perguntar('Devia para a vitima? '))

respostas.append (perguntar('Já trabalhou com a vítima? '))

print(respostas)

for i in range(5):

    if respostas[i] in respostasPositivas:

        sim = sim + 1

    elif respostas[i] in respostaNegativas:

        nao = nao + 1

if sim == 5:

    print('Assassino')

elif sim == 4 or sim == 3:

    print('Cumplice')

elif sim == 2:

    print ('Suspeito')

else:

    print ('Inocente')
