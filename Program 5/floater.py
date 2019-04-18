# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    def __init__(self, x, y):
        self.ufo = PhotoImage(file = 'ufo.gif')
        self.randomize_angle()
        ufo_width = self.ufo.width()
        ufo_height = self.ufo.height()
        Prey.__init__(self, x, y, ufo_width, ufo_height, self.get_angle(), 5)
    
    def update(self, model):
        random_time = random()
        if random_time <= 0.3:
            random_speed_num = random()
            if random_speed_num < 0.5 and -random_speed_num > -0.5:
                self.random_speed = self.get_speed() + random_speed_num
                if self.random_speed > 3.0 and self.random_speed < 7.0:
                    self.set_speed(self.random_speed)
            random_angle_num = random()
            if random_angle_num < 0.5 and -random_angle_num > -0.5:
                self.random_angle = self.get_angle() + random_angle_num
                self.set_angle(self.random_angle)
        self.move()
    
    def display(self, the_canvas):
        the_canvas.create_image(*self.get_location(), image = self.ufo)