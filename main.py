#!/usr/bin/env python3
import enum
from tkinter import *
from tkinter import messagebox
import tkinter
import game
import sys
import os

root = tkinter.Tk()
wordleGame = game.WordleGame()

GREEN = "#007d21"
YELLOW = "#e2e600"
BLACK = "#000000"
GREY = "#808080"
WHITE = "#FFFFFF"

root.config(bg=WHITE)
root.title("Wordle")
wordInput = Entry(root)
wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3)


def playGame():
    guess = wordInput.get().lower()
    wordleGame.guess(guess)
    game_status = wordleGame.get_game_status()
    if wordleGame.get_last_guess():
        guess, squares = wordleGame.get_last_guess()
        for i, letter in enumerate(guess):
            label = Label(root, text=letter.upper())
            label.grid(row=wordleGame.turn_number+1,
                       column=i, padx=20, pady=20)
            label.config(bg=squares[i], fg=BLACK, padx=20, pady=20)
        wordInput.delete(0, END)
        root.update()
        if game_status == 1:
            MsgBox=messagebox.askquestion('Again', 'Do you want to play again?')
            if MsgBox == 'yes':
                python = sys.executable
                os.execl(python, python, * sys.argv)
            else:
                messagebox.showinfo('Exit','OK. Bye-bye!')
                root.destroy()

        elif game_status == -1:
            MsgBox=messagebox.askquestion('Again', 'Do you want to play again?')
            if MsgBox == 'yes':
                python = sys.executable
                os.execl(python, python, * sys.argv)
            else:
                messagebox.showinfo('Exit', 'OK. Bye-bye!')
                root.destroy()

wordGuessButton = Button(root, text="Guess", command=playGame)
wordGuessButton.grid(row=999, column=3, columnspan=3)
root.bind('<Return>', lambda event: playGame())

root.mainloop()