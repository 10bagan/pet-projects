import random
import string

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
EXCON = 'il1Lo0O'

chars_list = []

def pass_gen(a, b):
    for i in range(int(a)):
        chars = ''
        while len(chars) != int(b):
            chars += random.choice(random.choice(chars_list))
        if bool(int(input('Исключать неоднозначные символы {}? 1 - Да, 0 - Нет '.format(EXCON)))): 
            for i in chars:
                if i in EXCON:
                    chars = chars.replace(i, '')    
        print(chars)

cntPw = input('Укажите количество паролей для генерации:')
lenPw = input('Укажите длину одного пароля:')

if bool(int(input('Включать цифры {}? 1 - Да, 0 - Нет '.format(DIGITS)))): 
    chars_list.append(tuple(string.digits))

if bool(int(input('Включать прописные буквы {}? 1 - Да, 0 - Нет '.format(UPPERCASE_LETTERS)))):
    chars_list.append(tuple(string.ascii_uppercase))

if bool(int(input('Включать строчные буквы {}? 1 - Да, 0 - Нет '.format(LOWERCASE_LETTERS)))): 
    chars_list.append(tuple(string.ascii_lowercase))

if bool(int(input('Включать символы {}? 1 - Да, 0 - Нет '.format(PUNCTUATION)))): 
    chars_list.append(tuple(string.punctuation))

pass_gen(cntPw, lenPw)