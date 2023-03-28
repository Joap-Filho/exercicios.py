print('Exercicio 13: Calcular o peso ideal baseado na altura com distinção entre homens e mulheres')

#Solicitar sexo e altura do usuário 
sexo = str(input('Você é homem ou mulher: '))
h = float(input('Informe sua altura: '))

#Contas 
homem = (72.7 * h) - 58
mulher = (62.1 * h) - 44.7

#Se o usuário for homem
if ((sexo == 'homem') or (sexo == 'h') or (sexo == 'Homem') or (sexo == 'Masculino') or (sexo == 'masculino')):
    print(f'O peso ideal baseado na sua altura é igual a {homem: .2f}')

#Se o usuário for mulher
if ((sexo == 'mulher') or (sexo == 'Mulher') or (sexo == 'Feminino') or (sexo == 'feminino')or (sexo == 'F')):
    print(f'O peso ideal baseado na sua altura é igual a {mulher: .2f}')

