# Final Project Proposal

## Introduction

In this project, we create a game similar to Wordle, a recently popular game acquired by the New York Times. This game has captivated many of us, our friends, and family. We were inspired to do this because is a relatively simple game with few rules. We believe that several of the algorithms and techniques that we learned throughout this course would be applicable to this game. We can form a knowledge base and use different heuristics, implement a simple genetic algorithm, and much more!

The general rules are as follows:

1. There are six chances to guess the word.
2. The words you enter as guesses have to be on the word list, which consists of most common English words.
3. A correct letter in the correct position turns green.
4. A correct letter in the wrong position turns yellow.
5. An incorrect letter with no correct position turns gray.
6. Letters can occur in the word more than one time. 

It should be noted that, in our game, rule #2 will not apply as we will not have a word list but rather we will randomly generate letters to make a five letter word. This word may or may not be an actually word in the English language. The only possible restraint will be the letters that can be used to create a word. This is in order to constrain the number of possible words. 

However, we may still opt to use words from the English language that a predefined as a word list. We also may sticking to only words 5 letters long but that will be up to our discretion as we complete the project. It mainly depends on the algorithms that we implement and how they may operate. 

Additionally, we may not always apply rule #1 so we can test the performance of the algorithms as the number of chances varies. 

# Game Framework
We will create a class for an instance of the "game". We initiate this class with parameters such as number of guesses allowed, length of the word, number of letters in the alphabet used to create the word, and the instance of the algorithm used (which we will cover later). This `Game` class will essentially serve as the framework in which we create the game, track the moves made, give feedback to the algorithm and GUI, and determine the results of the game. 

First, we need to generate the "word of the day" which, in the real game of Wordle, is a selected word in which people can deduce that day. This is something that can be set automatically when a new instance of a `Game` is created. We simply create a method, `set_word`, that generates a random word. It may be interesting to give more weight, or likelihood, to some letters as we humans typically do use certain letters more than others so we may explore that during our project.

As previously mentioned in the introduction, rules #1 and #2 may be modified during our project to allow for more experimentation. These modifications can be regarded in terms of a combination where the size of the alphabet used to create the word is the total number of objects in the set, commonly regarded as `n`, and the number of letters in the word is the number of choosing objects from the set, or `r`. Therefore, we use the following combination formula to calculate the number of possible words and measure the performance of the algorithm:

`C(n,r)=n!/(r!(n-r)!)`

Again, we may opt for a word list which means that the approach of generating a word will vary from a randomly generated word.

Next, we will need to set up a method for inputing a guess then outputting the result. The input would be the guess provided by the algorithm (or, if the algorithm is known to the object, the method would calculate a guess itself). Then, the method would need to check if the guess is valid based on our criteria. Finally, the result of the guess accuracy would be given. The result would need to include the green, yellow, and grey square or, at the end, whether the user won the game. 

One idea for the game strucutre is for us to implement a method that effectively restarts the game so that the different algorithms can play the same exact game for us to better measure the performance of the implemented algorithms. The only thing that would not be reset is the word that is the answer of the particular game which includes the aspect of two of the initial inputs, the length of the word and alphabet.

Finally, we discuss how the framework will interact with the algorithm. Basically, we implement a `Algorithm` class that serves as a Parent class for our algorithm implementations. The specifics of this will be further outlined in the Algorithms section later in our proposal. Our main idea on this is to structure it similar to other code we previously dealt with in this class. The Game object will take input as the next guess while the Algorithm object will make decisions of the guess based on feedback from the Game object. 

# GUI
In this section, we discuss how we will implement the Graphical User Interface (GUI) for our selected game based off of Wordle. The layout for the GUI should be relatively simple; we will have a n by m box grid where n is the length of the word and m is the number of guesses allowed. The boxes will display the input given by row and also show the color of the box determined by the accuracy of the input. There are several Python libraries for simple GUIs that we will explore during the project. We may use previously developed code and would site that if that is the case.  

We will also implement a way for a human to interact with the game (or, at least, a human-like decision algorithm) in order to serve as a baseline for the performance of our algorithms.

# Algorithms
For the most significant portion of our project, we will implement a Parent class, `Algorithm`, that will serve as the Parent class for all the algorithms that we will implement. Within our code, this was key in setting up the framework in which we implement our selected algorithms. Each specific algorithm implemented will make guesses based on their criteria then the guess will be used as input for the game. The main method necessary in all the algorithms will be one that outputs a guess given acquired knowledge from the feedback of the Game (think green, yellow, and grey squares). To make this simpler, the algorithm will always be given an initial hint from the Game in the form of feedback from a randomly guess word.

The following are some ideas we have for algorithms to implement, but may modify this list as we discover other algorithms throughout this class:

1. *Genetic Algorithm*: 
2. *Greedy Min Max*: minimize remaining possible word guesses with every guess
3. 

# Sources
https://arxiv.org/abs/2202.00557

https://towardsdatascience.com/automatic-wordle-solving-a305954b746e

https://github.com/yotam-gafni/wordle\_solver
