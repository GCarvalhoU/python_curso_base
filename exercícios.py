#O separador sep mostra como vocÊ quer que separe os elementos: 
print('a','b','c', sep='\n')

#--------------------
#Exibir o valor arredondado :2f.
pi = 3.14159
print(f'O valor arredondado de pi é: {pi:.2f}')
# Utilizando a função round() : print('O valor arredondado de pi é:', round(pi, 2))

#-------------------
#novo modelo para usar ao invés de if e else:
opcao_escolhida = int(input('Escolha uma opção: '))
match opcao_escolhida:
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case 3:
        print('Ativar restaurante')
    case 4:
        print('Finalizar app')
    case _:
        print('Opção inválida!')

#------------------
#Resto de divisão: %
print(4%2)
print(5%2)
#------------------