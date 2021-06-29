def perguntar(pergunta):
    resposta = ''
    respostasValidas = ['s' ,'sim','Sim','SIM' ,'n' ,'nao' ,'Não','não','NÃO','NAO']
    while True:
        resposta = input(pergunta)
        if resposta in respostasValidas:
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
    if(respostas[i] == 's'):
            sim = sim + 1
    elif respostas[i] == 'n':
        nao = nao + 1
    


if sim == 5 and nao == 0:
    print('Assassino')
elif sim == 4 or sim == 3:
    print('Cumplice')
elif sim == 2:
    print ('Suspeito')
else:
    print ('Inocente')

