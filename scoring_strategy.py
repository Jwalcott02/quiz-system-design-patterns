from abc import ABC, abstractmethod

# Strategy Interface
class ScoringStrategy(ABC):
    @abstractmethod
    def calculate_score(self, question, user_answer):
        pass


# Standard Scoring: Full points if correct, 0 if wrong
class StandardScoring(ScoringStrategy):
    def calculate_score(self, question, user_answer):
        return 1 if question.is_correct(user_answer) else 0

# Partial Credit Scoring: Some points for partial correct answers
class PartialCreditScoring(ScoringStrategy):
    def calculate_score(self, question, user_answer):
        correct_answers = set(question.correct_answer)
        user_answers = set(user_answer)
        partial_correct = correct_answers.intersection(user_answers)
        return len(partial_correct) / len(correct_answers)
