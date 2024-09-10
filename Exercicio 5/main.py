# Funcao para inverter uma string
def inverter_string(string):
    string_invertida = ""
    for s in string:
        string_invertida = s + string_invertida
    return string_invertida

# Entrada e saida de dados
string = input("Entre com uma string: ")
string_invertida = inverter_string(string)
print(f"String '{string}' invertida: '{string_invertida}'")