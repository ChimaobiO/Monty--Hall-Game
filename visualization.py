"""Visulization of wins and loses for monty hall game"""

import monty_hall
import pandas as pd
import seaborn as sns

class Plot:
    
    """Class Plot: Plots monty hall win percentage on plot.
       ARGS: doors - number of doors. defaults to 3
            Iterations - number of games played. defaults to 200
        METHODS: __init__: Intializer
                make plot : Makes plot of monty hall game"""
       
    def __init__(self, doors=3, iterations=200):
        
        """init method: creates instance of simulation class and saves win percentage of monty hall game using play_game method. Creates data used in dataframe.
        ARGS: doors - number of doors played. defualts to 3
              iterationns  - number of games played. defaults to 200
        NO RETURNS"""
        
        self.attributes = []
        self.doors = doors
        self.iterations = iterations
        for i, amount in enumerate(range(iterations)):
            if i % 2 == 0:
                switched = True
            else:
                switched = False
            P = monty_hall.Simulation(doors)
            win_percentage = P.play_game(switched, iterations)
            self.attributes.append({
                "Iteration": i,
                "Percentage": win_percentage,
                "Doors": doors,
                "Switched": switched
            })
    def make_plot(self):
        
        """ make_plot: creates plot of data from __init__ method.
        NO ARGS
        NO RETURNS"""
        
        df = pd.DataFrame(self.attributes)
        plot = sns.lmplot(x = "Iteration", y = "Percentage", hue = "Switched", data = df)
        plot.savefig(f"monty_hall_{self.doors}_doors_{self.iterations}_iterations.png")
if __name__ == "__main__":
    Instance = Plot(5,100)
    Instance.make_plot()


                
            