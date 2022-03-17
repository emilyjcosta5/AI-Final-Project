# Final Project Proposal

## Introduction

In this project, we create a game similar to Wordle, a recently popular game acquired by the New York Times. This game has captivated many of us, our friends, and family. The general rules are as follows:

1. There are six chances to guess the word.
2. The words you enter as guesses have to be on the word list, which consists of most common English words.
3. A correct letter in the correct position turns green.
4. A correct letter in the wrong position turns yellow.
5. An incorrect letter with no correct position turns gray.
6. Letters can occur in the word more than one time. 

It should be noted that, in our game, rule #2 will not apply as we will not have a word list but rather we will randomly generate letters to make a five letter word. This word may or may not be an actually word in the English language. The only possible restraint will be the letters that can be used to create a word. This is in order to constrain the number of possible words. Additionally, we do not always apply rule #1 so we can test the performance of the algorithms as the number of chances varies. These modifications can be regarded in terms of a combination where the size of the alphabet used to create the word is the total number of objects in the set, commonly regarded as `n`, and the number of letters in the word is the number of choosing objects from the set, or `r`.

We were inspired to do this because is a relatively simple game with few rules. We believe that several of the algorithms and techniques that we learned throughout this course would be applicable to this game. We can form a knowledge base and use different heuristics, implement a simple genetic algorithm, and much more!  

# Game Framework
We will create a class for an instance of the "game". We initiate this class with parameters such as number of guesses allowed, length of the word, and the instance of the algorithm used (which we will cover later).

First, we need to generate the "word of the day" which, in the real game of Wordle, is a selected word in which people can deduce that day. To do this, we created a class in which

# GUI

In this section, we discuss how we will implement the Graphical User Interface (GUI) for our selected game based off of Wordle. Within our code, this was key in setting up the framework in which we implement our selected algorithms.  

# Algorithms

1. *Genetic Algorithm*
