def math_operations():
    while True:
        try:
            x = input("Введите что нужно сосчитать: ")
            print(eval(x))
            break
        except ValueError:
            print("Неверно набран номер!")
