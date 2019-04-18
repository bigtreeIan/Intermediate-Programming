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
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)
    
    def contains(self, xy):
        dimension = self.get_dimension()
        wid = dimension[0]
        rad = wid / 2
        return rad >= self.distance(xy)
        
    def update(self, model):
        eaten_set = set()
        ball_in = model.find(lambda x: isinstance(x, Prey) and self.contains(x.get_location()))
        for ball in ball_in:
            eaten_set.add(ball)
            model.remove(ball)
        return eaten_set
    
    def display(self, the_canvas):
        dimension = self.get_dimension()
        wid = dimension[0]
        rad = wid / 2
        the_canvas.create_oval(self._x - rad, self._y - rad, self._x + rad, self._y + rad, fill = 'Black')
        
        
                
        