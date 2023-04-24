import tkinter as tk
import random
from tkinter import messagebox

class TreasureHunt:
    def __init__(self):
        self.clues = [
            "You look for the limit but you find it infinite",
            "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
            "I am a paradox, a riddle wrapped in a mystery, yet I am always there for you to see. What am I?",
            "I am not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but I need water to live. What am I?",
            "The end is the beginning and the beginning is the end"
        ]
        self.answers = [
            "universe",
            "echo",
            "reflection",
            "Fire",
            "infinite"
        ]
        self.current_clue_number = 0
        self.chances = 3
        self.window = tk.Tk()
        self.window.geometry("400x400")
        self.window.title("Treasure Hunt")

        self.chances_label = tk.Label(self.window, text="Lives : "+str(self.chances))
        self.chances_label.pack()
        
        self.clue_label = tk.Label(self.window, text=self.clues[self.current_clue_number])
        self.clue_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.window)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.window, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.hint_button = tk.Button(self.window, text="Get a hint", command=self.show_hint)
        self.hint_button.pack(pady=10)
        
        self.refresh_button = tk.Button(self.window, text="Refresh", command=self.ref)
        self.refresh_button.pack()
        self.window.mainloop()
    
    def ref(self):
        self.window.destroy()
        TreasureHunt()
        
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
            if self.chances>0:
                self.chances-=1
            if self.chances == 0:
                tk.messagebox.showerror("OOPS!", "You reached dead end")
            else:
                tk.messagebox.showerror("Wrong Answer", "Try again!")
            self.chances_label.config(text = self.chances)

    def show_hint(self):
        hint = f"The first letter of the answer is '{self.answers[self.current_clue_number][0]}'"
        tk.messagebox.showinfo("Hint", hint)
def main():
    treasure_hunt = TreasureHunt()
if __name__ == "__main__":
    main()
    

    
