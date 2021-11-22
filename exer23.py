# A digitação do número

num = int(input('Informe um número de 0 a 9999: '))
print('Analisando o número {}:'.format(num))

# Sua unidade
u = num // 1 % 10
print('Unidade: {}'.format(u))

# Sua dezena
d = num // 10 % 10
print('Dezena: {}'.format(d))

# Sua centena
c = num // 100 % 10
print('Centena: {}'.format(c))

# E seu milhar
m = num // 1000 % 10
print('Milhar: {}'.format(m))
