def is_valid(a):
    while True:
        if a.lower() in 'ed':
            return a
        else:
            a = input('Please type correct: ')
            continue


# Зашифровать текст
def encrypt(text):
    text_list = list(text)
    upper_en_list = list(upper_eng_alphabet)
    lower_en_list = list(lower_eng_alphabet)
    upper_rus_list = list(upper_rus_alphabet)
    lower_rus_list = list(lower_rus_alphabet)


    if text_list[0] in upper_eng_alphabet or text_list[0] in lower_eng_alphabet:
        for i in range(len(text_list)):
            if text_list[i].isupper():
                for j in range(len(upper_en_list)):
                    if text_list[i] == upper_en_list[j]:
                        text_list[i] = upper_en_list[(j + sdv) % len(upper_en_list)]
                        break
            elif text_list[i].islower():
                for j in range(len(lower_en_list)):
                    if text_list[i] == lower_en_list[j]:
                        text_list[i] = lower_en_list[(j + sdv) % len(lower_en_list)]
                        break


    if text_list[0] in upper_rus_alphabet or text_list[0] in lower_rus_alphabet:
        for i in range(len(text_list)):
            if text_list[i].isupper():
                for j in range(len(upper_rus_list)):
                    if text_list[i] == upper_rus_list[j]:
                        text_list[i] = upper_rus_list[(j + sdv) % len(upper_rus_list)]
                        break
            elif text_list[i].islower():
                for j in range(len(lower_rus_list)):
                    if text_list[i] == lower_rus_list[j]:
                        text_list[i] = lower_rus_list[(j + sdv) % len(lower_rus_list)]
                        break


    text = ''.join(text_list)
    print(text)

# Дешифровать текст
def decrypt(text):
    text_list = list(text)
    upper_en_list = list(upper_eng_alphabet)
    lower_en_list = list(lower_eng_alphabet)
    upper_rus_list = list(upper_rus_alphabet)
    lower_rus_list = list(lower_rus_alphabet)


    if text_list[0] in upper_eng_alphabet or text_list[0] in lower_eng_alphabet:
        for i in range(len(text_list)):
            if text_list[i].isupper():
                for j in range(len(upper_en_list)):
                    if text_list[i] == upper_en_list[j]:
                        text_list[i] = upper_en_list[(j - sdv) % len(upper_en_list)]
                        break
            elif text_list[i].islower():
                for j in range(len(lower_en_list)):
                    if text_list[i] == lower_en_list[j]:
                        text_list[i] = lower_en_list[(j - sdv) % len(lower_en_list)]
                        break


    if text_list[0] in upper_rus_alphabet or text_list[0] in lower_rus_alphabet:
        for i in range(len(text_list)):
            if text_list[i].isupper():
                for j in range(len(upper_rus_list)):
                    if text_list[i] == upper_rus_list[j]:
                        text_list[i] = upper_rus_list[(j - sdv) % len(upper_rus_list)]
                        break
            elif text_list[i].islower():
                for j in range(len(lower_rus_list)):
                    if text_list[i] == lower_rus_list[j]:
                        text_list[i] = lower_rus_list[(j - sdv) % len(lower_rus_list)]
                        break


    text = ''.join(text_list)
    print(text)

choic = input('шифрование = e, дешифрование = d: ')
sdv = int(input('Сколько нужно сдвигнуть: '))
text = input('Напишите свой текст: ')

upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

if is_valid(choic) == 'e':
    encrypt(text)
else:
    decrypt(text)
