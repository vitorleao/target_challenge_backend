# Função para inverter a string
def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# Solicitar ao usuário a entrada da string
entrada = input("Informe uma string para inverter: ")

# Inverter a string e exibir o resultado
resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")

