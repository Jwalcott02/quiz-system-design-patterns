from scoring_strategy import StandardScoring
from question import Question

class QuizManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(QuizManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.questions = []
        self.scoring_strategy = StandardScoring()
        self.score = 0
        self._initialized = True

    def set_scoring_strategy(self, strategy):
        self.scoring_strategy = strategy

    def add_question(self, question):
        self.questions.append(question)

    def start_quiz(self):
        for question in self.questions:
            question.ask()
            user_input = input("Your answer (e.g., A or A,C): ").split(",")
            user_input = [ans.strip() for ans in user_input]
            earned = self.scoring_strategy.calculate_score(question, user_input)
            print(f"Points earned: {earned}\n")
            self.score += earned
        print(f"Final Score: {self.score}")
