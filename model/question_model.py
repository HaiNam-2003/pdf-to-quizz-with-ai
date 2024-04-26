class QuestionModel():
    def __init__(self,question,choices,answer) -> None:
        self.question = question
        self.choices = choices
        self.answer = answer
    def print(self):
        print(self.question)
        print(self.choices)
        print(self.answer)
# QuestionModel(question= 'Barcelona được biết đến với phong cách chơi tấn công nào?', choices= [' Tiki-taka', ' Catenaccio', ' Gegenpressing', ' Total Football'], answer= 'A').print()