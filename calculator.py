operators = ['+', '-', '*', '/']
answer = 0


def multiply(first_num, second_num):
    return first_num * second_num


def divide(first_num, second_num):
    return first_num / second_num


def subtract(first_num, second_num):
    return first_num - second_num


def add(first_num, second_num):
    return first_num + second_num


while True:
    first_operand = float(input('What is the first number?\n'))

    while True:
        selected_operator = input('+\n-\n*\n/\nPick an operation:\n')

        if selected_operator in operators:
            second_operand = float(input('What is the next number?\n'))
            if selected_operator == '*':
                answer += multiply(first_operand, second_operand)
                print(
                    f'{first_operand} {selected_operator} {second_operand} = {answer}')
                break
            elif selected_operator == '/':
                answer += divide(first_operand, second_operand)
                print(
                    f'{first_operand} {selected_operator} {second_operand} = {answer}')
                break
            elif selected_operator == '-':
                answer += subtract(first_operand, second_operand)
                print(
                    f'{first_operand} {selected_operator} {second_operand} = {answer}')
                break
            elif selected_operator == '+':
                answer += add(first_operand, second_operand)
                print(
                    f'{first_operand} {selected_operator} {second_operand} = {answer}')
                break
        else:
            print('Invalid selection, try again\n')

    while True:
        first_operand = answer
        user_restart = input(
            f'Type "y" to continue calculating with {answer}, or type "n" to start a new calculation\n')

        if user_restart == 'y':
            while True:
                selected_operator = input('+\n-\n*\n/\nPick an operation:\n')
                second_operand = float(input('What is the next number?\n'))

                if selected_operator in operators:
                    if selected_operator == '*':
                        answer = multiply(first_operand, second_operand)
                        print(
                            f'{first_operand} {selected_operator} {second_operand} = {answer}')
                        break
                    elif selected_operator == '/':
                        answer = divide(first_operand, second_operand)
                        print(
                            f'{first_operand} {selected_operator} {second_operand} = {answer}')
                        break
                    elif selected_operator == '-':
                        answer = subtract(first_operand, second_operand)
                        print(
                            f'{first_operand} {selected_operator} {second_operand} = {answer}')
                        break
                    elif selected_operator == '+':
                        answer = add(first_operand, second_operand)
                        print(
                            f'{first_operand} {selected_operator} {second_operand} = {answer}')
                        break
                else:
                    print('Invalid selection, try again\n')

        elif user_restart == 'n':
            break
        else:
            print('Invalid selection, try again\n')
