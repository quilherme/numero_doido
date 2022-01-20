print ('Bem-vindo ao Número Doido')

numero_doido = 26

chute_do_usuario = input ('escolha um número de 1 a 30:')
print ('você escolheu o número doido', chute_do_usuario, end = '.')
chute_do_usuario_int = int (chute_do_usuario)

chute_certo = numero_doido == chute_do_usuario_int
chute_maior = numero_doido < chute_do_usuario_int
chute_menor = numero_doido > chute_do_usuario_int

if (chute_certo):
    print ('\nParabéns, você acertou!')
else:
    if (chute_maior):
        print ('\n Vixi, você chutou um número maior que o esperado')
    elif (chute_menor):
        print('\n Vixi, você chutou um número menor que o esperado')