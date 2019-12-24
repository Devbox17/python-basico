real = float(input('Quanto dinheiro você tem na carteira?: R$'))
dolar = 3.27
resultado = real / dolar

print('Com R${} você pode comprar US${:.2f}'.format(real, resultado))

# Usando Regra de Três
# US$ 1 --> R$ 3.27
# US$ x --> R$ 19.88
# x = 19.88 / 3.27