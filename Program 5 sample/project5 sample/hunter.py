# A Hunter is both a  Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    eye = 200
    
    def __init__(self,x,y):
        self.randomize_angle()
        Mobile_Simulton.__init__(self, x, y, 20, 20,self.get_angle(),5)
        Pulsator.__init__(self, x, y)
        
    def update(self,model):
        temp=model.find(lambda a:isinstance(a,Prey))
        for i in temp:
            if self.distance(i.get_location())<=Hunter.eye:
                self.set_angle(atan2(i.get_location()[1]-self.get_location()[1],i.get_location()[0]-self.get_location()[0]))
        Pulsator.update(self,model)
        self.move()
                
                
                
                
                
                
                
                
                
                
                
        
