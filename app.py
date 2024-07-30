import os
restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False }, 
                {'nome': 'Japa', 'categoria': 'Japonesa', 'ativo': True}]

def exibir_nome_do_programa():
    print("""
        𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
        
        """)

def exibir_opcoes():
    print('1) Cadastrar restaurante')
    print('2) Listar restaurante')
    print('3) Alternar estado do restaurante')
    print('4) Sair\n')

def finalizar_app():
    #limpar o sistema com a importação da biblioteca os
    exibir_subtitulo('Encerrando o app')

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print (linha)
    print(texto)
    print(linha)
    print()

def cadastar_novo_restaurante():
    exibir_subtitulo('Cadastrando Restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante , 'categoria': categoria , 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes')

    print(f'{'Nome do restaurante'.ljust(23)} / {'Categoria'.ljust(20)} / Status' )
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} / {categoria_restaurante.ljust(20)} / {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja altear o estado: ')
    restante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f' O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi destivado com sucesso'
            print(mensagem) 
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')


    voltar_ao_menu_principal()
def escolher_opcao():
    try:
        opção_escolhida = int(input('Escolha uma opção: '))
        # print('Voce escolheu a opção', opção_escolhida)
        # print('Você escolheu a opção {}'.format(opção_escolhida))
        # print(f'Você escolheu a opção {opção_escolhida}')




        if opção_escolhida == 1:
            cadastar_novo_restaurante()
        elif opção_escolhida == 2:
            print('Listar Restaurante')
            listar_restaurantes()
        elif opção_escolhida == 3:
            alternar_estado_restaurante()
        elif opção_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()