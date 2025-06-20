import tkinter as tk
import random
class HangmanApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hangman Game")
        self.words = ["python","hangman","challenge","programming","developer"]
        self.guessed_letters = set()
        self.attempts = 6
        self.word = random.choice(self.words)
        self.word_label = tk.Label(self.window, text=self.get_display_word(), font=("Arial", 24))
        self.word_label.pack()
        self.guess_entry = tk.Entry(self.window, font=("Arial", 18))
        self.guess_entry.pack()
        self.guess_button = tk.Button(self.window, text="Guess", command=self.guess_letter)
        self.guess_button.pack()
        self.result_label = tk.Label(self.window, text="", font=("Arial", 18))
        self.result_label.pack()
        self.attempts_label = tk.Label(self.window, text=f"Attempts left: {self.attempts}", font=("Arial", 18))
        self.attempts_label.pack()
    def get_display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
    def guess_letter(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        if len(guess) != 1 or not guess.isalpha():
            self.result_label.config(text="Please enter a single letter.")
            return
        if guess in self.guessed_letters:
            self.result_label.config(text="You've already guessed that letter.")
            return
        self.guessed_letters.add(guess)

        if guess not in self.word:
           self.attempts -= 1

        self.word_label.config(text=self.get_display_word())
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

        if "_" not in self.get_display_word():
            self.result_label.config(text="You won!")
            self.guess_button.config(state=tk.DISABLED)

        if self.attempts == 0:
            self.result_label.config(text=f"You lost! The word was '{self.word}'")
            self.guess_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = HangmanApp()
    app.window.mainloop()