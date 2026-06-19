# cnpj_base = "608774800001"  # 12 primeiros dígitos
cnpj_base = "111111111111"  # 12 primeiros dígitos

# ==========================
# Primeiro dígito verificador
# ==========================
pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

soma_1 = 0

print("Cálculo do 1º dígito:\n")

for numero, peso in zip(cnpj_base, pesos_1):
    produto = int(numero) * peso
    soma_1 += produto
    print(f"{numero} × {peso} = {produto}")

resto_1 = soma_1 % 11

if resto_1 < 2:
    digito_1 = 0
else:
    digito_1 = 11 - resto_1

print(f"\nSoma = {soma_1}")
print(f"Resto da divisão por 11 = {resto_1}")
print(f"1º dígito = {digito_1}")

# ==========================
# Segundo dígito verificador
# ==========================
cnpj_13 = cnpj_base + str(digito_1)

pesos_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

soma_2 = 0

print("\n\nCálculo do 2º dígito:\n")

for numero, peso in zip(cnpj_13, pesos_2):
    produto = int(numero) * peso
    soma_2 += produto
    print(f"{numero} × {peso} = {produto}")

resto_2 = soma_2 % 11

if resto_2 < 2:
    digito_2 = 0
else:
    digito_2 = 11 - resto_2

print(f"\nSoma = {soma_2}")
print(f"Resto da divisão por 11 = {resto_2}")
print(f"2º dígito = {digito_2}")

# ==========================
# Resultado final
# ==========================
cnpj_completo = cnpj_base + str(digito_1) + str(digito_2)

print(f"\nCNPJ válido: {cnpj_completo}")