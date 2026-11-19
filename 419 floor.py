
import tkinter as tk
import random

root = tk.Tk()
root.title("THE PYTHON BOOK: ABANDONED BUILDING ESCAPE")
root.geometry("850x650")
root.configure(bg="#151515")
root.resizable(False, False)

name = ""
score = 0
player_floor = 3
multo_floor = 1
exit_floor = 17
cleared_floors = [3]
game_over = False
escaped = False

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

boss_question = {
    "period": "ROOF EXIT",
    "q": "FINAL BOSS: What is Sir Jomar's username in MU Online?",
    "answer": "JOMS927"
}

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def make_label(text, size=16, color="white"):
    label = tk.Label(
        root,
        text=text,
        font=("Consolas", size, "bold"),
        fg=color,
        bg="#151515",
        wraplength=750,
        justify="center"
    )
    label.pack(pady=12)
    return label

def make_button(text, command):
    button = tk.Button(
        root,
        text=text,
        command=command,
        font=("Consolas", 13, "bold"),
        bg="#333333",
        fg="white",
        activebackground="#555555",
        activeforeground="white",
        width=35,
        height=2,
        relief="flat",
        cursor="hand2"
    )
    button.pack(pady=6)
    return button

def title_screen():
    clear_screen()

    make_label("THE PYTHON BOOK", 28, "#d6d6d6")
    make_label("ABANDONED BUILDING ESCAPE", 19, "#b00000")

    make_label("\nYou are exploring an abandoned 17-story building.")
    make_label("You discover THE PYTHON BOOK containing foundational Python lessons.")

    make_label("\nENTER YOUR NAME", 14)

    global name_entry
    name_entry = tk.Entry(
        root,
        font=("Consolas", 16),
        justify="center",
        bg="#333333",
        fg="white",
        insertbackground="white"
    )
    name_entry.pack(pady=10)

    make_button("START GAME", start_chapter)

def start_chapter():
    global name

    name = name_entry.get().strip()

    if name == "":
        name = "Adventurer"

    show_chapter(0)

chapters = [
    {
        "title": "CHAPTER 1: PRELIM",
        "lesson": "Python was created by Guido van Rossum in 1991.\n\nPython uses indentation for blocks.\n\nprint() displays output."
    },
    {
        "title": "CHAPTER 2: MIDTERM",
        "lesson": "input() takes user data.\n\nPython operators:\n\n+  Addition\n-  Subtraction\n/  Division\n// Floor Division\n%  Modulus"
    },
    {
        "title": "CHAPTER 3: FINALS",
        "lesson": "Loops repeat code.\n\nfor = repeats through a sequence.\n\nwhile = repeats while a condition is true."
    }
]

def show_chapter(index):
    clear_screen()

    make_label("THE PYTHON BOOK", 24, "#d6d6d6")
    make_label(chapters[index]["title"], 20, "#b00000")

    make_label("\n" + chapters[index]["lesson"], 16)

    if index < 2:
        make_button("NEXT CHAPTER", lambda: show_chapter(index + 1))
    else:
        make_button("START THE PURSUIT", start_game)

def start_game():
    clear_screen()

    make_label("THE PURSUIT BEGINS", 25, "#b00000")

    make_label("A ghost (multo) appears on Floor 1 chasing you!")
    make_label("Starting Floor: 3")
    make_label("Goal: Roof Exit (Floor 17)")

    make_label("\nCORRECT ANSWER: Ghost climbs 1 floor.")
    make_label("WRONG ANSWER: Ghost climbs 2 floors.")

    make_label("\nWARNING: The ghost gets closer after every move!", 14, "#ff4444")

    make_button("BEGIN ESCAPE", show_game)

def show_game():
    clear_screen()

    if game_over:
        show_game_over()
        return

    if escaped:
        show_victory()
        return

    make_label("ABANDONED BUILDING ESCAPE", 22, "#b00000")

    make_label(
        f"PLAYER: FLOOR {player_floor}       GHOST: FLOOR {multo_floor}",
        16
    )

    make_label(f"SCORE: {score}", 15, "#dddddd")

    distance = player_floor - multo_floor

    if distance == 2:
        make_label("WARNING! THE GHOST IS ONLY 2 FLOORS BELOW!", 13, "#ff9900")
    elif distance == 1:
        make_label("DANGER! THE GHOST IS RIGHT BELOW YOU!", 13, "#ff3333")

    make_label("\nCHOOSE YOUR NEXT FLOOR", 16)

    possible_moves = []

    for f in [player_floor - 1, player_floor + 1, player_floor + 2]:
        if 2 <= f <= exit_floor:
            possible_moves.append(f)

    for floor in possible_moves:
        if floor in cleared_floors:
            make_button(f"FLOOR {floor} - CLEARED", lambda f=floor: move_player(f))
        elif floor == exit_floor:
            make_button("FLOOR 17 - ROOF EXIT", lambda f=floor: move_player(f))
        else:
            make_button(f"FLOOR {floor} - LOCKED", lambda f=floor: move_player(f))

def move_player(target_floor):
    global player_floor, multo_floor, score

    if target_floor in cleared_floors:
        player_floor = target_floor
        multo_floor += 1

        check_ghost()
        return

    if target_floor == exit_floor:
        current_q = boss_question
    else:
        current_q = standard_questions.pop()

    show_question(target_floor, current_q)

def show_question(target_floor, current_q):
    clear_screen()

    make_label(f"FLOOR {target_floor} LOCKED", 22, "#b00000")
    make_label(current_q["period"], 14, "#aaaaaa")

    if target_floor == exit_floor:
        make_label("YOU HAVE REACHED THE ROOFTOP!", 17)
        make_label("A final boss is guarding the exit...")
        make_label("\n" + current_q["q"], 15)

        answer_entry = tk.Entry(
            root,
            font=("Consolas", 17),
            justify="center",
            bg="#333333",
            fg="white",
            insertbackground="white"
        )
        answer_entry.pack(pady=15)

        make_button(
            "SUBMIT ANSWER",
            lambda: check_answer(
                target_floor,
                current_q,
                answer_entry.get().strip().upper()
            )
        )

    else:
        make_label("\n" + current_q["q"], 16)

        for choice in current_q["choices"]:
            make_button(
                choice,
                lambda c=choice[0]: check_answer(target_floor, current_q, c)
            )

def check_answer(target_floor, current_q, user_ans):
    global score, player_floor, multo_floor, game_over, escaped

    clear_screen()

    if user_ans == current_q["answer"]:
        score += 1
        player_floor = target_floor
        cleared_floors.append(player_floor)

        make_label("CORRECT! DOOR UNLOCKED.", 20, "#00cc66")

        if player_floor == exit_floor:
            escaped = True
            show_victory()
            return

        multo_floor += 1

        make_label("The ghost climbs 1 floor.", 14)

    else:
        make_label("INCORRECT! THE DOOR IS JAMMED!", 20, "#ff3333")
        make_label(f"Correct answer: {current_q['answer']}")
        make_label("You cannot move to the next floor.")

        multo_floor += 2

        make_label("The ghost climbs 2 floors.", 14)

    check_ghost()

def check_ghost():
    global game_over

    if player_floor <= multo_floor:
        game_over = True
        show_game_over()
    else:
        make_button("CONTINUE", show_game)

def show_game_over():
    clear_screen()

    make_label("GHOST CAUGHT YOU!", 26, "#ff2222")

    ghost_art = r"""
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
    """

    make_label(ghost_art, 15, "#eeeeee")

    make_label("The ghost caught you inside the abandoned building.")
    make_label("GAME OVER.", 20, "#ff2222")

    show_results()

def show_victory():
    clear_screen()

    make_label("ROOF EXIT UNLOCKED!", 26, "#00cc66")
    make_label(f"{name}, YOU ESCAPED THE ABANDONED BUILDING!")
    make_label("\nYou defeated the final boss!")
    make_label("The ghost could not catch you.")
    make_label("You survived the 17-story nightmare!")

    show_results()

def show_results():
    make_label("\nFINAL RESULTS", 22)
    make_label(f"Player: {name}")
    make_label(f"Final Score: {score}")

    if escaped:
        make_label("RESULT: SUCCESS!", 16, "#00cc66")
        make_label("You escaped through the rooftop!")
    else:
        make_label("RESULT: DEFEAT!", 16, "#ff3333")
        make_label("You were trapped inside the building.")

    make_button("EXIT GAME", root.destroy)

title_screen()

root.mainloop()
