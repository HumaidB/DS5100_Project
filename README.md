"""
--------------------
MetaData:
--------------------

Monte Carlo Package
Author: Humaid Billoo
Version: 1.0
Date: May 1 2025

Description:
This package simulates Monte Carlo using a set
of three related classes — a Die class, a Game class, and an Analyzer
class. counts, and permutations.

--------------------
Synopsis:
--------------------

from montecarlo import Die, Game, Analyzer
import numpy as np

# CLASS DIE USES
faces = np.array([1, 2, 3, 4, 5, 6])
die = Die(faces)
die.change_weight(6, 5)
die.roll(1000)
die.show()

# CLASS GAME USES
die1 = Die(np.array([1, 2, 3, 4, 5, 6])
die2 = Die(np.array([1, 2, 3, 4, 5, 6])
die3 = Die(np.array([1, 2, 3, 4, 5, 6])
game = Game([die1, die2, die3])
game.play(1000)
game.show(view='narrow')

# CLASS ANALYZER USES
analyzer = Analyzer(game)
analyzer.jackpot()
analyzer.face_counts_per_roll()
analyzer.combo_count()
analyzer.permutation_counts()

--------------------
API Reference:
--------------------

Die Class:
----------
-__init__(self, faces):
        Initializer, it takes a Numpy array and makes sure
        that it is being passed and assures the faces on the die are unique and sets
        the weights to  1.
        Args: faces
        Return: None
- change_weight(self, face, new_weight):
        A method to change the weight of a single side:
        Takes two arguments: the face value to be changed and the new
        weight. Error checks to make sure face is in array and weight is numeric 
        Args: face, new_weight
        Return: None'''
- roll(self, rolls=1):
        A method to roll the die one or more times:
        Takes a parameter of how many times the die is to be rolled
        Args: rolls =1,
        Return outcomes
- show(self):
        Returns the Die Dataframe
        Args: Self,
        Return:self._die

Game Class:
-----------
- __init__(self, dice):
        Initializer, Takes a single parameter, a list of already instantiated similar
        dice
- play(self, num_rolls):
        Takes an integer parameter to specify how many times the dice should
        be rolled and Saves the result of the play to a data frame
        Args: num_rolls
        Return: None
- show(self, view="wide"):
        This method  returns a copy of the  play data frame
        Args: view = wide
        Return: Data frame

Analyzer Class:
---------------
- __init__(self, game):
        Iniatializer, Takes a game object as its input parameter
        args: game
- face_counts_per_roll(self):
        Computes how many times a given face is rolled in each even
        and returns data frame of results
- def combo_count(self):
        Computes the distinct combinations of faces rolled, along with their
        counts and returns a data frame of results
- permutation_counts(self):
        Computes the distinct permutations of faces rolled, along with their
        counts and returns a data frame of results

"""
