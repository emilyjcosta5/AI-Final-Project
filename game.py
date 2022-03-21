from multiprocessing.sharedctypes import Value
import requests
import random

class Game:
    def __init__(self, word_length=5, word_source="manual", word_list=None, number_guesses=6):
        """
        Initiates the Game class

        Parameters
        ----------

        Returns
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

    def restart(self):
        pass

if __name__=="__main__":
    game = Game(word_source="web_simple")