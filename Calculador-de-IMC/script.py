print('Oi, me diga qual é o seu nome: ')
nome = input()
print('Quantos quilos você tem (no formato **.**): ')
peso = input()
print('Agora me diz qual é sua altura (no formato *.**): ')
altura = input()

imc = float(peso) / (float(altura) ** float(2))

print(f'{nome}, o seu eu IMC é de {imc:.2f}.')

if imc < 16:
    print(f'Você está em estado de magreza de grau grave, procure um especialista imediatamente.')
elif imc < 17:
    print(f'Você está em estado de magreza de grau moderado.')
elif imc < 18.5:
    print(f'Você está em estado de magreza de grau leve.')
elif imc < 25:
    print(f'Você está saudável.')
elif imc < 30:
    print(f'Você está com sobrepeso, recomendo que faça a realização de atividades física, como caminhada por exemplo e que procure a ajuda de um especialista.')
elif imc < 35:
    print(f'Você está em situação de sobrepeso de grau 1, procure um especialista.')
elif imc < 40:
    print(f'Você está em situação obesidade grave de grau 2, procure um especialista o mais rápido possível!')
else:
    print(f'Você está em situação obesidade grave de grau 3, procure um especialista o mais rápido possível!')
