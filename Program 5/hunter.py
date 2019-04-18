# A Hunter is both a Mobile_Simulton and a Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2

class Hunter(Pulsator, Mobile_Simulton):
    search_distance = 200
    def __init__(self, x, y):
        self.randomize_angle()
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, self._width, self._height, self.get_angle(), 5)
        
    def update(self, model):
        target_simu = model.find(lambda x: isinstance(x, Prey) and self.distance(x.get_location()) <= Hunter.search_distance)
        for target in target_simu:
            position_target = target.get_location()
            position_hunter = self.get_location()
            self.set_angle(atan2(position_target[1] - position_hunter[1], position_target[0] - position_hunter[0]))
        Pulsator.update(self, model)
        self.move()
                
            
        