#mercado
lista_produtos = ['macarrão','feijão','uva','sal']
lista_valores = [2.50,5.00,10.00,5.00]
print('Escolha seus produtos: ')
print(lista_produtos)

carrinho = []
meus_valores = []

#input produtos
produto1 = int(input('Digite o protudo: '))
produto2 = int(input('Digite o protudo: '))
produto3 = int(input('Digite o protudo: '))
produto4 = int(input('Digite o protudo: '))
produto5 = int(input('Digite o protudo: '))
produto6 = int(input('Digite o protudo: '))


#soma de valores dos produtos escolhidos
carrinho += (lista_produtos [produto1],lista_produtos [produto2],lista_produtos [produto3],lista_produtos [produto4],lista_produtos [produto5],lista_produtos [produto6])
meus_valores +=(lista_valores [produto1],lista_valores [produto2],lista_valores [produto3],lista_valores [produto4],lista_valores [produto5],lista_valores [produto6])


#Print na tela simulando a tela de um mercado
print('SEUS PRODUTOS', carrinho)
print('VALORES', meus_valores)
soma = sum (meus_valores)
print('===========TOTAL============')
print('R$', soma)