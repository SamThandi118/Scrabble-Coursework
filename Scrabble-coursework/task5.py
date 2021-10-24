# Sam Thandi 20/11/2020 coursework
def wordInTiles(word, myTiles):
    # word has to be converted to upper as tiles are in capitals
    word = word.upper()
    # For each letter in word, run the loop
    for x in word:
        # Negative check, if the letter is not in myTiles, return False I.E word cannot be created
        # OR if there are more letters (x)'s in the word than tiles, return False
        if x.upper() not in myTiles or word.count(x) > myTiles.count(x):
            print("Your word cannot be created with the given tiles, try again")
            return False
    print("Your word is valid ")
    return True

myTiles = ['T', 'Y', 'S', 'E', 'U', 'W', 'I']
word = ("swet")

wordInTiles(word, myTiles)