import random

word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо',
             'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец',
             'вид', 'система']

# Выбираем слово через функцию рандома
word = random.choice(word_list)
result = ['_' for _ in word]
count = 0
max_attempts = 10  # Максимальное количество попыток

# Проверка result
def won(result, word):
    if ''.join(result) == word:
        print("Вы выиграли!")
        print(''.join(result))
    else:
        print("Вы проиграли!")
        print(f"Загаданное слово было: {word}")

def game():
    global result
    global count
    while ''.join(result) != word and count < max_attempts:
        n = input("Введите букву: ").lower()
        if n.isalpha() and len(n) == 1:
            if n in word:
                print("Вы угадали букву!")
                for i in range(len(word)):
                    if word[i] == n:
                        result[i] = n
            else:
                print("Вы ошиблись!")
                count += 1
            print('Текущее состояние слова: ' + ''.join(result))
        else:
            print("Некорректный ввод")

    won(result, word)

game()
