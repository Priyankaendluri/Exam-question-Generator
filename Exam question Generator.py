import random

# Sample question bank (you can load from a file or database)
question_bank = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Rome", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Macbeth'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    },
    {
        "question": "2 + 2 × 2 = ?",
        "options": ["6", "8", "4", "2"],
        "answer": "6"
    },
]

def generate_exam(question_list, num_questions=3):
    selected_questions = random.sample(question_list, k=min(num_questions, len(question_list)))

    exam_paper = []
    answer_key = {}

    for i, q in enumerate(selected_questions, start=1):
        options = q["options"].copy()
        random.shuffle(options)

        correct_index = options.index(q["answer"])
        lettered_options = dict(zip("ABCD", options))
        
        exam_paper.append(f"Q{i}. {q['question']}")
        for letter, option in lettered_options.items():
            exam_paper.append(f"   {letter}) {option}")
        exam_paper.append("")  # Blank line

        answer_key[f"Q{i}"] = list(lettered_options.keys())[list(lettered_options.values()).index(q["answer"])]

    return exam_paper, answer_key

def print_exam_and_key():
    exam, key = generate_exam(question_bank, num_questions=3)
    
    print("----- EXAM PAPER -----\n")
    print("\n".join(exam))

    print("\n----- ANSWER KEY -----")
    for q, ans in key.items():
        print(f"{q}: {ans}")

if __name__ == "__main__":
    print_exam_and_key()

