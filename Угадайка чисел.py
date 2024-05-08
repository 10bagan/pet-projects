import random
import time

def is_valid(n):
    if 0 < n < 100:
        return True and n
    else:
        return False

def loop(number):
    if is_valid(number):
        start_time = time.time()
        while is_valid(number):
            if number > random_int:
                number = int(input("Слишком много, попробуйте еще раз: "))
                continue
            elif number < random_int:
                number = int(input("Слишком мало, попробуйте еще раз: "))
                continue
            else:
                end_time = time.time()
                print(f"Вы угадали, поздравляем! Вы потратили {int(end_time - start_time)} секунд на угадывание числа.")
                break
    else:
        number = int(input("Далбаеб, введи числа в диапозоне от 1 до 100: "))
        loop(number)
    

random_int = random.randint(1, 101)
print("Добро пожаловать в игру 'Угадай число'!")
print('Правила просты: я загадываю число от 1 до 100, а ты пытаешься отгадать его, предполагая число. Я буду говорить "слишком мало", "слишком много" или "верно", в зависимости от того, ближе твое предположение к загаданному числу или нет.')
print('Для начала, попробуй угадать число.Введите свое предположение:')

number = int(input())
loop(number)
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")