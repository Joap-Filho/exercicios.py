print('+' *20)
print('Exercício 5: Conversor de metros para centímetros')
print('+' *20)

m = float(input('Informe um valor em metros: '))
cm = m * 100

if m > 0:
    if m == 1:
        print(m, 'metro é equivalente a ', cm, 'centímetros')
    elif m > 1:
        print(m, 'metros são equivalentes a ', cm, 'centímetros')
else:
    print('Informe um valor maior que zeroaisias')
