# Sam Thandi 20/11/2020 coursework

scoreFile = open("Scores.txt")
scoreList = []
for line in scoreFile:
    # splits the line into 2 and sub lists EG ['A','1']
    line = line.split()
    # line 0 refers to the A (the first variable)
    letter = line[0]
    # line 1 refers to the score of 1 (the second variable)
    score = int(line[1])
    scoreList.append([letter,score])
scoreFile.close()

def getLetterScore():
    letter = input("Enter letter ")
    for item in scoreList:
        if item[0] == letter.upper():
           print("the score is", item[1])
getLetterScore()