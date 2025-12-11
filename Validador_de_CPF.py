import re

# Validar CPF

def validar_cpf(cpf):
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return re.match(padrao, cpf) is not None

# Verificar CPF

def verificar_cpf(cpf):
    cpf_numeros = re.sub(r'[^\d]', '', cpf)

 # Cálculo do primeiro dígito verificador

    soma = 0 
    for i in range(9):
        soma += int(cpf_numeros[i]) * (10 - i) 
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto 


    soma = 0
    for i in range (10):
        soma += int(cpf_numeros [i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    return digito1 == int(cpf_numeros[9]) and digito2 == int(cpf_numeros[10])


def main():
    cpf = input('Digite um CPF: ')

    if validar_cpf(cpf):
        print('Formato válido!')
        if verificar_cpf(cpf):
            print('CPF VÁLIDO')
        else:
            print('CPF INVÁLIDO')
    else:
        print('Formato inválido!')
main()