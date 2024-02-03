import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.choices = ["Rock", "Paper", "Scissors"]

        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors Game")

        self.user_choice_label = tk.Label(self.window, text="Your Choice:")
        self.user_choice_label.pack()

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("Rock")  # Default choice
        self.user_choice_menu = tk.OptionMenu(self.window, self.user_choice_var, *self.choices)
        self.user_choice_menu.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        self.play_again_button = tk.Button(self.window, text="Play Again", command=self.play_again)
        self.play_again_button.pack()

        self.update_result()

        self.window.mainloop()

    def play_again(self):
        self.user_choice_var.set("Rock")
        self.update_result()

    def update_result(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(self.choices)

        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"You chose {user_choice}.\nComputer chose {computer_choice}.\n{result}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
        ):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

if __name__ == "__main__":
    RockPaperScissorsGame()
