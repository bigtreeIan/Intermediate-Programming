import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special 

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=


running_option = False
num_cycle = 0
simulton_module = set()
object_kind = ''
#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running_option, num_cycle, simulton_module
    running_option = False
    num_cycle = 0
    simulton_module = set()

#start running the simulation
def start ():
    global running_option
    running_option = True

#stop running the simulation (freezing it)
def stop ():
    global running_option
    running_option = False

#tep just one update in the simulation
def step ():
    global running_option, num_cycle
    start()
    update_all()    
    stop()
    
#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global object_kind
    object_kind = kind

#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate

def mouse_click(x,y):
    created_object = (x, y)
    try:
        if object_kind == 'Remove':
            find_set = find(lambda p: p.contains(created_object))
            for i in find_set:           
                remove(i)
        elif object_kind != '':
            eval('simulton_module.add({a}({b}, {c}))'.format(a = object_kind, b = x, c = y))
    except:
        pass
        
#add simulton s to the simulation
def add(s):
    global created_object
    simulton_module.add(s)
# remove simulton s from the simulation    
def remove(s):
    global simulton_module
    simulton_module.remove(s)

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    simu_set = set()
    for simu in simulton_module:
        if p(simu) == True:
            simu_set.add(simu)
    return simu_set

#call update for every simulton in the simulation
def update_all():
    global num_cycle
    if running_option == True:
        num_cycle += 1
        try:
            for simu in simulton_module:
                simu.update(model)
        except:
            pass

#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    try:
        for o in controller.the_canvas.find_all():
            controller.the_canvas.delete(o)
        for b in simulton_module:
            b.display(controller.the_canvas)
        controller.the_progress.config(text=str(num_cycle)+" cycles/"+str(len(simulton_module))+" simultons")
    except AttributeError:
        pass
