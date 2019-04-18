'''
span balls
'''

import model
from ball import Ball
from simulton import Simulton


class Special(Simulton):
    radius = 10
    another_truth_of_the_world = 10
    
    def __init__(self,x,y):
        self._truth=0
        Simulton.__init__(self, x, y, 20, 20)
        
    def update(self,model):
        self._truth+=1
        if self._truth==Special.another_truth_of_the_world:
            self._truth=0
            model.simu.add(Ball(self.get_location()[0],self.get_location()[1]))

    def display(self,canvas):
        canvas.create_oval(self._x-self.get_dimension()[0],
                           self._y-self.get_dimension()[1],
                           self._x+self.get_dimension()[0],
                           self._y+self.get_dimension()[1],
                           fill='Purple')
        
