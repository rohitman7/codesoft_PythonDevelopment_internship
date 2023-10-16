import tkinter as tk
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=result)

    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")

def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer's Score: 0")

# Create a new window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

# Create user interface components
instruction_label = tk.Label(window, text="Choose your move:")
instruction_label.pack()

choices = ["rock", "paper", "scissors"]
user_choice_var = tk.StringVar()
user_choice_var.set(choices[0])

user_choice_menu = tk.OptionMenu(window, user_choice_var, *choices)
user_choice_menu.pack()

play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack()

reset_button = tk.Button(window, text="Reset Scores", command=reset_scores)
reset_button.pack()

computer_choice_label = tk.Label(window, text="")
computer_choice_label.pack()

result_label = tk.Label(window, text="")
result_label.pack()

user_score = 0
computer_score = 0

user_score_label = tk.Label(window, text=f"Your Score: {user_score}")
user_score_label.pack()

computer_score_label = tk.Label(window, text=f"Computer's Score: {computer_score}")
computer_score_label.pack()

# Run the GUI application
window.mainloop()
