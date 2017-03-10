import json
import random

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

questionFile = config['GENERAL']['questionFile']

#a python dictionary of all the questions
questionList = readInQuestions(questionFile)

#todo create object for player and game to keep track of stats, questions, and scores

#function that keeps track of the game
def game():
    print('hello world')
#clear out the old game data
def newGame():
    print('hello world')

#function called when a new turn is started
def getNewQuestion():
    nextQuestion = pickQuestion()

    #select the next question based on it's index
    question = questionList['questions'][nextQuestion]
    game.pickedQuestions.append(nextQuestion)

    return question

#returns the index of the question to be asked
def pickQuestion(exclude):
    r = None
    #loop until the random number that is picked is not a question that has laready been selected.
    while r in exclude or r is None:
         r = random.randrange(1,10)
    return r

#return a python dictionary of
def readInQuestions():
    with open(questionFile) as json_data:
        questionData = json.load(json_data)
        print(type(questionData))
        print(questionData[1])
