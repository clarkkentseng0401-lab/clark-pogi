
import random

print("=================================================================")
print("          THE PYTHON BOOK: ABANDONED BUILDING ESCAPE")
print("=================================================================")

# Get player name
name = input("\nEnter your name: ")

if name == "":
    name = "Adventurer"

print("\nYou are exploring an abandoned 17-story building.")
print("You find THE PYTHON BOOK containing foundational Python lessons.")
input("\nPress ENTER to open the book...")

print("=================================================================")
print("                    CHAPTER 1: PRELIM")
print("=================================================================")
print("- Python created by Guido van Rossum in 1991.")
print("- Uses indentation for blocks. print() shows output.")

action1 = input("\nType 'next': ").lower()

while action1 != "next":
    action1 = input("Type 'next': ").lower()

print("=================================================================")
print("                    CHAPTER 2: MIDTERM")
print("=================================================================")
print("- input() takes user data. Operators: +, -, /, //, %.")

action2 = input("\nType 'next': ").lower()

while action2 != "next":
    action2 = input("Type 'next': ").lower()

print("=================================================================")
print("                    CHAPTER 3: FINALS")
print("=================================================================")
print("- Loops repeat code. for = sequence, while = condition.")

action3 = input("\nType 'done': ").lower()

while action3 != "done":
    action3 = input("Type 'done': ").lower()

print("=================================================================")
print("                  THE PURSUIT BEGINS")
print("=================================================================")
print("A ghost (multo) appears on Floor 1 chasing you!")
print("Start: Floor 3. Goal: Roof Exit (Floor 17).")
print("Correct answer: Ghost climbs 1 floor.")
print("Wrong answer: Ghost climbs 2 floors.")
print("WARNING: The ghost gets closer after every move!")

input("\nPress ENTER to start...")

# Game variables
score = 0
player_floor = 3
multo_floor = 1
exit_floor = 17
cleared_floors = [3]
game_over = False
escaped = False

# Question pool
standard_questions = [
    {"period": "PRELIM", "q": "What is Python?", "choices": ["A. Programming language", "B. Computer", "C. Website", "D. Game"], "answer": "A"},
    {"period": "PRELIM", "q": "Which function displays output?", "choices": ["A. input()", "B. print()", "C. len()", "D. int()"], "answer": "B"},
    {"period": "PRELIM", "q": "Which symbol is used for single-line comments?", "choices": ["A. //", "B. --", "C. #", "D. @"], "answer": "C"},
    {"period": "PRELIM", "q": "Which data type represents whole numbers?", "choices": ["A. str", "B. int", "C. float", "D. bool"], "answer": "B"},
    {"period": "PRELIM", "q": "Which function captures user input?", "choices": ["A. print()", "B. input()", "C. range()", "D. len()"], "answer": "B"},

    {"period": "MIDTERM", "q": "Which keyword is used for conditional decisions?", "choices": ["A. if", "B. print", "C. input", "D. import"], "answer": "A"},
    {"period": "MIDTERM", "q": "Which keyword handles alternative outcomes when an if condition fails?", "choices": ["A. for", "B. else", "C. while", "D. break"], "answer": "B"},
    {"period": "MIDTERM", "q": "Which loop structure is designed for iterating over sequences?", "choices": ["A. print", "B. input", "C. for", "D. str"], "answer": "C"},
    {"period": "MIDTERM", "q": "What sequence of numbers does range(5) generate?", "choices": ["A. 1 to 5", "B. 0 to 4", "C. 0 to 5", "D. 1 to 4"], "answer": "B"},
    {"period": "MIDTERM", "q": "Which operator checks for value equality?", "choices": ["A. =", "B. !=", "C. ==", "D. +="], "answer": "C"},

    {"period": "FINALS", "q": "What does the len() function return?", "choices": ["A. Number of items", "B. A random number", "C. A string", "D. A loop"], "answer": "A"},
    {"period": "FINALS", "q": "Which keyword is used to stop a loop?", "choices": ["A. stop", "B. break", "C. end", "D. exit"], "answer": "B"},
    {"period": "FINALS", "q": "Which collection type uses square brackets []?", "choices": ["A. Tuple", "B. Dictionary", "C. List", "D. Set"], "answer": "C"},
    {"period": "FINALS", "q": "What does the list method append() do?", "choices": ["A. Removes an item", "B. Adds an item", "C. Sorts a list", "D. Clears a list"], "answer": "B"},
    {"period": "FINALS", "q": "Which keyword is used to load external modules?", "choices": ["A. include", "B. using", "C. import", "D. add"], "answer": "C"}
]

random.shuffle(standard_questions)

# Final boss question
boss_question = {
    "period": "ROOF EXIT",
    "q": "FINAL BOSS: What is Sir Jomar's username in MU Online?",
    "answer": "JOMS927"
}

# Main game loop
while not game_over and not escaped:

    print("\n=================================================================")
    print(f"       PLAYER: FLOOR {player_floor} | GHOST: FLOOR {multo_floor}")
    print(f"                       SCORE: {score}")
    print("=================================================================")

    # Ghost warning
    distance = player_floor - multo_floor

    if distance == 2:
        print("WARNING: The ghost is only 2 floors below you!")
    elif distance == 1:
        print("DANGER! The ghost is right below you!")

    # Available moves
    possible_moves = []

    for f in [player_floor - 1, player_floor + 1, player_floor + 2]:
        if 2 <= f <= exit_floor:
            possible_moves.append(f)

    print(f"\nAvailable floors: {possible_moves}")

    # Player selects floor
    target_floor = 0

    while target_floor not in possible_moves:

        choice = input("Choose floor number: ")

        if choice.isdigit() and int(choice) in possible_moves:
            target_floor = int(choice)
        else:
            print("Invalid floor! Choose from the available floors.")

    # Check cleared floors
    if target_floor in cleared_floors:

        player_floor = target_floor

        print(f"\nFloor {player_floor} is already cleared.")
        print("You move through the floor safely.")

        multo_climb = 1

    else:

        # Get question
        if target_floor == exit_floor:
            current_q = boss_question
        else:
            current_q = standard_questions.pop()

        print(f"\n--- FLOOR {target_floor} LOCKED [{current_q['period']}] ---")

        if target_floor == exit_floor:
            print("\nYou have reached the rooftop!")
            print("A final boss is guarding the exit...")
            print("Answer correctly to escape!")

        # Display question
        print("\n" + current_q["q"])

        if target_floor == exit_floor:

            user_ans = input("Answer: ").upper()

        else:

            for c in current_q["choices"]:
                print(c)

            user_ans = input("\nAnswer (A/B/C/D): ").upper()

        # Check answer
        if user_ans == current_q["answer"]:

            score += 1
            player_floor = target_floor
            cleared_floors.append(player_floor)

            print("\nCORRECT! Door unlocked.")

            multo_climb = 1

            if player_floor == exit_floor:

                escaped = True

                print("\n=================================================================")
                print("                     ROOF EXIT UNLOCKED!")
                print("=================================================================")
                print(f"{name}, you escaped the abandoned building!")
                print("You defeated the final boss!")
                print("The ghost could not catch you.")
                print("You survived the 17-story nightmare!")

                break

        else:

            print(f"\nINCORRECT! Correct answer: {current_q['answer']}")
            print("The door is jammed!")
            print("You cannot move to the next floor.")

            multo_climb = 2

    # Ghost movement
    multo_floor += multo_climb

    print(f"\nThe ghost climbs {multo_climb} floor(s).")
    print(f"The ghost is now on Floor {multo_floor}!")

    # Check win or lose
    if player_floor <= multo_floor:

        game_over = True

        print("\n=================================================================")
        print("                       GHOST CAUGHT YOU!")
        print("=================================================================")

        print(r"""
                  .-''''''''''-.
                .'   _      _   '.
               /    (o)    (o)    \
              |                 |
              |       BOO!      |
              |     \______/    |
               \               /
                '.           .'
                  '-.____.-'
                     |  |
                    /    \
                   /      \
        """)

        print("The ghost caught you inside the abandoned building.")
        print("GAME OVER.")

    elif player_floor - multo_floor == 1:
        print("\nDANGER! The ghost is right below you!")

    elif player_floor - multo_floor == 2:
        print("\nWARNING! The ghost is getting dangerously close!")

# Final results
print("\n=================================================================")
print("                         FINAL RESULTS")
print("=================================================================")

print(f"Player: {name}")
print(f"Final Score: {score}")

if escaped:
    print("RESULT: SUCCESS!")
    print("You escaped through the rooftop!")
else:
    print("RESULT: DEFEAT!")
    print("You were trapped inside the abandoned building.")

print("=================================================================")
print("                       END OF THE GAME")
print("=================================================================")

