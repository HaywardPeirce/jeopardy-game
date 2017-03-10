import json
import ramdom

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
