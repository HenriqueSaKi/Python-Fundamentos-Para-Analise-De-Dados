# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

# Funções da Calculadora
soma = lambda a, b : a + b
subtracao = lambda a, b : a - b
multiplicacao = lambda a, b : a * b
divisao = lambda a, b : a / b
resultado = 0

operacao = input("Digite a operacao que deseja realizar.\nO formato deve seguir o padrão apresentado a seguir: 'a + b'\nEntrada: ")

operacao.split(" ")

a = int(operacao[0])
b = int(operacao[4])

if(operacao[2] == "+"):
    print(soma(a, b))
elif(operacao[2] == "-"):
    print(subtracao(a, b))
elif(operacao[2] == "*"):
    print(multiplicacao(a, b))
elif(operacao[2] == "/"):
    print(divisao(a, b))
    