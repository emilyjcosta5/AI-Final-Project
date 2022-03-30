import enum
from tkinter import *
from tkinter import messagebox
import tkinter
import game

root = tkinter.Tk()
wordleGame = game.WordleGame()

GREEN = "#007d21"
YELLOW = "#e2e600"
BLACK = "#000000"
GREY = "#808080"
WHITE = "#FFFFFF"

root.config(bg=BLACK)
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

        if game_status == 1:
            messagebox.showinfo(
                "correct!", f"You won!")
            # try_again = input("You won! Play another game? (Y/N) ")
            # if try_again == 'Y':
            #     print("Not right now")
            #     break
            # game = WordleGame(word_source="web_simple")
            # game_status = game.get_game_status()
            # else:
            #     print("OK. Bye-bye!")
            #     break
        elif game_status == -1:
            messagebox.showerror(
                "you lose!", f"You Lose! The word was {wordleGame.answer}")
            # if try_again == 'Y':
            #     wordleGame.restart()
            #     game_status = wordleGame.get_game_status()
            # else:
            #     print("OK. Bye-bye!")
            #     break


wordGuessButton = Button(root, text="Guess", command=playGame)
wordGuessButton.grid(row=999, column=3, columnspan=3)
root.bind('<Return>', lambda event: playGame())


root.mainloop()
