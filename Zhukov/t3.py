
# Придумайте как минимум 2 способа нахождения
# количества цифр в числе. Один из них не
# должен использовать строки, а основываться
# только на математических операторах и
# других конструкциях языка.

def main():
    #1st
    print('1)Колличество цифр в введеном числе с помощью функции len : ' + str(len(input())))

    #2nd
    num = int(input())
    count = 0
    while num > 0:
        num = num // 10
        count+=1
    print('2)Колличество цифр в введеном числе с помощтю деления :' + str(count))

if __name__ == '__main__':
  main()
