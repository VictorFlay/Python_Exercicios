salario = float(input('Digite o salário: R$'))
aumento = salario + (salario * 15/100)
print('Salário original: R${:.2f}'.format(salario))
print('Novo salário: R${}'.format(aumento))