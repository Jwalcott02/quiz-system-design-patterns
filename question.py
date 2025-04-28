from abc import ABC, abstractmethod

# Question Interface
class Question(ABC):
    @abstractmethod
    def ask(self):
        pass

    @abstractmethod
    def is_correct(self, user_answer):
        pass



# Multiple Choice Question
class MultipleChoiceQuestion(Question):
    def __init__(self, prompt, options, correct_answers):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answers  # List of correct options (ex: ['A', 'C'])

    def ask(self):
        print(self.prompt)
        for label, option in zip(["A", "B", "C", "D"], self.options):
            print(f"{label}. {option}")

    def is_correct(self, user_answer):
        # Expect user_answer to be a list of selected options (e.g., ['A', 'C'])
        return set(user_answer) == set(self.correct_answer)

# True/False Question
class TrueFalseQuestion(Question):
    def __init__(self, prompt, correct_answer):
        self.prompt = prompt
        self.correct_answer = correct_answer  # True or False

    def ask(self):
        print(self.prompt)
        print("A. True")
        print("B. False")

    def is_correct(self, user_answer):
        # Expect user_answer to be 'A' for True, 'B' for False
        answer_bool = True if user_answer == 'A' else False
        return answer_bool == self.correct_answer
