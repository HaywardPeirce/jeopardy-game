import json
import random, configparser

#list of jeopardy categories that have already been played
playedCategories = []

#read in the cofig file
config = configparser.ConfigParser()
config.read('config.ini')


#where is the questionfile located
questionFile = config['GENERAL']['questionFile']

#return a python list of questions
def readInQuestions():
    
    returnDict = {}
    
    with open(questionFile) as json_data:
        questionData = json.load(json_data)
        #print(type(questionData))
        #print(questionData[1])
        
        #loop through each of the questions in the data file
        for entry in questionData:
            
            tempDict = {}
            
            tempDict['category'] = entry['category']
            tempDict['air_date'] = entry['air_date']
            tempDict['question'] = entry['question']
            tempDict['value'] = entry['value']
            tempDict['answer'] = entry['answer']
            tempDict['round'] = entry['round']
            tempDict['show_number'] = entry['show_number']
            
            #check whether there is already a category called `entry['category']` in tempDict
            if returnDict.get(entry['category']):
                print('it already exists')
                #add the question of value `entry['value']` to the dictionary `entry['category']`
                returnDict[entry['category']][entry['value']] = tempDict
                
            else: 
                print('it doesnt exist yet')
                
                returnDict[entry['category']] = {}
                
                #add the question of value `entry['value']` to the dictionary `entry['category']`
                returnDict[entry['category']][entry['value']] = tempDict
                

                
        
    return returnDict


#a python dictionary of all the questions
#TODO: do I need to pass in questionFile?
questionDict = readInQuestions()

print(questionDict)

#questionListLen = len(questionList)


#TODO: create object for player and game to keep track of stats, questions, and scores

class Game(object):
    # Point class for the game being played.
    turn = 0
    players = 0
    pickedQuestions = []

    def __init__(self, turn, players, pickedQuestions):
        self.turn = turn
        self.players = players
        self.pickedQuestions = pickedQuestions
        
class Player(object):
    # Point class for the player of a game.
    score = 0

    def __init__(self, score):
        self.score = score


#clear out the old game data
def newGame():
    print('hello world')

#function called when a new turn is started, returns the question to be asked
def getNewQuestion():
    #get the next non-picked question
    nextQuestionIndex = pickQuestion(game.pickedQuestions)

    #select the next question based on it's index
    question = questionList[nextQuestionIndex]
    
    #add this question to the list of already asked questions
    game.pickedQuestions.append(nextQuestionIndex)

    return question

#returns the index of the question to be asked
def pickQuestion(exclude):
    r = None
    #loop until the random number that is picked is not a question that has laready been selected.
    while r in exclude or r is None:
         r = random.randrange(0,(questionListLen-1))
    return r



def playGame(session, gameInput):
    
    #
    if not session['questions']:
        session['questions'] = readInQuestions()
        
    return session
        
    

def main():
    #time.sleep(delay)
    
    #start a new game
    #game = Game(0,0,[])
    
    #setup list of playes based on config
    #for player in config['GENERAL']['questionFile']
    print("hello wprl")

if __name__ == '__main__':
    main()
