valores = [] 
auxiliar = []

continuar = True

while continuar == True:

    entrada = int(input('Insira um valor positivo para o andamento da aplicação ou digite (-1) para fechar a aplicação:\n'))

    if entrada == -1:

        continuar = False

    elif entrada < -1:

        print('ERRO: Insira um valor positivo!')

    else:

        valores.append(entrada)  

if len(valores) > 0:   

    print('\nNumero de valores lidos: {}'.format(len(valores)))

    print(valores)

    print('Ordem inversa da lista')

    i = len(valores)

    for passo in valores:

        i = i -1

        auxiliar.append(valores[i])

    print(auxiliar)

    print('Soma dos valores da lista')

    soma = 0

    for passo in range(0, len(valores)):

        soma = soma + valores[passo]

    print(soma)

    print('Média dos valores da lista')

    media = soma / len(valores)

    print(media)

    print('Valores acima da média')

    auxiliar.clear()

    for passo in range(0, len(valores)):

        if valores[passo] > media:

            auxiliar.append(valores[passo])

    print(auxiliar)

    print('Valores da lista que são abaixo de 7')

    auxiliar.clear()

    for passo in range(0, len(valores)):

        if valores[passo] < 7:

            auxiliar.append(valores[passo])

    print(auxiliar)

    print('\nO programa será finalizado')

    input('')
