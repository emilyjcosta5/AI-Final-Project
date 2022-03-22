import requests
import random

class Game:
    def __init__(self, word_length=5, word_source="manual", word_list=None, number_guesses=6):
        """
        Initiates the Game class

        Parameters
        ----------
        word_length: int, optional 
            Length of word to guess
        word_source: str, optional
            Where to get the input of the words
        word_list: list, optional
            If word_source is 'manual', then this is the list of allowed word guesses
        number_guesses: int, optional
            Max number of times a word can be guessed

        Returns
        None
        -------
        """
        # check parameters are correct
        if word_source not in ["web_simple", "manual"]:
            raise ValueError("word_list parameter is 'word_simple' or 'manual'.")
        if not isinstance(word_length, int):
            raise ValueError("word_length must be an int.") 
        if not isinstance(number_guesses, int):
            raise ValueError("number_guesses must be an int.") 
        if word_source=="manual":
            if word_list==None:
                raise ValueError("word_list must be provided.")
            if not type(word_list) is list or not type(word_list) is tuple:
                raise ValueError("word_list must be in list or tuple form.")
            if not all([isinstance(word, str) for word in word_list]):
                raise ValueError("all words in word_list must be strings.")  
        # set up variables
        self.word_list = word_list
        if word_source=="web_simple":
            url = "https://www.mit.edu/~ecprice/wordlist.10000"
            r = requests.get(url, stream=True)
            self.word_list = [word for word in r.text.split("\n") if len(word)==word_length]
        self.answer = random.choice(self.word_list)
        self.turn_number = 0
        self.number_guesses = number_guesses
        self.guesses = []
        self.WIN = 1
        self.LOSE = -1
        self.game_status = 0
        self.word_length = word_length

    def get_guesses(self):
        '''
        Gives previous guesses and the square color of each letter, 
        which indicates the correctness of the guess.

        Parameters
        ----------
        None

        Returns
        -------
        guesses: tuple
            The guesses structured as (guess, colors of letter blocks)
        '''
        squares = []
        for guess in self.guesses:
            square = []
            for i, letter in enumerate(guess):
                if letter==self.answer[i]:
                    square.append("GREEN")
                elif letter in self.answer:
                    square.append("YELLOW")
                else:
                    square.append("GREY")
            squares.append(square)
        guesses = zip(self.guesses,squares)
        return guesses

    def get_last_guess(self):
        '''
        Get most recent word guess

        Parameters
        ----------
        None

        Returns
        -------
        last_guess: str
            Last word guesses
        last_squares: list
            The color of the square of the last guess
        '''
        guesses = self.get_guesses()
        if not guesses:
            return []
        last_guess, last_squares = guesses[-1]
        return last_guess, last_squares

    def restart(self):
        '''
        Restarts game to default

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.turn_number = 0
        self.guesses = []
        self.game_status = 0

    def guess(self, guess):
        if not len(guess)==self.word_length:
            print('Must guess a word of length %d'%self.word_length)
            return self.game_status
        if not self.turn_number<self.number_guesses:
            print('No more guesses left! Please restart game.')
            self.game_status = self.LOSE
            return self.game_status
        if guess==self.answer:
            self.game_status = self.WIN
            return self.game_status
        self.guesses.append(guess)
        self.turn_number += 1
        return self.game_status


if __name__=="__main__":
    game = Game(word_source="web_simple")
    