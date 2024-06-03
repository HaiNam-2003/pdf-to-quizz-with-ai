from model.question_model import QuizItem,QuizData
from typing import List,Dict
class QuestionModel():
    def __init__(self,question,choices,answer) -> None:
        self.question = question
        self.choices = choices
        self.answer = answer
    def print(self):
        print(self.question)
        print(self.choices)
        print(self.answer)
class Parse():
    def __init__(self) -> None:
        pass
    
    # def parse_questions(self, text):
    #     quizzs = []
    #     lines = text.strip().split("\n\n")  # Tách câu hỏi và đáp án thành các đoạn văn bản riêng biệt
    #     print(text)
    #     for line in lines:
    #         if line.strip():  # Bỏ qua các dòng trống
    #             parts = line.strip().split("**")  # Tách câu hỏi và đáp án dựa trên ký tự in đậm
    #             question = parts[2].split("\n")[1]   # Lấy câu hỏi
    #             options = []
    #             if len(parts) > 2:
    #                 for option in parts[2].split("\n")[2:-1]:
    #                     print(option.strip().split(":")[1])
    #                     options.append(option.strip().split(":")[1])
    #             # print(options)
    #             choice_mapping = {}
    #             for i, choice in enumerate(options):
    #                 choice_mapping[chr(65 + i)] = choice.strip()
    #             answer = parts[2].strip().split(": ")[-1]  # Lấy đáp án
    #             quizz = QuestionModel(question=question.strip().split(":")[1],choices=choice_mapping,answer=answer)
    #             quizzs.append(quizz)
    #     return quizzs
    def create_quiz_item(self,question: str, options: List[str], answer: str) -> QuizItem:
        choice_mapping = {chr(65 + i): option.strip() for i, option in enumerate(options)}
        return QuizItem(question=question.strip(), choices=choice_mapping, answer=answer.strip().split(":")[1])
    # def parse_questions(self, text):
    #     lines = self.createQuizzsByText(text=text)
    #     quiz_data = QuizData()
    #     # print(lines)
    #     quizzs_result = []
    #     # lines = text.strip().split("\n\n")  # Tách câu hỏi và đáp án thành các đoạn văn bản riêng biệt
    #     for line in lines:
    #         if line.strip():  # Bỏ qua các dòng trống
    #             # parts = line.strip().split("\n")  # Tách câu hỏi và đáp án dựa trên dòng mới
    #             # content = parts[2:]
    #             parts = line.strip().split("\n")  # Tách câu hỏi và đáp án dựa trên dòng mới
    #             # print(parts)
    #             # Kiểm tra xem có định dạng bắt đầu và kết thúc câu hỏi không
    #             question = parts[0]  # Lấy câu hỏi, bỏ đi ký tự "<"
    #             options = []
    #             for option in parts[1:-1]:
    #                 options.append(option.split(":")[1])
    #             choice_mapping = {chr(65 + i): option.strip() for i, option in enumerate(options)}
    #             answer = parts[-1]  # Lấy đáp án
    #             # quizz = {
    #             #         "question": question,
    #             #         "choices": choice_mapping,
    #             #         "answer": answer.split(":")[1]
    #             #     }
    #             quiz = self.create_quiz_item(question, options, answer)
    #             print("hello")

    #             quiz_data.add_quiz(item=quiz)
    #     return quiz_data.data
    def parse_questions(self, text):
        lines = self.createQuizzsByText(text=text)
        quiz_data = QuizData(data=[])
        for line in lines:
            if line.strip():  # Bỏ qua các dòng trống
                parts = line.strip().split("\n")  # Tách câu hỏi và đáp án dựa trên dòng mới
                question = parts[0]  # Lấy câu hỏi
                options = []
                for option in parts[1:-1]:
                    options.append(option.split(":")[1])
                answer = parts[-1]  # Lấy đáp án
                quiz = self.create_quiz_item(question, options, answer)
                quiz_data.add_quiz(item=quiz)
        return quiz_data.data

    def createQuizzsByText(self,text):
        quizzes = []
        # Tìm vị trí của thẻ "start question" đầu tiên trong văn bản
        start_pos = text.find("<start question>")
        # Lặp qua toàn bộ văn bản để tìm và xử lý các câu hỏi
        while start_pos != -1:
            # Tìm vị trí của thẻ "end question" tương ứng với "start question"
            end_pos = text.find("<end question>", start_pos)
            # Kiểm tra xem cặp thẻ "start question" và "end question" có tồn tại không
            if end_pos != -1:
                # Cắt chuỗi từ vị trí bắt đầu của "<start question>" đến vị trí kết thúc của "<end question>"
                question_text = text[start_pos + len("<start question>"):end_pos].strip()
                # Thêm câu hỏi vào danh sách
                quizzes.append(question_text)
                # Tìm vị trí của thẻ "start question" tiếp theo từ vị trí kết thúc của "end question"
                start_pos = text.find("<start question>", end_pos)
            else:
                break
        return quizzes




text = """
**Câu hỏi 4:**
<start question>
Loại tế bào nào thường là đơn bào?
A: Tế bào Proka
B: Tế bào Euka
C: Cả hai đều có thể là đơn bào
D: Không xác định được từ đoạn văn bản
Answer: A
<end question>

**Câu hỏi 5:**
<start question>
Tế bào nào có hệ thống bào quan biệt hóa trong tế bào chất?
A: Tế bào Proka
B: Tế bào Euka
C: Cả hai đều có hệ thống bào quan biệt hóa
D: Không xác định được từ đoạn văn bản
Answer: B
<end question>

**Câu hỏi 6:**
<start question>
Quá trình dịch mã diễn ra ở đâu trong tế bào Euka?
A: Nhân
B: Tế bào chất
C: Cả nhân và tế bào chất
D: Không xác định được từ đoạn văn bản
Answer: B
<end question>

**Câu hỏi 7:**
<start question>
Loại tế bào nào có thể thực hiện chức năng ở cả quy mô đơn bào và đa bào?
A: Tế bào Proka
B: Tế bào Euka
C: Cả hai đều có thể thực hiện chức năng ở cả quy mô đơn bào và đa bào
D: Không xác định được từ đoạn văn bản
Answer: C
<end question>
"""
# print(Parse().parse_questions(text=text))
# Parse().parse_questions(text=text)