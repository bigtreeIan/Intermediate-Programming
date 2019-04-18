import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
simu       = set()
command     = ''

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,simu
    running     = False;
    cycle_count = 0;
    simu       = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop():
    global running
    running = False 


#step just one update in the simulation
def step ():
    global cycle_count,running
    if running:
        cycle_count += 1
        try:
            for b in simu:
                b.update(model)
        except RuntimeError:
            pass
        running=False
    else:
        cycle_count += 1
        try:
            for b in simu:
                b.update(model)
        except RuntimeError:
            pass
#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global command
    command = kind

#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    obj=(x,y)  
    if command == 'Remove':
        try:
            for i in simu:
                if obj[0]>(i.get_location()[0]-i.get_dimension()[0]) and\
                 obj[1]>(i.get_location()[1]-i.get_dimension()[1]) and\
                  obj[0]<(i.get_location()[0]+i.get_dimension()[0]) and\
                   obj[1]<(i.get_location()[1]+i.get_dimension()[1]):
                    remove(i)
        except RuntimeError:pass
    else:
        add(obj)    

#add simultion s to the simulation
def add(s):
    global command
    if command!='':
        eval('simu.add({}({},{}))'.format(command,s[0],s[1]))

# remove simulton s from the simulation    
def remove(s):
    global simu
    simu.remove(s)
   
#find/return a set of simultons that each satisfy predicate p    
def find(p):
    result=set()
    for i in simu:
        if p(i):
            result.add(i)
    return result

#call update for every simulton in the simulation
def update_all():
    global cycle_count,simu
    if running:
        cycle_count += 1
        try:
            for b in simu:
                b.update(model)
        except RuntimeError:
            pass

#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    try:
        for o in controller.the_canvas.find_all():
            controller.the_canvas.delete(o)
        
        for b in simu:
            b.display(controller.the_canvas)
         
        controller.the_progress.config(text=str(cycle_count)+" cycles/"+str(len(simu))+" simultons")
    except AttributeError:
        pass
