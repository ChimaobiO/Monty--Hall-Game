"""Monty Hall Game"""
import random

"""Class Simulation : Simulates Monty Hall game. ARGS : doornum - Number of Doors Being Played
    Methods: __init_ - Initalizer
    set_random_doors - sets the random doors that contains zonks and car
    choose_door - chooses random door for user"""

class Simulation:
    def __init__(self, doornum):
        
        """Init method: Checks if door number is  at least 3 before proceeding. Attribute Numdoors is configured to doornum. 
        ARGS: doornum
        NO RETURNS"""
        
        if doornum < 3:
            raise ValueError("Number of Doors must be at least 3")
        self.numdoors = doornum
    
    
    def set_random_doors(self):
        
        """ Set_Random_Doors: Creates List of doors using number of doors. Fills all but one door with zonks.
        ARGS: NONE
        Returns: doorlist"""
        
        doorlist = ["zonk" for amount in range(self.numdoors)]
        newstring = "car"
        replace = "zonk"
        positions = [i for i, x in enumerate(doorlist) if x == replace ]
        indexreplace = random.choice(positions)
        doorlist[indexreplace] = newstring
        return doorlist
    
    def choose_doors(self):
        
        """choose_doors - chooses two random doors for user. Reveals a 'zonk' door. 
        ARGS: NONE
        RETURNS: final - tuple of two random doors"""
        
        randomdoor = self.set_random_doors()
        door = random.choice(randomdoor)
        randomdoor.remove(door)
        removing = "zonk"
        randomdoor.remove(removing)
        altdoor = random.choice(randomdoor)
        randomdoor.remove(altdoor)
        final = (door, altdoor)
        return final
    
    def play_game(self, switch = False, iterations = 1):
        
        """play_game - plays the monty hall game. Keeps track of wins, loses, and win percentage.
        ARGS: switch - Allows user to choose if wants to switch inital choice. defualts to false
              iterations - number of times user wants to play the game. - defaults to 1
        RETURNS: result - floating point average of win percentage."""
        
        win = 0
        lose = 0
        for games in range(iterations):
            game = self.choose_doors()
            if game[0] == "car" and switch == False or game[1] == "car" and switch == True:
                win += 1
            else:
                lose += 1
        total = win + lose
        result = float((win/total))
        return result
if __name__ == "__main__":
    Instance = Simulation(3)
    print(Instance.play_game(True, 1000))
            
            
        