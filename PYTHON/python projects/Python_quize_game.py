# python quiz game

questions = ("How many elements are in the periodic table?:",
             "which animal lays the larhest eggs?: ",
             "what is the most abundant gas in Earth's atmopspher?: ",
             "How many bones are in the human body?: ",
             "which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogin", "B. Oxygen", "C. Carbon", "D. Hydrogen"), 
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for questions in questions:
    print("------------------------------")
    print(questions)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    
print("-----------------------")
print("      RESULTS          ")
print("--------------------   ")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print() 

score = int(score / len(questions)* 1000)
print(f"Your score is : {score}%")