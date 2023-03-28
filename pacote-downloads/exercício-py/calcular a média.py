print('+' *20)
print('Exercício 4: Calcular a média')
print('+' *20)

nota1 = float(input('informe a primeira nota: '))
nota2 = float(input('informe a segunda nota: '))
nota3 = float(input('informe a terceira nota: '))
nota4 = float(input('informe a quarta nota: '))
nota5 = float(input('informe a quinta nota: '))
nota6 = float(input('informe a sexta nota: '))
nota7 = float(input('informe a sétima nota: '))
nota8 = float(input('informe a oitava nota: '))
Soma = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8) / 8

print('A nota final do aluno foi de', Soma)

if Soma >= 7: 
    print('O aluno passou')
else: 
    print('O aluno não passou')