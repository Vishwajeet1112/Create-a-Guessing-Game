import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        self.root.geometry("500x400")
        self.root.configure(bg="#e3f2fd")  # Light blue background
        
        self.secret_number = random.randint(1,2)
        self.attempts = 0
        
        self.create_widgets()

    def create_widgets(self):
        # Instructions
        tk.Label(self.root, text="Guess a number between 1 and 100", font=('Arial', 12), bg="#e3f2fd").pack(pady=10)
        
        # Entry for user guess
        self.entry_guess = tk.Entry(self.root, font=('Arial', 12))
        self.entry_guess.pack(pady=10)
        
        # Submit button
        self.btn_submit = tk.Button(self.root, text="Submit Guess", font=('Arial', 12), command=self.check_guess, bg="#0288d1", fg="white")
        self.btn_submit.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(self.root, text="", font=('Arial', 12), bg="#e3f2fd")
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1
            
            if guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed the number in {self.attempts} attempts.")
                self.show_restart_option()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def show_restart_option(self):
        """Show a dialog to restart the game."""
        response = messagebox.askyesno("Play Again?", "Would you like to play again?")
        if response:
            self.restart_game()
        else:
            self.root.quit()

    def restart_game(self):
        """Restart the game with a new secret number and reset attempts."""
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry_guess.delete(0, 'end')

# Set up the GUI window
root = tk.Tk()
app = GuessingGame(root)
root.mainloop()
