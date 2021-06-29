def salario_liquido(salario_bruto):
    inss = salario_bruto * 0.08
    IR = salario_bruto * 0.11
    Sindicato = salario_bruto * 0.05
    
    print('Salario Bruto: {}'.format(salario_bruto))

    print('Valor de INSS:  {}'.format(inss))

    print('Valor de IR: {}'.format(IR))

    print('Sindicato: {}'.format(Sindicato))

    return salario_bruto - inss - IR - Sindicato

def calcular_salario(salarioHora, horasTrab):
    salario_bruto = salarioHora * horasTrab
    return salario_bruto

salarioHora = int(input('Insira o salário por hora do funcionário: '))
horasTrab = int(input('Insira as horas trabalhadas no mês: '))

print('Salário líquido: {}'.format( salario_liquido(calcular_salario(salarioHora, horasTrab))))

