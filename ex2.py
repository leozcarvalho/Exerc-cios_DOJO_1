valor = []
x = int(0)
aux = []
aux1 = []
aux2 = []
soma = 0

while True:
    x = int(input('Insira um valor positivo para o andamento da aplicação ou digite (-1) para fechar a aplicação:\n'))
    if x > -1:
        valor.append(x)  
   
    elif x == -1:
        break

    else:
        print('Erro!')
        break

        
    
print('\nNumero de valores lidos: {}'.format(len(valor)))
print(valor)

i = len(valor)

print('Ordem inversa da lista')

for passo in valor:
    i = i -1
    aux.append(valor[i])
print(aux)

print('Soma dos valores da lista')

for passo in range(0, len(valor)):
    soma = soma + valor[passo]
print(soma)

print('Média dos valores da lista')

media = soma / len(valor)
print(media)

print('Valores acima da média')

for passo in range(0, len(valor)):
    if valor[passo] > media:
        aux2.append(valor[passo])
print(aux2)


print('Valores da lista que são abaixo de 7')

for passo in range(0, len(valor)):
    if valor[passo] < 7:
        aux1.append(valor[passo])
print(aux1)
    
print('\nO programa será finalizado')
input('')