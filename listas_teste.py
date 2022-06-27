nomes = ['Jeronimo', 'Thais', 'Walter']
print(nomes)

while True:
    adc = str(input("Gostaria de adicionar um nome a lista?: "))
    if adc == 'sim':
        novo = str(input("Insira o novo nome: "))
        nomes.append(novo)

    elif adc == 'nao':
        apaga = str(input("Qual nome deseja apagar?: "))
        nomes.remove(apaga)

    elif adc == 'sair':
        print(f'Itens na lista: {len(nomes)}')
        break

print(nomes)
