import numpy
from numpy import sort
from game import WordleGame
import random
import math
from itertools import product

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
            self.guesses.append(guess)
            return guess
        p_guess, squares = previous_guess
        for idx, square in enumerate(squares):
            if square=="GREY":
                self.bad_letters.append(p_guess[idx])
            if square=="YELLOW" or square=="GREEN":
                self.good_letters.append(p_guess[idx])
            if square=="GREEN":
                self.right_position[idx] = p_guess[idx]
        possible_words = [word for word in self.word_list if \
                            all(good_letter in word for good_letter in self.good_letters) \
                            and \
                            all(bad_letter not in word for bad_letter in self.bad_letters) \
                            and \
                            all(word[i]==self.right_position[i] for i in self.right_position.keys()) \
                            and \
                            word not in self.guesses]
        guess = random.choice(possible_words)   
        self.guesses.append(guess)
        return guess


class NaiveFrequencyAlgorithm(BaseAlgorithm):
    '''
    Pick the words by counting the number of words a letter appears in and then selecting the word with
    aggregate highest number of its 5 letters

    We will ignore the duplicate characters in a word while calculating the aggregate

    Implementation inspired by - https://ido-frizler.medium.com/the-science-behind-wordle-67c8112ed0d1
    '''

    def __init__(self, word_list) -> None:
        super().__init__(word_list)
        self.remaining_word_list = self.word_list

    def countCharacterFrequency(self) -> dict:
        countDict = {}
        for i in range(ord('a'),ord('z')+1):
            countDict[chr(i)] = 0
        for i in self.remaining_word_list:
            unique_chars = set(list(i.lower().strip()))
            for c in unique_chars:
                countDict[c]+=1
        return countDict

    def make_guess(self,previous_guess=None) -> str:
        
        if previous_guess==None:
            guess = random.choice(self.word_list)
            self.guesses.append(guess)
            return guess

        p_guess, squares = previous_guess
        for idx, square in enumerate(squares):
            if square=="GREY":
                self.bad_letters.append(p_guess[idx])
            if square=="YELLOW" or square=="GREEN":
                self.good_letters.append(p_guess[idx])
            if square=="GREEN":
                self.right_position[idx] = p_guess[idx]
        self.remaining_word_list = [word for word in self.word_list if \
                            all(good_letter in word for good_letter in self.good_letters) \
                            and \
                            all(bad_letter not in word for bad_letter in self.bad_letters) \
                            and \
                            all(word[i]==self.right_position[i] for i in self.right_position.keys()) \
                            and \
                            word not in self.guesses]
        
        frequency = self.countCharacterFrequency()

        max_aggregate = 0
        guess = ""

        for i in self.remaining_word_list:
            agg_freq = 0
            for j in set(list(i.lower().strip())):
                agg_freq+=frequency[j]
            if(agg_freq>max_aggregate):
                max_aggregate = agg_freq
                guess = i
        self.guesses.append(guess)
        return guess
        


class MaxEntropyAlgorithm(BaseAlgorithm):
    '''
    Information Theory based implementation
    Guess the word by selecting the word with highest entropy from the available word list.
    It basically means that we want to reduce the number of possible words matching the existing pattern.
    The more small the space of possible words is after a guess, more will be the information gain.

    Implementation inspired by - https://towardsdatascience.com/information-theory-applied-to-wordle-b63b34a6538e
    Youtube(3 Blue 1 Brown) - https://youtu.be/v68zYyaEmEA
    '''

    def __init__(self, word_list) -> None:
        super().__init__(word_list)
        self.remaining_word_list = self.word_list

    def calculate_entropy(self,word) -> float:
        patterns = {}
        for w in self.remaining_word_list:
            p = ""
            for i in range(len(w)):
                if w[i]==word[i]:
                    p+="g"
                elif w[i] in word:
                    p+="y"
                elif w[i] not in word:
                    p+="b"
            if p in patterns:
                patterns[p]+=1
            else:
                patterns[p]=1
                
        entropy = 0
        for k,v in patterns.items():
            if v!=0:
                prob = v/len(self.remaining_word_list)
                info = -1 * math.log(prob,2)
                entropy+=prob*info
                
        return entropy
    

    def make_guess(self,previous_guess=None) -> str:
        
        if previous_guess==None:
            guess = random.choice(self.word_list)
            self.guesses.append(guess)
            return guess
        
        
        p_guess, squares = previous_guess
        for idx, square in enumerate(squares):
            if square=="GREY":
                self.bad_letters.append(p_guess[idx])
            if square=="YELLOW" or square=="GREEN":
                self.good_letters.append(p_guess[idx])
            if square=="GREEN":
                self.right_position[idx] = p_guess[idx]

        self.remaining_word_list = [word for word in self.word_list if \
                            all(good_letter in word for good_letter in self.good_letters) \
                            and \
                            all(bad_letter not in word for bad_letter in self.bad_letters) \
                            and \
                            all(word[i]==self.right_position[i] for i in self.right_position.keys()) \
                            and \
                            word not in self.guesses]
        
        
        max_entropy = 0
        guess = random.choice(self.remaining_word_list)

        for word in self.remaining_word_list:
            entropy = self.calculate_entropy(word)
            if(entropy>max_entropy):
                max_entropy = entropy
                guess = word
            
        
        self.guesses.append(guess)
        return guess

    
    
class GreedyDepthAlgorithm(BaseAlgorithm):
    '''
    Pick the words by finding the path to minimal depth which basically minimizes the pool
    of possible words as the algorithm gets feedback.
    
    Implemenation is inspired by: https://towardsdatascience.com/automatic-wordle-solving-a305954b746e
    '''
    def __init__(self, word_list, Verbose=False) -> None:
        super().__init__(word_list, Verbose)
        self.word_list = word_list
        self.best_words = self.find_best_words()
    
    def find_best_words(self):
        count = 0
        best_words = {}
        for answer in self.word_list:
            for guess in self.word_list:
                if count > 0:
                    points = best_words[guess]
                else:
                    points = 0
                for i, letter in enumerate(guess):
                    if letter == answer[i]:
                        points +=2
                    elif letter in answer:
                        points +=1
                    else:
                        points += 0

                best_words[guess] = points
            count+=1
        
        best_words = dict(sorted(best_words.items(), key=lambda item: item[1], reverse=True)).keys()
        return best_words

    def make_guess(self, previous_guess=None) -> str:
        
        if previous_guess==None:
            guess = self.best_words[0]
            self.guesses.append(guess)
            return guess

        p_guess, squares = previous_guess
        for idx, square in enumerate(squares):
            if square=="GREY":
                self.bad_letters.append(p_guess[idx])
            if square=="YELLOW" or square=="GREEN":
                self.good_letters.append(p_guess[idx])
            if square=="GREEN":
                self.right_position[idx] = p_guess[idx]

        remaining_words = [word for word in self.word_list if \
                            all(good_letter in word for good_letter in self.good_letters) \
                            and \
                            all(bad_letter not in word for bad_letter in self.bad_letters) \
                            and \
                            all(word[i]==self.right_position[i] for i in self.right_position.keys()) \
                            and \
                            word not in self.guesses]
        
        for key in self.best_words.keys:
            if key not in remaining_words:
                self.best_words.pop(key)
        
        guess = self.best_words
        
        return guess

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
    #algo = HumanAlgorithm(word_list=game.get_word_list())
    #2. Aggregated Frequency
    #algo = NaiveFrequencyAlgorithm(word_list=game.get_word_list())
    # 4. Greedy Depth
    #algo = GreedyDepthAlgorithm(word_list=game.get_word_list())
    # etc...

    choice = 1
    print("Select an Algorithm:\
          \n1.Human Algorithm\
          \n2.Aggregated Frequency\
          \n3.Entropy Maximization\
          \n4.Greedy Depth")
    
    choice = int(input())
    if choice == 1:
        algo = HumanAlgorithm(word_list=game.get_word_list())
    elif choice == 2:
        algo = NaiveFrequencyAlgorithm(word_list=game.get_word_list())
    elif choice == 3:
        algo = MaxEntropyAlgorithm(word_list=game.get_word_list())
    elif choice == 4:
        algo = GreedyDepthAlgorithm(word_list=game.get_word_list())

    best_words = algo.best_words

    print(best_words)

    #print("ANSWER:",game.answer)
    # game_status = game.get_game_status()
    # while game_status==0:
    #     game.guess(algo.make_guess(game.get_last_guess()))
    #     game_status = game.get_game_status()
    #     if game_status==0 and game.get_last_guess():
    #         guess, squares = game.get_last_guess()
    #         print('%s: %s'%(guess, ' '.join(squares)))
    #     elif game_status==1:
    #         guess, squares = game.get_last_guess()
    #         print('%s: %s'%(guess, ' '.join(squares)))
    #         try_again = input("You won! Play another game? (Y/N) ")
    #         if try_again=='Y':
    #             game = WordleGame()
    #             algo.reset()
    #             game_status = game.get_game_status()
    #         else:
    #             print("OK. Bye-bye!")
    #             break
    #     elif game_status==-1:
    #         guess, squares = game.get_last_guess()
    #         print('%s: %s'%(guess, ' '.join(squares)))
    #         try_again = input("You lose. Try again? (Y/N) ")
    #         if try_again=='Y':
    #             game.restart()
    #             algo.reset()
    #             game_status = game.get_game_status()
    #         else:
    #             print("OK. Bye-bye!")
    #             break
