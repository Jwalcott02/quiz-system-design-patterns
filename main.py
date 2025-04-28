from quiz_manager import QuizManager
from question import MultipleChoiceQuestion, TrueFalseQuestion
from scoring_strategy import StandardScoring, PartialCreditScoring

def main():
    quiz = QuizManager()  # Singleton instance

    # Choose Scoring Strategy
    print("Choose scoring strategy:")
    print("1. Standard Scoring (full points if correct)")
    print("2. Partial Credit Scoring (partial points for partially correct)")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        quiz.set_scoring_strategy(StandardScoring())
    else:
        quiz.set_scoring_strategy(PartialCreditScoring())

    # Add questions
    q1 = MultipleChoiceQuestion(
        "What are the primary colors?",
        ["Red", "Green", "Blue", "Yellow"],
        ["A", "C", "D"]  # Correct answers: Red, Blue, Yellow
    )

    q2 = TrueFalseQuestion(
        "The Earth is flat.",
        False
    )

    quiz.add_question(q1)
    quiz.add_question(q2)

    # Start quiz
    quiz.start_quiz()

if __name__ == "__main__":
    main()
