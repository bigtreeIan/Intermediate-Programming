###Escaper:
###I write a escaper for special simulton, when user click special, it creates a special, which looks like a ball and is prey.
###However, escapers have the ability to detect the simultons that will eat them and try to avoid them.
###When escaper detect the simulton get in to its sight, it will speed up to run away.
###If a escaper survive for more than 30 time count, it will create a ball and a floater to divert attention from hunter

from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2, pi
from random import random
from floater import Floater
from ball import Ball

class Special(Prey):  
    safe_distance = 50
    def __init__(self, x, y):
        self.time_count = 0
        self.randomize_angle()
        Prey.__init__(self, x, y, 15, 15, self.get_angle(), 4)
    
    def update(self, model):
        self.time_count += 1
        target_simu = model.find(lambda x: isinstance(x, Prey) == False and self.distance(x.get_location()) <= Special.safe_distance)
        if target_simu != set():
            for target in target_simu:
                position_target = target.get_location()
                position_hunter = self.get_location()
                self.set_angle(pi - atan2(position_target[1] - position_hunter[1], position_target[0] - position_hunter[0])) 
            self.rs = self.get_speed() + random()
            self.set_speed(self.rs)
        if self.time_count > 30:
            model.simulton_module.add(Floater(self.get_location()[0],self.get_location()[1]))
            model.simulton_module.add(Ball(self.get_location()[0],self.get_location()[1]))
            self.time_count = 0
        self.move()
        
    def display(self, the_canvas):
        the_canvas.create_oval(self._x-self.get_dimension()[0], self._y-self.get_dimension()[1], self._x+self.get_dimension()[0], self._y+self.get_dimension()[1], fill = 'Red')
        