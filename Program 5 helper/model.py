import controller
import model       #strange, but need to pass this module to update; ignore error

from ball import Ball
import math,random


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
balls       = set()


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

def random_speed():
    # Magnitude is 5-10
    return random.randint(5,10)


def random_angle():
    # between 0 and 2pi
    return random.random()*math.pi*2


def random_color():
    # hex(52) -> "0x34", so [2:] is the two hex digits, without the 0x prefix
    return "#"+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]


def reset ():
    global running,cycle_count,balls
    running     = False
    cycle_count = 0
    balls       = set()


def mouse_click(x,y):
    balls.add( Ball(x,y,random_speed(),random_angle(),random_color()))

  
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for b in balls:
            b.update(model)

    
def display_all():
    # Easier to delete all and display all; could use move with more thought
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")

  
def start():
    global running
    running = True

  
def stop():
    global running
    running = False 
  
  
def reverse():
    for b in balls:
        b.reverse() 

  
