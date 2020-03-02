import random
WORDLIST = [""]
updatedWord = ""

def initialize():
    global updatedWord
    global SECRET
    WORDLIST = ['one','two','three','four','five','six','seven','eight','nine','ten']
    SECRET = random.choice(WORDLIST)
    updatedWord = [('_'*len(SECRET))]
   
    print(updatedWord)
    print SECRET

def getLetter():
    global letter
    letter = str(raw_input('ENTER YOUR GUESS: '))
    print ('YOUR GUESS: ' + letter)

def fillLetter():
    pos = SECRET.find(letter)
    updatedWord[pos] = letter
    
def ifWon():
    if updatedWord == SECRET:
        print ('You Won!')
    else: 
        getLetter()
        
def main():
    
    initialize()
    getLetter()






word = list("Howdy")
wordList = list(word.lower())
updatedSpaces = []
wordLen = len(word)
lives = 5
letter = " "

for i in range (0, int(word.en)):
    updatedSpaces.append("-")
    


def getLetter():
    global letter
    letter = raw_input("Which letter do you think is in the word")
    
def check():
    global updatesSpaces
    global lives
    global letter
    for x in range (0, int(word.en)):
        if letter == word[x]:
            updatesSpaces[x] = word[x]
            break
        else:
            lives -= 1
            if lives != 0:
                print(updatedSpaces)
                getLetter()
            else:
                print("Out of Lives. Game Over")
    

def game():
    getLetter()
    check()

game() 

