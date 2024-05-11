import random

print("Добро пожаловать в числовую угадайку")


def get_random_number(d1, d2):
    return random.randint(d1, d2)


def is_diapazon(x, y):  # Определение границ диапозона
    if x > y:           # если начальная граница больше конечной, то свапаем с конечной
        x, y = y, x
        return x, y
    else:
        return x, y

def is_valid(num, a, b):      # тест на то, чтобы определить что это, если это цифра то ретурн
    return num.isdigit() and float(num) - int(num) == 0 and a < int(num) < b

def continue_game(word):
        while word not in 'ДдНн':
            word = input('Можете написать корректно? д = да / н = нет: ')
        else:
            if word in 'Дд':
                game()
            else:
                print('До следующей встречи! Пока!')

def game():
    total = 0
    x, y = int(input("Введите начало диапозона: ")), int(input("Введите конец диапозона: "))
    a, b = is_diapazon(x, y)
    r = random.randint(a, b)
    n = input("Для начала, попробуй угадать число. Введите свое предположение: ")
    while is_valid(n, a, b):
        if int(n) > r:
            n = input("Слишком много, попробуйте еще раз: ")
            total += 1
            continue
        elif int(n) < r:
            n = input("Слишком мало, попробуйте еще раз: ")
            total += 1
            continue
        else:
            print(f"Вы угадали, поздравляем! Вы потратили {total} попыток на угадывание числа.")
            continue_game(input("Следующая игра? д = да / н = нет: ")) # если пользователь хочет продолжит игру
            break

game()