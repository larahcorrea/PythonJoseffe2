cliente =[]
produto = []


baseDados = 'CJose dos Santos,42,Sao Paulo;CSandra Silva,36,Sao Jose do Rio Preto;CAugusto Soares,22,Sao Paulo;CVanderlei Azevedo,45,Santos;CVanessa Ferreira,27,Sao Paulo;PMouse,1,9.90;PTeclado,3,19.90;PMonitor,2,349.90;PHD SSD,2,199.90;PProcessador,1,350.00'

baseSplit = baseDados.split(';')

for b in baseSplit:

    baseInfo = b.split(',')



    Nome = (baseInfo[0])



    if (Nome.startswith ('C')):
        Idade = float(baseInfo[1])
        Cidade = (baseInfo[2])

        cliente.append({'Nome': Nome, 'Idade': Idade,'Cidade': Cidade })
    else :
        Quantidade = int(baseInfo[1])
        Preco = (baseInfo[2])
        produto.append({'Produto': Nome, 'Quantidade': Quantidade,'Preço': Preco })

for item in cliente:
    print('Nome' , item['Nome'][1:] )





