#-------------------------------------------------------------------------------
# Name:        HangMan
# Purpose:
#
# Author:      Andrew Robinovich
#
# Created:     12.09.2021
# Copyright:   (c) Andrew Robinovich 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''','''
+---+
0   |
    |
    |
   ===''','''

+---+
0   |
|   |
    |
   ===''','''

 +---+
 0   |
/|   |
     |
    ===''','''

 +---+
 0   |
/|\  |
     |
    ===''','''

 +---+
 0   |
/|\  |
/    |
    ===''','''

 +---+
 0   |
/|\  |
/ \  |
    ===''']

words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лосось лось лягушка медведь моллск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель харек черепаха ястреб ящерица'.split()

def getRandomWord(wordList):
    # Возвращаем  случайную строку из переданного списка
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы: ', end = '')
    for letter in missedLetters:
        print(letter, end = '')
    print()

    blanks= '_'*len(secretWord)

    for i in range(len(secretWord)): #Заменяем пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #Показываем секретное слово с пробелами между буквами
        print(letter, end='')
    print()

def getGuess(alreadGuessed):
 # Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) !=1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadGuessed:
            print('Вы уже указывали эту букву. Введите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчщъыьэюя':
            print('Пожалуйста, введите БУКВУ!')
        else:
            return guess

def playAgain():
    # Возвращаем True, если игрок хочет сыграть заново; в противном случае возвращаем False
    print('Хотите сыграть еще? (да или нет')
    return input().lower().startswith('д')

print('В И С И Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone =  False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    #позволяет игроку ввести букву
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # проверяем выйграл ли игрок
        founAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                founAllLetters = False
                break
        if founAllLetters:
            print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        # проверяем превышен ли лимит попыток и проиграл
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            #print('Вы исчерпали все попытки!\n Не угадано букв: ' +str(len(missedLetters))+ ' и угадано букв: ' + str(len(correctLetters) + '. Было загадано слово: "' + str(secretWord)))
            print('Вы исчерпали все попытки!')
            print('Не угадано букв: ' +str(len(missedLetters)))
            print('Угадано букв: ' + str(len(correctLetters)))
            print('Было загадано слово: ' + str(secretWord))
            gameIsDone = True


    # Запрашиваем, хочет ли игрок сыграть заново (только, если игра завершена)

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break







def main():
    pass

if __name__ == '__main__':
    main()