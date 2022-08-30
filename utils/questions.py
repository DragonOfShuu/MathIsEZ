from utils.general_utils import stringtobool

class Question:
    '''
    Class for asking a question. If answer_type is None,
    then str(answer) is returned. If beckon_text is None,
    then the default beckon is "> ".
    '''
    def __init__(self, question: str, /, answer_type: None, beckon_text: str = None):
        self.question = question
        self.answer_type = answer_type
        self.beckon_text = beckon_text
    def __str__(self):
        return self.question
    
    def main_question(self, comparable: type, answer: float | int | bool | str):
        try:
            if comparable == type(float):
                return float(answer)
            elif comparable == type(int):
                return int(answer)
            elif comparable == type(bool):
                return stringtobool(answer)
            else:
                return answer;
        except Exception:
            print(f"Not an accepted type. Accepted types are {self.answer_type}")
            return None;

    # Ask various questions
    def execute(self):
        while True:
            print(self.question)
            answer = input("> " if self.beckon_text == None else self.beckon_text)
            comparable = type(str if self.answer_type else self.answer_type)
            
            returnable = self.main_question(comparable, answer)
            if returnable == None:
                continue;
            else:
                return returnable;

class Questionnaire:
    '''
    Class for asking multiple questions. DAnswerType and DBeckonText
    are overriding variables for values that are None.
    '''
    def __init__(self, questions: list[Question | str], /, DAnswerType: type = None, DBeckonText: str = None):
        self.questions = questions
        self.DAnswerType = DAnswerType
        self.DBeckonText = DBeckonText
    def execute(self):
        answers = []
        for question in self.questions:
            # Override values if they are not present
            # in the original question.
            if type(question) == Question:
                if question.answer_type == None:
                    question.answer_type = self.DAnswerType;
                if question.beckon_text == None:
                    question.beckon_text = self.DBeckonText;
            else:
                question = Question(question, self.DAnswerType, self.DBeckonText);

            answers.append(question.execute())
        return answers;