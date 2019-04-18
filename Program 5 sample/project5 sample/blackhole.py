# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey

class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, 20, 20)
        
    def update(self,model):  
        result=set()  
        temp=model.find(lambda a:isinstance(a,Prey))
        for i in temp:
            if self.contains(i.get_location()):
                result.add(i)
                model.remove(i)
        return result
    
    def display(self,canvas):
        canvas.create_oval(self._x-self.get_dimension()[0],
                           self._y-self.get_dimension()[1],
                           self._x+self.get_dimension()[0],
                           self._y+self.get_dimension()[1],
                           fill='Black')

    def contains(self,xy):
        return self._x-self.get_dimension()[0]/2  <= xy[0] <= self._x+self.get_dimension()[0]/2 and\
               self._y-self.get_dimension()[1]/2 <= xy[1] <= self._y+self.get_dimension()[1]/2














