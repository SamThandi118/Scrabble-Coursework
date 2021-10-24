# Sam Thandi 20/11/2020 coursework
# Creates a dictionary variable that opens the file Dictionary.txt
dictionary = open("Dictionary.txt")
dictionaryList = []
for line in dictionary:
    # for the amount of lines in dictionary, strip the end of it. This removes any white space and /n's in the txt
    line = line.strip()
    dictionaryList.append(line)
dictionary.close()

def onlyEnglishLetters(word):
    usersWord = word
    # .isalpha checks to see if the input is in the alphabet. If yes then returns True, if not returns False
    usersWordCheck = usersWord.isalpha()
    return(usersWordCheck)

def wordInTiles(word, myTiles):

    word = word.upper()
    for x in word:
        # Negative check, if the letter is not in myTiles, return False I.E word cannot be created
        # OR if there are more letters (x)'s in the word than tiles, return False
        if x.upper() not in myTiles or word.count(x) > myTiles.count(x):
            return False
    print("Your word is valid ")
    return True

def isValid(word, myTiles, dictionaryList):
    # Runs through both functions in task 2 and 5, checks to see if using letters and if the word can be created
    if onlyEnglishLetters(word) == True and wordInTiles(word, myTiles) == True:
        # If word was letters and could be created with given tiles, check if the word is in the dictionary
        if word in dictionaryList:
            return True
        else:
            print("Not in the dictionary")
            return False
    else:
        print("Your word is either not English or cannot be created with the given tiles")
        return False

myTiles = ['T', 'Y', 'S', 'E', 'U', 'W', 'I']
word = input("Input your given word please: ")
word = word.upper()

isValid(word, myTiles, dictionaryList)