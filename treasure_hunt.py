import tkinter as tk
import random
from tkinter import messagebox

class TreasureHunt:
    def __init__(self):
        self.clues = [
            "What starts with an 'E', ends with an 'E', but only contains one letter?",
            "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
            "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
            "I am not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but I need water to live. What am I?",
            "I am always hungry, I must always be fed. The finger I touch, will soon turn red. What am I?"
        ]
        self.answers = [
            "An envelope",
            "An echo",
            "A pencil",
            "Fire",
            "Fire"
        ]
        self.current_clue_number = 0

        self.window = tk.Tk()
        self.window.geometry("400x400")
        self.window.title("Treasure Hunt")

        self.clue_label = tk.Label(self.window, text=self.clues[self.current_clue_number])
        self.clue_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.window)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.window, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.hint_button = tk.Button(self.window, text="Get a hint", command=self.show_hint)
        self.hint_button.pack(pady=10)

        self.window.mainloop()

    def check_answer(self):
        user_answer = self.answer_entry.get()
        if user_answer.lower() == self.answers[self.current_clue_number].lower():
            if self.current_clue_number == len(self.clues) - 1:
                tk.messagebox.showinfo("Congratulations!", "You found the treasure!")
                self.window.destroy()
            else:
                self.current_clue_number += 1
                self.clue_label.config(text=self.clues[self.current_clue_number])
                self.answer_entry.delete(0, tk.END)
                tk.messagebox.showinfo("Correct Answer!", "Well done! Here's your next clue.")
        else:
            tk.messagebox.showerror("Wrong Answer", "Try again!")

    def show_hint(self):
        hint = f"The first letter of the answer is '{self.answers[self.current_clue_number][0]}'"
        tk.messagebox.showinfo("Hint", hint)

treasure_hunt = TreasureHunt()

    
