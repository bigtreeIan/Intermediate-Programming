# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions

'''Write, test, and debug the Pulsator class. Ensure the user can add Pulsators to the simulation. 
Each Pulsator behaves and initially looks like a Black_Hole, except for the following additional behavior. 
For every object a Pulsator eats, its dimension (both width and length) grows by 1 and its "time between meals" counter is reset; 
whenever it is goes 30 updates without eating anything, its dimension (both width and length) shrinks by 1; 
and if the dimesions ever shrink to 0, the object starves and removes itself from the simulation. 
The update method should still return the set of simultons eaten. 
Hint: 2 methods (__init__ and update), 1 self variable -for that pulsator's counter-, 
and 1 class variable for the counter constant of 30).'''

from blackhole import Black_Hole


class Pulsator(Black_Hole):
    death_num = 30
    def __init__(self, x, y):
        self.time_count = 0
        Black_Hole.__init__(self, x, y)
    
    def update(self, model):
        self.time_count += 1
        ball_eaten = Black_Hole.update(self, model)
        if self.time_count == Pulsator.death_num:
            if ball_eaten == set():
                self.change_dimension(-1, -1)
                self.time_count = 0
            if ball_eaten != set():
                self.time_count = 0
        if ball_eaten != set():
            for ball in ball_eaten:
                self.change_dimension(1, 1)
                self.time_count = 0    
        wid = self.get_dimension()[0]
        if wid == 0:
            model.remove(self)
        
                
                
                         
            
            
        
        
        
        