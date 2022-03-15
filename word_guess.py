import random

# Pull a random word from words.txt file
def word():
    with open("words.txt", "r") as words:
        lines = words.readlines()
    wordList = []
    for word in lines:
        wordList.append(word.strip("\n"))
    
    gameWord = random.choice(wordList)
    return gameWord

# Main game function
def userChoice():
    count = 0
    gameWord = word()
    letterList = list(gameWord)
    userLetters = []
    letterBlanks = "*****"
    while True:
        try:
            userWord = input("What's your guess?: ")
            if userWord == "exit":
                exit()
            assert len(userWord) == 5
        except AssertionError:
            print("Word must be 5 letters long!")
            continue
        if userWord == gameWord:
            print("Correct!")
            break
        else:
            if count < 3:
                print(f"Wrong. {4 - count} tries remaining.")
            if count == 3:
                print("Wrong. 1 try remaining.")

            for i in letterList:
                if i in userWord:
                    if i not in userLetters:
                        userLetters.append(i)
                    letterBlanks.replace("*", i)
            for i in userLetters:
                letterIndex = gameWord.index(i)
                letterBlanks = replaceBlanks(letterBlanks, letterIndex, i.upper())
            if count < 4:
                print(letterBlanks)
        count += 1
        if count > 4:
            print(f"Wrong. You ran out of tries! The answer was {gameWord.upper()}!")
            break
    # Allow users the opportunity to play again
    playAgain = input("Play again? (y/n): ")
    if playAgain == "y":
        userChoice()
    else:
        quit()

# Function to replace blanks with correctly guessed letters
def replaceBlanks(blank, index, replacement):
    return "%s%s%s"%(blank[:index], replacement, blank[index+1:])


userChoice()