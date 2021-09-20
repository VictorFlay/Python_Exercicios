preco = float(input('Digite o preço do produto: '))
novo = preco - (preco * 5/100)
print('O preço original do produto é de R${:.2f}\n Com desconto de 5% passará a ser R${}'.format(preco, novo))
