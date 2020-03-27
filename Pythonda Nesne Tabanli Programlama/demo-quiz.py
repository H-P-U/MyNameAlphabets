#Question
class Question:
    def __init__(self, text, choices, answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self, answer):
        return self.answer == answer
q1= Question('En iyi pogramlama dili hangisidir?', ['c#', 'python','javascript','java'] , 'python')
q2= Question('En popüler pogramlama dili hangisidir?', [ 'python','javascript','c#','java'], 'python')
q3= Question('En çok kazandıran pogramlama dili hangisidir?', ['c#', 'javascript','java','python'] , 'python')
liste=[q1,q2,q3]
#print(q1.checkAnswer('python'))
#print(q2.checkAnswer('c#'))
#Quiz

class Quiz:
    def __init__(self, questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    def getQuestions(self):
        return self.questions[self.questionIndex]
    def displayQuestions(self):
        question=self.getQuestions()
        print(f'Soru {self.questionIndex+1}: {question.text}')

        for q in question.choices:
            print('-'+q)

        answer= input('Cevabınız:')
        self.guess(answer)
        self.LoadQuestions()
    def guess(self,answer):
        question= self.getQuestions()
        if question .checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1


    def LoadQuestions(self):
        if len(self.questions)== self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestions()

    def displayProgress(self):
        totalQuestions= len(self.questions)
        questionNumber= self.questionIndex + 1

        if questionNumber > totalQuestions:
             print('Quiz Bitti')
        else:
             print(f'Question number {questionNumber} of {totalQuestions}'.center(100, '*'))

    def showScore(self):
        print(f'score: {self.score}')

q1= Question('En iyi pogramlama dili hangisidir?', ['c#', 'python','javascript','java'] , 'python')
q2= Question('En popüler pogramlama dili hangisidir?', [ 'python','javascript','c#','java'], 'python')
q3= Question('En çok kazandıran pogramlama dili hangisidir?', ['c#', 'javascript','java','python'] , 'python')
q4= Question('En çok sevilen pogramlama dili hangisidir?', ['c#', 'javascript','java','python'] , 'python')
q5= Question('En kolay pogramlama dili hangisidir?', ['c#', 'javascript','java','python'] , 'python')
questions=[q1,q2,q3,q4,q5]

quiz=Quiz(questions)
question=quiz.getQuestions()
quiz.LoadQuestions()

