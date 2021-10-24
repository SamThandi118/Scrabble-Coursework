# Sam Thandi 20/11/2020 coursework

def onlyEnglishLetters(word):
    usersWord = word
    # .isalpha checks to see if the input is in the alphabet. If yes then returns True, if not returns False
    usersWordCheck = usersWord.isalpha()
    print(usersWordCheck)
word = input("Enter a word: ")
onlyEnglishLetters(word)