import random

# Listas para armazenar os dados dos clientes
nomes = []
telefones = []
enderecos = []

# Loop para obter dados dos clientes
while True:
    nome = input("Insira o nome do cliente (ou 'fim' para terminar): ")
    if nome.lower() == 'fim':
        print(f'Progama encerrado. Boa sorte.')
        break
    telefone = input("Insira o telefone do cliente (máximo 11 caracteres): ")
    # Validação do telefone
    while len(telefone) !=11:
        telefone = input("Telefone inválido! Insira o telefone do cliente (máximo 11 caracteres): ")
    endereco = input("Insira o endereço do cliente: ")
    # Armazenar dados do cliente nas listas
    nomes += [nome]
    telefones += [telefone]
    enderecos += [endereco]
    

# Realizar o sorteio
if nomes:
    indice_sorteado = random.randint(0, len(nomes) - 1)
    print("Cliente sorteado:")
    print(f"Nome: {nomes[indice_sorteado]}")
    print(f"Telefone: {telefones[indice_sorteado]}")
    print(f"Endereço: {enderecos[indice_sorteado]}")
