import enum
from lib2to3.pytree import Base
from game import WordleGame
import random

class BaseAlgorithm:
    '''
    Serves as the basis for how our algorithm should be structured
    and the methods that need to be implemented.
    '''
    def __init__(self, word_list, Verbose=False) -> None:
        self.word_list = word_list
        self.Verbose = Verbose
        self.guesses = []
        self.bad_letters = []
        self.good_letters = []
        self.right_position = {}

    def reset(self):
        self.guesses = []
        self.bad_letters = []
        self.good_letters = []
        self.right_position = {}

    def create_tree(self, word):
        '''
        This will need to be implemented for those who need a tree to conduct a search.

        Notes: I would make this so it updates based on a new root word then the possible words
        as branches or leafs.

        it may look something like https://www.poirrier.ca/notes/wordle/ except more simple. 
        recursion might be useful for this.
        '''
        # TO-DO
        pass
    
    def make_guess(self) -> str:
        pass

class HumanAlgorithm(BaseAlgorithm):
    '''
    Meant to mimic the typical human strategy; picks a random word that
    is possible given the feedback on the most previous word.
    '''
    def __init__(self, word_list) -> None:
        super().__init__(word_list)

    def make_guess(self, previous_guess=None) -> str:
        if previous_guess==None:
            guess = random.choice(self.word_list)
            return guess
        p_guess, squares = previous_guess
        for idx, square in enumerate(squares):
            if square=="GREY":
                self.bad_letters.append(p_guess[idx])
            elif square=="YELLOW" or square=="GREEN":
                self.good_letters.append(p_guess[idx])
            else:
                self.right_position[idx]==p_guess[idx]
        possible_words = [word for word in self.word_list if \
                            all(good_letter in word for good_letter in self.good_letters) \
                            and \
                            all(bad_letter not in word for bad_letter in self.bad_letters) \
                            and \
                            all(word[i]==self.right_position[i] for i in self.right_position.keys())]
        guess = random.choice(possible_words)
        return guess

class GreedyDepthAlgorithm(BaseAlgorithm):
    '''
    Pick the words by finding the path to minimal depth which basically minimizes the pool
    of possible words as the algorithm gets feedback.
    
    Implemenation is inspired by: https://towardsdatascience.com/automatic-wordle-solving-a305954b746e
    '''
    def __init__(self, word_list, Verbose=False) -> None:
        super().__init__(word_list, Verbose)

    def make_guess(self) -> str:
        # TO-DO
        return super().make_guess()

class GreedyBreadthAlgorithm(BaseAlgorithm):
    '''
    Similar to GreedyDepthAlgorithm but searches the word tree using breadth
    first search. I imagine this will be optimal since we would stop the search
    once a leaf is found (which provides the shortest branch such that we would 
    want to pick the child of the root that brings us there).
    '''
    def __init__(self, word_list, Verbose=False) -> None:
        super().__init__(word_list, Verbose)
    
    def make_guess(self) -> str:
        # TO-DO
        return super().make_guess()

if __name__=="__main__":
    # manual tests on algorithms
    game = WordleGame()
    # 1. Human
    algo = HumanAlgorithm(word_list=game.get_word_list())
    # 2. Greedy Depth
    #algo = GreedyDepthAlgorithm(word_list=game.get_word_list())
    # etc...

    game_status = game.get_game_status()
    while game_status==0:
        game.guess(algo.make_guess(game.get_last_guess()))
        game_status = game.get_game_status()
        if game_status==0 and game.get_last_guess():
            guess, squares = game.get_last_guess()
            print('%s: %s'%(guess, ' '.join(squares)))
        elif game_status==1:
            try_again = input("You won! Play another game? (Y/N) ")
            if try_again=='Y':
                game = WordleGame()
                algo.reset()
                game_status = game.get_game_status()
            else:
                print("OK. Bye-bye!")
                break
        elif game_status==-1:
            try_again = input("You lose. Try again? (Y/N) ")
            if try_again=='Y':
                game.restart()
                algo.reset()
                game_status = game.get_game_status()
            else:
                print("OK. Bye-bye!")
                break