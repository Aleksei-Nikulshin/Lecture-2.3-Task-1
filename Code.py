
# Нужно реализовать Польскую нотацию для двух положительных чисел. Реализовать нужно будет следующие операции:

# Сложение
# Вычитание
# Умножение
# Деление
# Например, пользователь вводит: + 2 2 Ответ должен быть: 4

def main():

    print \
        ('Вы можете использовать следующие операции для двух положительных чисел: \nСложение\nВычитание\nУмножение\nДеление')
    print()

    inp = input \
        ('Введите знак операции и положительные значения для двух чисел\n согласно правилам Польской нотации, разделяя каждый элемент пробелом ')
    inp = inp.split(' ')
    # print(inp)
    # print(type(inp))


    inp_str = list(filter(None, inp))
    # print(inp_str)
    # print(len(inp_str))


    stack = 0

    if len(inp_str) != 3:
        print('Вы ввели данные неверно')
    else:
        try:
            for i in inp_str:
                if i == '-':
                    stack = int(inp_str[1]) - int(inp_str[2])
                    print(f'\nРезультат равен {stack}')
                    break
                elif i == '*':
                    stack = int(inp_str[1]) * int(inp_str[2])
                    print(f'\nРезультат равен {stack}')
                    break
                elif i == '/':
                    stack = int(inp_str[1]) / int(inp_str[2])
                    print(f'\nРезультат равен {stack}')
                    break
                elif i == '+':
                    stack = int(inp_str[1]) + int(inp_str[2])
                    print(f'\nРезультат равен {stack}')
                    break
                elif int(i) == int(i):
                    print("Вы ввели данные не по правилам Польской нотации")
                    break
        except ValueError:
            print('Вы ввели неверный знак операции')


main()



