# Sam Thandi 20/11/2020 coursework
# Creates a score variable that opens the file Scores.txt
score = open("Scores.txt")
# Makes a list to append (add) the contents of 'score' later in the code.
scoreList = []
for line in score:
    # for the amount of lines in score, strip the end of it. This removes any white space and /n's in the txt
    line = line.strip()
    # adds the content of line (referenced in line 8) to scoreList (line 5) until the text document runs out of lines
    scoreList.append(line)
score.close()


#DICTIONARY
# Creates a dictionary variable that opens the file Dictionary.txt
dictionary = open ("Dictionary.txt")
dictionaryList = []
for line in dictionary:
    # for the amount of lines in dictionary, strip the end of it. This removes any white space and /n's in the txt
    line = line.strip()
# adds the content of line (referenced in line 20) to dictionaryList (line 17) until the text document runs out of lines
    dictionaryList.append(line)
dictionary.close()


#TILES
# Creates a tile variable that opens the file Tiles.txt
tiles = open ("Tiles.txt")
tileList = []
for line in tiles:
    # for the amount of lines in tiles, strip the end of it. This removes any white space and /n's in the txt
    line = line.strip()
# adds the content of line (referenced in line 32) to tileList (line 29) until the text document runs out of lines
    tileList.append(line)
tiles.close()
