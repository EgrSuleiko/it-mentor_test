def main ():
    result = calculator(*unpack_string(input()))
    print(result)


def unpack_string(str):
    if len(str.split()) != 3:
        raise ValueError('Cтрока не является математической операцией')

    num1, operator, num2 = str.split()

    if operator not in ['+', '-', '*', '/']:
        raise ValueError('Введена неверная операция')

    if not is_int_number(num1) or not is_int_number(num2):
        raise ValueError('Одно или несколько введенные значений не является целым числом')

    return int(num1), int(num2), operator


def is_int_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def calculator(num1, num2, operator):
    if num1 < 1 or num2 < 1:
        raise ValueError('Одно или несколько чисел меньше 1, что не удовлетворяет условиям задачи')

    if num1 > 10 or num2 > 10:
        raise ValueError('Одно или несколько чисел больше 10, что не удовлетворяет условиям задачи')

    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 // num2


main()
