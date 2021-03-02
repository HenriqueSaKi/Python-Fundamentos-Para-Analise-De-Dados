# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

# Funções da Calculadora
soma = lambda a, b : a + b
subtracao = lambda a, b : a - b
multiplicacao = lambda a, b : a * b
divisao = lambda a, b : a / b

while(True):
    print("\n\n******************* Python Calculator *******************")
    print("Escolha uma das operações a seguir: ")
    operacao = int(input("1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n"))
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if operacao == 1:
        print("\n\nResultado: " + soma(num1, num2))
    elif operacao == 2:
        print("\n\nResultado: " + subtracao(num1, num2))
    elif operacao == 3:
        print("\n\nResultado: " + multiplicacao(num1, num2))
    elif operacao == 4:
        print("\n\nResultado: " + divisao(num1, num2))
    else:
        print("Opção inválida")