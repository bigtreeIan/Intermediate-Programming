import prompt,re
import math
from goody import type_as_str

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        for item in self.x, self.y, self.z:
            assert type(item) is int, 'Point.__init__: x('+str(item)+') must be an int.'
        
    def __repr__(self):
        return 'Point({a},{b},{c})'.format(a = self.x, b = self.y, c = self.z)
        
    def __str__(self):
        return "({a},{b},{c})".format(a = 'x=' + str(self.x), b = 'y=' + str(self.y), c = 'z=' + str(self.z))
    
    def __bool__(self):
        return not all(coords == 0 for coords in (self.x,self.y,self.z))
        
    def __add__(self, given_point):
        if type(given_point) == Point:
            new_point1 = Point(self.x + given_point.x, self.y + given_point.y, self.z + given_point.z)
        elif type(given_point) != Point:
            raise TypeError('The given parameter should be a Point')
        return new_point1
    
    def __mul__(self, multi):
        if type(multi) == int:
            new_point2 = Point(self.x*multi, self.y*multi, self.z*multi)
        elif type(multi) != int:
            raise TypeError('The given parameter should be a integer')
        return new_point2
    
    def __rmul__(self, multi):
        if type(multi) == int:
            new_point2 = Point(self.x*multi, self.y*multi, self.z*multi)
        elif type(multi) != int:
            raise TypeError('The given parameter should be a integer')
        return new_point2

    def __lt__(self, pif):
        if type(pif) == Point:
            dis1 = math.sqrt(self.x**2 + self.y**2 + self.z**2) 
            dis2 = math.sqrt(pif.x**2 + pif.y**2 + pif.z**2)
            return dis1 < dis2
        elif type(pif) == int or type(pif) == float:
            dis3 = math.sqrt(self.x**2 + self.y**2 + self.z**2)
            return dis3 < pif
        else:
            raise TypeError('The given parameter should be a Point or an integer')
    def __getitem__(self, int_str):
        if int_str == 'x' or int_str == 0 and type(int_str) != float:
            return self.x
        elif int_str == 'y' or int_str == 1 and type(int_str) != float:
            return self.y
        elif int_str == 'z' or int_str == 2 and type(int_str) != float:
            return self.z
        else:
            raise IndexError('The given index should inside the Point')
    
    def __call__(self, x_new, y_new, z_new):
        self.x = x_new
        self.y = y_new
        self.z = z_new
        for item in x_new, y_new, z_new:
            assert type(item) is int, 'Point.__init__: x('+str(item)+') must be an int.'
        return None

if __name__ == '__main__':
    # Put in simple tests for Point before allowing driver to run
    
    print()
    import driver
    
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
