print('Hello, Django girls!')
if 3 > 2:
    print('Funciona!')
if 5 > 2:
    print('5 é maior que 2')
else:
    print('5 não é maior que 2')
name = 'Sonja'
if name == 'Ola':
    print('Olá Ola!')
elif name == 'Sonja':
    print('Olá Sonja!')
else:
    print('Olá estranho!')
volume = 57
if volume < 20:
    print("Está um pouco baixo")
elif 20 <= volume < 40:
    print("Está bom para música ambiente")
elif 40 <= volume < 60:
    print("Perfeito, posso ouvir todos os detalhes")
elif 60 <= volume < 80:
    print("Ótimo para festas!")
elif 80 <= volume < 100:
    print("Está muito alto!")
else:
    print("Meus ouvidos doem! :(")
if volume < 20 or volume > 80:
    volume = 50
    print("Bem melhor!")
def oi():
    print('olá!')
    print('Tudo bem?')

oi()
def oi(nome):
    if nome == 'Ola':
        print("Olá Ola!")
    elif nome == 'Sonja':
        print('Olá Sonja!')
    else:
        print('Olá estranho!')

oi("Ola")
oi("Sonja")
oi("Janine")
def oi(name):
    print('Olá ' + name + '!')

oi("Rachel")
def oi(nome):
    print('Oi ' + nome + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Voce']
for name in girls:
    oi(name)
    print('Próxima')
for i in range(1, 6):
    print(i)
