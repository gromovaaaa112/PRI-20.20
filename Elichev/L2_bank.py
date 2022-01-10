# Пользователь делает вклад в размере 'x' рублей на 'y' лет под 'p'% годовых.
# Написать программу с пользовательским вводом суммы 'x', количества лет 'y' и процента 'p',
# которая будет выводить конечную сумму на конец расчетного периода.

def bank():
    x = float(input('Введите размер вклада: '))
    y = int(input('Введите срок вклада (в годах): '))
    p = float(input('Введите процент годовых: '))

    for i in range(y):
        x *= 1+(p/100)

    print(f'Конечная сумма: {x}')


if __name__ == '__main__':
    bank()
