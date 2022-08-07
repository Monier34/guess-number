import random

NumberToGuess = random.randint(1, 100)
UserGuess = -1

while UserGuess != NumberToGuess:
    UserGuess = int(input("Угадай число от 1 до 100"))
    if UserGuess > NumberToGuess:
        print("Число должно быть меньше!")
    elif UserGuess < NumberToGuess:
        print("Число должно быть  больше!")
    else:
        print("Вы угадали, этл число" + str(NumberToGuess))
    break
