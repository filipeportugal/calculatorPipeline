from operations import arithmetic


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi("You")
    arithmetic.addition(3, 4)
    arithmetic.subtraction(3, 4)
    arithmetic.multiplication(3, 4)
    arithmetic.division(3, 4)
