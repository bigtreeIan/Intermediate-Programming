# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    the_truth_of_the_world = 30
    
    def __init__(self,x,y):
        self._truth=0
        Black_Hole.__init__(self, x, y)
        
    def update(self,model):
        self._truth+=1
        temp = Black_Hole.update(self,model)
        if len(temp)==0 and self._truth==Pulsator.the_truth_of_the_world:
            self.change_dimension(-1,-1)
            self._truth = 0
        elif self.get_dimension()==(0,0):model.remove(self)
        else:
            for i in range(len(temp)):
                self.change_dimension(1,1)
                self._truth = 0
        return temp
    
    
    
    
    
    
    
    
    
    
    
    
    