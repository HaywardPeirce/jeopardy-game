import json
import random

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

questionFile = config['GENERAL']['questionFile']

#a python dictionary of all the questions
questionList = readInQuestions()

questionListLen = len(questionList)

#todo create object for player and game to keep track of stats, questions, and scores
class Game:
    # Point class for the game being played.

    def __init__(self):
        self.turn = 0
        self.players = 0
        self.pickedQuestions = []

class Player:
    # Point class for the player of a game.

    def __init__(self):
        self.score = 0

game = Game()

#function that keeps track of the game
def game():
    print('hello world')
#clear out the old game data
def newGame():
    print('hello world')

#function called when a new turn is started, returns the question to be asked
def getNewQuestion():
    nextQuestionIndex = pickQuestion()

    #select the next question based on it's index
    question = questionList[nextQuestionIndex]
    game.pickedQuestions.append(nextQuestionIndex)

    return question

#returns the index of the question to be asked
def pickQuestion(exclude):
    r = None
    #loop until the random number that is picked is not a question that has laready been selected.
    while r in exclude or r is None:
         r = random.randrange(0,(questionListLen-1))
    return r

#return a python list of questions
def readInQuestions():
    with open(questionFile) as json_data:
        questionData = json.load(json_data)
        #print(type(questionData))
        #print(questionData[1])
    return questionData

def main():
    time.sleep(delay)

if __name__ == '__main__':
    main()
