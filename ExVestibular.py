alunosAprov = []

alunosVestibular = 'Jose dos Santos,7,Sao Paulo;Sandra Silva,6.5,Sao Jose do Rio Preto;Augusto Soares,8,Sao Paulo;Vanderlei Azevedo,5.65,Santos;Vanessa Ferreira,9,Sao Paulo;Natan Cruz,10,Sao Paulo'

listaVest = alunosVestibular.split(';')
for v in listaVest :
    alunosInfo = v.split(',')

    notas = float(alunosInfo[1])

    if notas >= 7 :
        alunosAprov.append ({'Nome' : alunosInfo[0],'Nota' : notas , 'Cidade': alunosInfo[2]  })

for item in alunosAprov:
    print('Nome:', item['Nome'])
    print('Cidade:', item['Cidade'])
    print()     
    


