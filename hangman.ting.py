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
    