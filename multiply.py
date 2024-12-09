def multiply_numbers(number1, number2, number3):
    return int(number1) * int(number2) * int(number3)

if __name__ == "__main__":
    number1 = input("Введите первое число: ")
    number2 = input("Введите второе число: ")
    number3 = input("Введите третье число: ")
    number_product = multiply_numbers(number1, number2, number3)
    print(number_product)