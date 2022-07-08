print('Olá, me diga qual é o seu nome?')
nome = input()
print('Quantos quilos você tem (no formato **.**)?')
peso = input()
print('Agora me diz qual é sua altura (no formato *.**):')
altura = input()

imc = float(peso) / (float(altura) ** float(2))

print(f'{nome}, o seu eu IMC é de {imc:.2f}')
