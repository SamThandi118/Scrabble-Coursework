# Sam Thandi 20/11/2020 coursework
# Referred to so the score for the letters/words can be worked out.
scoreFile = open("Scores.txt")
scoreList = []
for line in scoreFile:
    # splits the line into 2 and sub lists EG ['A','1']
    line = line.split()
    # line 0 refers to the A in my example (the first variable)
    letter = line[0]
    # line 1 refers to the score of 1 in my example (the second variable)
    score = int(line[1])
    scoreList.append([letter,score])
scoreFile.close()
# The word the user uses to calculate the score of the word
word = input("Please enter a word: ")
def getLetterScore(letter):
    for item in scoreList:
    # If item[0] (the letter) = a letter in scoreList return the next item in the list (the score of the letter)
        if item[0] == letter.upper():
            return item[1]

def getWordScore(word):
    letterTotal = 0
    for letter in word:
        # Adds the output of letterScore to letterTotal
        letterTotal = letterTotal + getLetterScore(letter)
    return letterTotal
print (getWordScore(word))