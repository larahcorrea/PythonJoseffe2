arquivo = open("./lista_compra-nova.txt", "a")

for i in range(0,3,1):
    produto = input('Digite o nome do produto: ')
    quantidade = input('Digite a quantidade do produto: ')
    preco = input('Digite o preço do produto: ')
    arquivo.write(f'{produto},{quantidade},{preco}\n')

