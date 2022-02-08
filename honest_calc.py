msgs = ["Enter an equation", "Do you even know what numbers are? Stay focused!", "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...", "Do you want to store the result? (y / n):", "Do you want to continue calculations? (y / n):",
        " ... lazy", " ... very lazy", " ... very, very lazy", "You are",
        "Are you sure? It is only one digit! (y / n)", "Don't be silly! It's just one number! Add to the memory? (y / n)", 
        "Last chance! Do you really want to embarrass yourself? (y / n)"]


def calculation(oper, x, y):
    if oper == '+':
        return x + y, True
    elif oper == '-':
        return x - y, True
    elif oper == '*':
        return x * y, True
    else:
        if y == 0:
            print(msgs[3])
            return 0, False
        else:
            return x / y, True


def is_one_digit(v):
    if 10 > v > - 10 and isinstance(v, int):
        return True
    return False


def check(v1, v2, v3):
    msg = ''
    if (is_one_digit(v1) and is_one_digit(v2)) or v1 == v2:
        msg += msgs[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msgs[7]
    if (v1 == 0 or v2 == 0) and (v3 in ['*', '+', '-']):
        msg += msgs[8]
    if msg != '':
        msg = msgs[9] + msg
        print(msg)


def check_operation(oper, x, y):
    if oper in ['+', '-', '*', '/']:
        check(x, y, oper)
        return calculation(oper, x, y)
    else:
        print(msgs[2])


def check_m(string, memory):
    if string == 'M':
        return str(memory)
    return string


def check_number(number):
    breaking = number.partition('.')
    if breaking[0].isnumeric() and breaking[1] == '.' and breaking[2].isnumeric():
        if float(number) - int(breaking[0]) == 0:
            return int(breaking[0]), True
        else:
            return float(number), True
    elif breaking[0].isnumeric() and breaking[1] == breaking[2] == '':
        return int(number), True
    else:
        return number, False


def additional_actions(result):
    if is_one_digit(result):
        msg_index = 10
        while True:
            print(msgs[msg_index])
            user = input()
            if user == 'y':
                if msg_index < 12:
                    msg_index += 1
                else:
                    return result
            elif user == 'n':
                return 0
    else:
        return result


def store_results(result):
    while True:
        print(msgs[4])
        answer = input()
        if answer == 'y':
            return additional_actions(result)
        elif answer == 'n':
            return 0


def continuation():
    while True:
        print(msgs[5])
        answer = input()
        if answer == 'y':
            return
        elif answer == 'n':
            exit()


def main():
    memory = 0
    while True:
        print(msgs[0])
        calc = input().split()

        x = calc[0]
        oper = calc[1]
        y = calc[2]

        x = check_m(x, memory)
        y = check_m(y, memory)

        x, result_x = check_number(x)
        y, result_y = check_number(y)

        if result_x is False or result_y is False:
            print(msgs[1])
        else:
            result, condition = check_operation(oper, x, y)
            if condition:
                print(float(result))
                memory += store_results(result)
                continuation()


main()
