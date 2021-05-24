import random
guesses_made = 0
name = input(' Привет как тебяя зовут? \n ')
number = random.randint(1, 40)
print('Отлично, {0}, я загадала число между 1 и 40. Сможешь угадать?'.format(name))
while guesses_made < 6:
    guess = int(input('Введите число:'))
    guesses_made += 1
    if guess < number:
        print('Твое число меньше того, что я загадал.')
    if guess > number:
        break
if guess == number:
    print(' О ты {0} Ты угадал мое число использовав {1} попыток'.format(name , guesses_made))
else:
    print(' А вот и не угадал) Я загадал число {0}'.format(number))
