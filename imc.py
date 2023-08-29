def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obeso"

# Solicitar entrada do usuário
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Calcular o IMC
imc_calculado = calcular_imc(peso, altura)

# Interpretar o IMC
classificacao = interpretar_imc(imc_calculado)

# Exibir resultado
print("Seu IMC é:", imc_calculado)
print("Classificação:", classificacao)
