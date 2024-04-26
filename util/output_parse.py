from model.question_model import QuestionModel
class Parse():
    def __init__(self) -> None:
        pass

    def parse_questions(self,text):
        quizzs = []
        lines = text.strip().split("\n\n")  # Tách câu hỏi và đáp án thành các đoạn văn bản riêng biệt
        for line in lines:
            if line.strip():  # Bỏ qua các dòng trống
                parts = line.strip().split("**")  # Tách câu hỏi và đáp án dựa trên ký tự in đậm
                question = parts[2].split("\n")[1]  # Lấy câu hỏi
                options = [option.strip()[3:] for option in parts[2].split("\n")[1:] if option.strip().startswith("(")]  # Lấy các lựa chọn
                choice_mapping = {}
                for i, choice in enumerate(options):
                    choice_mapping[chr(65 + i)] = choice.strip()
                answer = parts[3].strip().split(": ")[1]  # Lấy đáp án
                quizz = QuestionModel(question=question,choices=choice_mapping,answer=answer)
                quizzs.append(quizz)
        return quizzs


text = """
**Câu hỏi 1:**
Barcelona được biết đến với phong cách chơi tấn công nào?
(A) Tiki-taka
(B) Catenaccio
(C) Gegenpressing
(D) Total Football
**Đáp án: A**

**Câu hỏi 2:**
Messi đã giành được bao nhiêu giải thưởng FIFA Ballon d'Or?
(A) 4
(B) 5
(C) 6
(D) 7
**Đáp án: C**

**Câu hỏi 10:**
Messi được coi là một trong những cầu thủ bóng đá vĩ đại nhất mọi thời đại vì lý do nào?
(A) Sự xuất sắc và tài năng trên sân cỏ
(B) Số lượng danh hiệu giành được
(C) Khả năng ghi bàn ấn tượng
(D) Tất cả các câu trên
**Đáp án: D**
"""

questions = Parse().parse_questions(text=text)
print(questions)
for i in range(len(questions)):
    questions[i].print()