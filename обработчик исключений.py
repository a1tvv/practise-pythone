while True:
    try:
        x = int(input('Введите число: '))
        x -=998
        print('Ваш IQ равен: ', x)
        break
    except ValueError:
        print('Введите лучше число! ')