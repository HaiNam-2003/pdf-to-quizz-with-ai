def parse_quiz_text(quiz_text):
    new_quizz= quiz_text['result']
    parsed_output = []
    
    # Split the text by double newline characters to separate questions
    questions = new_quizz.strip().split('\n\n')
    
    for question in questions:
        # Split each question by newline characters to separate question, options, and answer
        lines = question.strip().split('\n')
        
        # Extract the question and answer
        question_text = lines[0].strip()
        answer = lines[-1].strip()
        
        # Extract options
        options = {}
        for line in lines[1:-1]:
            parts = line.split(': ')
            option_key = parts[0].strip().split(': ')[0]
            option_value = parts[1].strip()
            options[option_key] = option_value
        
        # Append the parsed question to the output list
        parsed_output.append({
            "question": question_text,
            "options": options,
            "answer": answer
        })
    
    return parsed_output

# Example usage:
quiz_text = {
    "query": "\"You are a teacher preparing questions for a quiz. Given the following document, please generate 4 multiple-choice questions (MCQs) with 4 options and a corresponding answer letter based on the document",
    "result": "\n1. What year was Chelsea Football Club founded?\na) 1905\nb) 1925\nc) 1950\nd) 1975\nAnswer: a) 1905\n\n2. Which color is primarily associated with Chelsea Football Club?\na) Cobalt blue\nb) Red\nc) Yellow\nd) Green\nAnswer: a) Cobalt blue\n\n3. In which English football competition does Chelsea currently participate?\na) Championship\nb) Premier League\nc) FA Cup\nd) League Cup\nAnswer: b) Premier League\n\n4. Which of the following is NOT a significant trophy that Chelsea has won?\na) Premier League championship\nb) FA Cup\nc) UEFA Champions League\nd) League Cup\nAnswer: c) UEFA Champions League<|im_end|>",
    "source_documents": [
        {
            "page_content": "Chelsea is a renowned football club based in London, England. The club was founded in 1905 and currently competes in the English Premier League, the top Aer of English football. Chelsea has won numerous signiﬁcant Atles throughout its history, including mulAple Premier League championships, FA Cups, and League Cups. The club's emblem is a lion, and its primary color is cobalt blue. Chelsea's home ground is Stamford Bridge, one of the most famous and historic stadiums in London. Chelsea boasts a large fan",
            "metadata": {
                "source": "/Users/mac/Documents/Final Project/app/service/test/data/test2.pdf",
                "page": 0
            },
            "type": "Document"
        },
        {
            "page_content": "stadiums in London. Chelsea boasts a large fan base worldwide and consistently aHracts aHenAon from football enthusiasts with its aHacking and entertaining style of play.",
            "metadata": {
                "source": "/Users/mac/Documents/Final Project/app/service/test/data/test2.pdf",
                "page": 0
            },
            "type": "Document"
        }
    ]
}
