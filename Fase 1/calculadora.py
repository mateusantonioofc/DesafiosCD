while True:
    num1 = float(input("Digite um numero => "))
    num2 = float(input("Digite outro numero => "))
    op = input("Operacao (+, -, *, /) => ").lower()

    if op == "+":
        print(f'soma: {num1 + num2}')
    elif op == "-":
        print(f'subtracao: {num1 - num2}')
    elif op == "*":
        print(f'multiplicacao: {num1 * num2}')
    elif op == "/":
        if num2 != 0: 
            print(f'divisao: {num1 / num2}')
        else:
            print("Nao pode dividir por 0")
    else:
        print("Hello World")
