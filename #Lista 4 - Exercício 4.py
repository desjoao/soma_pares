#Lista 4 - Exercício 4

soma = 0
for i in range (85, 908):
    if i%2==0:
        print(i)
        soma += i
print(f'\nA soma de todos os números pares compreendidos entre 85 e 907 é de: {soma}')
