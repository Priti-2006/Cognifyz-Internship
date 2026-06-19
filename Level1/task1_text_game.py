# ─────────────────────────────────────────
# Cognifyz Internship — Level 1, Task 1
# Text Based Game Program
# ─────────────────────────────────────────

import random

# ── QUIZ GAME ──────────────────────────────
def quiz_game():
    print("\n" + "="*45)
    print("         🎯 QUIZ GAME")
    print("="*45)
    print("Answer 5 questions. Score as high as you can!")
    print("="*45)

    questions = [
        {
            "question": "What is the capital of India?",
            "options":  ["A. Mumbai", "B. New Delhi", 
                         "C. Kolkata", "D. Chennai"],
            "answer":   "B"
        },
        {
            "question": "Which language is used for AI/ML?",
            "options":  ["A. Java", "B. C++", 
                         "C. Python", "D. PHP"],
            "answer":   "C"
        },
        {
            "question": "What does CPU stand for?",
            "options":  ["A. Central Process Unit", 
                         "B. Central Processing Unit",
                         "C. Computer Personal Unit", 
                         "D. Core Processing Unit"],
            "answer":   "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options":  ["A. Venus", "B. Jupiter", 
                         "C. Saturn", "D. Mars"],
            "answer":   "D"
        },
        {
            "question": "What is 15 x 15?",
            "options":  ["A. 215", "B. 225", 
                         "C. 235", "D. 245"],
            "answer":   "B"
        }
    ]

    score = 0
    total = len(questions)

    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for option in q['options']:
            print(f"   {option}")

        while True:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("❌ Please enter A, B, C or D only!")

        if answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer was: {q['answer']}")

    # Final Score
    print("\n" + "="*45)
    print(f"   QUIZ COMPLETE! Your Score: {score}/{total}")
    if score == total:
        print("   🏆 PERFECT SCORE! Excellent!")
    elif score >= 3:
        print("   👍 Good Job! Keep it up!")
    else:
        print("   📚 Keep Practicing!")
    print("="*45)


# ── GUESSING GAME ───────────────────────────
def guessing_game():
    print("\n" + "="*45)
    print("       🎲 NUMBER GUESSING GAME")
    print("="*45)
    print("I have picked a number between 1 and 100.")
    print("Try to guess it!")
    print("="*45)

    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print(f"\nYou have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        while True:
            try:
                guess = int(input(f"Attempt {attempts+1}/{max_attempts} — Enter your guess: "))
                if 1 <= guess <= 100:
                    break
                else:
                    print("❌ Please enter a number between 1 and 100!")
            except ValueError:
                print("❌ Invalid input! Enter a whole number.")

        attempts += 1

        if guess == secret:
            print(f"\n🎉 CORRECT! You guessed it in {attempts} attempts!")
            if attempts <= 3:
                print("🏆 Amazing! You're a mind reader!")
            elif attempts <= 5:
                print("👍 Great job!")
            else:
                print("😅 Just made it!")
            break
        elif guess < secret:
            remaining = max_attempts - attempts
            print(f"📈 Too LOW! Go higher. ({remaining} attempts left)")
        else:
            remaining = max_attempts - attempts
            print(f"📉 Too HIGH! Go lower. ({remaining} attempts left)")

    else:
        print(f"\n💀 GAME OVER! The number was {secret}.")
        print("Better luck next time!")


# ── MAIN MENU ───────────────────────────────
def display_menu():
    print("\n" + "="*45)
    print("        🎮 TEXT BASED GAME")
    print("  Cognifyz Technologies Internship")
    print("="*45)
    print("  1. Quiz Game")
    print("  2. Number Guessing Game")
    print("  3. Exit")
    print("="*45)

def main():
    print("\nWelcome to the Text Based Game!")
    print("Developed for Cognifyz Technologies Internship")

    while True:
        display_menu()
        choice = input("\nChoose an option (1-3): ").strip()

        if choice == '1':
            quiz_game()
        elif choice == '2':
            guessing_game()
        elif choice == '3':
            print("\n👋 Thanks for playing!")
            print("Cognifyz Technologies — Where Data Meets Intelligence")
            break
        else:
            print("\n❌ Invalid choice! Please select 1-3.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()