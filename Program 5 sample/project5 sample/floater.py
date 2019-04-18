# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    
    def __init__(self,x,y):
        self._image = PhotoImage(file='ufo.gif')
        self.randomize_angle()
        Prey.__init__(self, x, y, self._image.width(), self._image.height(), self.get_angle(),5)
        
    def update(self,model):
        if random()<=0.3:
            if random()<=0.5:
                self.set_angle(self.get_angle()+random()*0.5)
                if self.get_speed()+random()*0.5>=3.0 and self.get_speed()+random()*0.5<=7.0:
                    self.set_speed(self.get_speed()+random()*0.5)  
        self.move()
        
        
    def display(self,canvas):
        canvas.create_image(*self.get_location(),image=self._image)

