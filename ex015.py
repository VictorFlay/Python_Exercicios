dias = int(input('Informe quantos dias o carro ficou alugado: '))
km = float(input('Informe quantos km foram percorridos: '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de: R${:.2f}'.format(pago))