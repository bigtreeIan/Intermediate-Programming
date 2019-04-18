from tkinter import Tk,Frame,TOP,LEFT,BOTTOM,RAISED,BOTH

# import controller to call/create widgets and position them in the view
import controller


# Construct a simple root window
root = Tk()
root.title("Bouncing Balls")
root.protocol("WM_DELETE_WINDOW",quit)

frame = Frame(root)

# Place buttons simply at the top
frame.pack(side=TOP)
controller.reset_button  (frame,text="Reset")  .pack(side=LEFT)
controller.start_button  (frame,text="Start")  .pack(side=LEFT)
controller.reverse_button(frame,text="Reverse").pack(side=LEFT)
controller.stop_button   (frame,text="Stop")   .pack(side=LEFT)
controller.progress      (frame,text="0 balls/0 cycles",width=25,relief=RAISED).pack(side=LEFT)
 
# Place canvas in the space below
controller.simulation_canvas(root,width=300,height=300,bg="white").pack(side=BOTTOM,expand=True,fill=BOTH)