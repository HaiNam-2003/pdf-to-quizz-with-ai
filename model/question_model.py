from pydantic import BaseModel
from typing import List, Dict

# class QuestionModel(BaseModel):
#     def __init__(self,question,choices,answer) -> None:
#         self.question = question
#         self.choices = choices
#         self.answer = answer
#     def print(self):
#         print(self.question)
#         print(self.choices)
#         print(self.answer)
# # QuestionModel(question= 'Barcelona được biết đến với phong cách chơi tấn công nào?', choices= [' Tiki-taka', ' Catenaccio', ' Gegenpressing', ' Total Football'], answer= 'A').print()
class QuizItem(BaseModel):
    question: str
    choices: Dict[str, str]
    answer: str
class QuizData(BaseModel):
    data: list[QuizItem]
    def add_quiz(self,item : QuizItem):
        self.data.append(item)
