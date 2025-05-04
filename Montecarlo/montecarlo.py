import numpy as np
import pandas as pd

##########  DIE ##########
class Die:
    ''' Die Class and it has four methods:''' 
    def __init__(self, faces):
        ''' Initializer, it takes a Numpy array and makes sure
        that it is being passed and assures the faces on the die are unique and sets
        the weights to  1.
        Args: faces
        Return: None'''

        # Make sure faces is numpy array
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces is not a NumPy array.")
        if len(faces) != len(np.unique(faces)):
            raise ValueError("Faces are not unique.")
        
        # Values are unique
        self._die = pd.DataFrame({
            "face": faces,
            "weight": np.ones(len(faces))
            }).set_index("face")
        
    def change_weight(self, face, new_weight):
            ''' A method to change the weight of a single side:
            Takes two arguments: the face value to be changed and the new
            weight. Error checks to make sure face is in array and weight is numeric
            Args: face, new_weight
            Return: None'''

            # must be proper name in die
            if face not in self._die.index:
                raise IndexError("Face not in the die.")
            
            # must be numeric
            try:
                new_weight = float(new_weight)
            except ValueError:
                raise TypeError("Weight is not numeric.")
            self._die.loc[face, "weight"] = new_weight

    def roll(self, rolls=1):
        '''A method to roll the die one or more times:
        Takes a parameter of how many times the die is to be rolled
        Args: rolls =1,
        Return outcomes'''
        outcomes = self._die.sample(
            n=rolls,
            replace=True,
            weights=self._die["weight"]
            ).index.tolist()
        return outcomes

    def show(self):
        '''Returns the Die Dataframe
        Args: Self,
        Return:self._die'''
        return self._die


##########  Game    ##########

class Game:
    ''' Game Class and it has four methods:'''

    def __init__(self, dice):
        '''Initializer, Takes a single parameter, a list of already instantiated similar
    dice'''
        self._dice = dice

    def play(self, num_rolls):
        '''Takes an integer parameter to specify how many times the dice should
    be rolled and Saves the result of the play to a data frame
        Args: num_rolls
        Return: None'''
        data = {}
        for i, die in enumerate(self._dice):
            rolls = [die.roll()[0] for j in range(num_rolls)]
            data[i] = rolls
        self._play = pd.DataFrame(data)
        self._play.index.name = "Roll Number"
        
    def show(self, view="wide"):
        '''This method  returns a copy of the  play data frame
        Args: view = wide
        Return: Datfframe'''
        if view == "wide":
            return self._play.copy()
        elif view == "narrow":
            narrow = self._play.stack()
            narrow.index.names = ["Roll Number", "Die Number"]
            narrow.name = "Outcome"
            return narrow.to_frame()
        else:
            raise ValueError("view is not 'wide' or 'narrow'")
        
##########  Analyzer    ##########

class Analyzer:
    '''Takes the results of a single game and computes
various descriptive statistical properties about it, has five methods'''
    def __init__(self, game):
        '''Iniatializer, Takes a game object as its input parameter
        args: game'''
        if not isinstance(game, Game):
            raise ValueError("Input is not a Game object")
        self.game = game
        self.results = game._play

    def jackpot(self):
        '''jackpot is a result in which all faces are the same,
        Computes how many times the game resulted in a jackpot,
        and Returns an integer for the number of jackpots'''
        jackpotcnt = 0
        for roll_number in range(len(self.results)):
            row = self.results.iloc[roll_number]
            first_face = row.iloc[0]
            YNjackpot = True
            for value in row:
                if value != first_face:
                    YNjackpot = False
                    break 
            if YNjackpot:
                jackpotcnt += 1

        return jackpotcnt

    def face_counts_per_roll(self):
        '''Computes how many times a given face is rolled in each even
        and returns data frame of results'''
        allcnt = []
        minface = int(self.results.min().min())
        maxface = int(self.results.max().max())
        for roll_number in range(len(self.results)):
            row = self.results.iloc[roll_number]
            counts = {}
            for face in range(minface, maxface + 1):
                counts[face] = 0
            for value in row:
                counts[value] += 1
            allcnt.append(counts)
        facecnt = pd.DataFrame(allcnt)
        facecnt.index.name = "Roll Number"
        return facecnt

    def combo_count(self):
        '''Computes the distinct combinations of faces rolled, along with their
        counts and returns a data frame of results'''
        lstcombo = []
        for roll_number in range(len(self.results)):
            row = self.results.iloc[roll_number]
            sorted_row = tuple(sorted(row.tolist()))
            lstcombo.append(sorted_row)
        combocnt = {}
        for combo in lstcombo:
            if combo in combocnt:
                combocnt[combo] += 1
            else:
                combocnt[combo] = 1
        combo_df = pd.DataFrame.from_dict(combocnt, orient="index", columns=["Count"])
        multi_index = pd.MultiIndex.from_tuples(combo_df.index, names=["Die {i+1}" for i in range(len(self.results.columns))])
        combo_df.index = multi_index
        return(combo_df)

    def permutation_counts(self):
        ''' Computes the distinct permutations of faces rolled, along with their
        counts and returns a data frame of results'''
        perms_list = []
        for roll_number in range(len(self.results)):
            row = self.results.iloc[roll_number]
            row_tuple = tuple(row.tolist())
            perms_list.append(row_tuple)
        cntperm = {}
        for perm in perms_list:
            if perm in cntperm:
                cntperm[perm] += 1
            else:
                cntperm[perm] = 1

        perm_df = pd.DataFrame.from_dict(cntperm, orient="index", columns=["Count"])
        multi_index = pd.MultiIndex.from_tuples(perm_df.index, names=["Die {i+1}" for i in range(len(self.results.columns))])
        perm_df.index = multi_index

        return perm_df
