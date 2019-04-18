import prompt
from goody import irange
from random import shuffle
import predicate


# List Node class and helper functions (to set up problem)

class LN:
    def __init__(self,value,next=None):
        self.value = value
        self.next  = next

def list_to_ll(l):
    if l == []:
        return None
    front = rear = LN(l[0])
    for v in l[1:]:
        rear.next = LN(v)
        rear = rear.next
    return front

def str_ll(ll):
    answer = ''
    while ll != None:
        answer += str(ll.value)+'->'
        ll = ll.next
    return answer + 'None'

# Tree Node class and helper functions (to set up problem)

class TN:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left  = left
        self.right = right

def list_to_tree(alist):
    if alist == None:
        return None
    else:
        return TN(alist[0],list_to_tree(alist[1]),list_to_tree(alist[2])) 

def str_tree(atree,indent_char ='.',indent_delta=2):
    def str_tree_1(indent,atree):
        if atree == None:
            return ''
        else:
            answer = ''
            answer += str_tree_1(indent+indent_delta,atree.right)
            answer += indent*indent_char+str(atree.value)+'\n'
            answer += str_tree_1(indent+indent_delta,atree.left)
            return answer
    return str_tree_1(0,atree) 

# Define separate here ITERATIVELY

def separate(ll,p):
    ll_t = LN(None)
    ll_f = LN(None)
    while ll != None:
        if p(ll.value) == True:
            ll_t.next = LN(ll.value, ll_t.next)
        else:
            ll_f.next = LN(ll.value, ll_f.next)
        ll = ll.next
    return (ll_t.next, ll_f.next)
            
# Define is_min_heap here RECURSIVELY
def is_min_heap(t):
    if t == None:
        return False
    if t.value == None or (t.left == None and t.right == None):
        return True
    if t.left == None and t.right.value > t.value:
        return is_min_heap(t.right)
    elif t.right == None and t.left.value > t.value:
        return is_min_heap(t.left)
    elif t.left != None and t.right != None and t.left.value > t.value and t.right.value > t.value:
        return is_min_heap(t.left) and is_min_heap(t.right)
    else:
        return False

# Define the derived StingVar_WithHistory using the StringVar base class defined in tkinter

from tkinter import StringVar

class StringVar_WithHistory(StringVar):
    def __init__(self):
        self.history = []
        
    def set (self,value):
        if value not in self.history:
            StringVar.__init__(self, value = value)
            self.history.append(value) 

    def undo (self):
        if len(self.history) > 1: 
            self.history = self.history[:-1]
            StringVar.__init__(self, value = self.history[-1])
            
# OptionMenuUndo: acts much like an OptionMenu, but also allows undoing the most recently
#   selected option, all the way back to the title (whose selection cannot be undone).
# It overrides the __init__ method and defines the new methods get, undo, and 
#   simulate_selections.
# It will work correctly if StringVar_WithHistory is defined correctly
from tkinter import OptionMenu
class OptionMenuUndo(OptionMenu):
    def __init__(self,parent,title,*option_tuple,**configs):
        self.result = StringVar_WithHistory()
        self.result.set(title)
        OptionMenu.__init__(self,parent,self.result,*option_tuple,**configs)

    # Get the current option  
    def get(self):                
        return self.result.get() # Call get on the StringVar_WithHistory attribute

    # Undo the most recent option
    def undo(self):
        self.result.undo()       # Call undo on the StringVar_WithHistory attribute
      
    # Simulate selecting an option (mostly for test purposes)
    def simulate_selection(self,option):
        self.result.set(option)  # Call set on the StringVar_WithHistory attribute


# Testing Script
if __name__ == '__main__':
    
    print('Testing separate')
    ll = list_to_ll([i for i in range(20)])
    even,odd = separate(ll,lambda x : x%2 == 0) 
    print(str_ll(even)+' and '+str_ll(odd))
    
    prime,composite = separate(ll,predicate.is_prime) 
    print(str_ll(prime)+' and '+str_ll(composite))
    
    small,big = separate(ll,lambda x : x <= 10) 
    print(str_ll(small)+' and '+str_ll(big))
    

    print('\nTesting is_min_heap')
    t = None
    print('\nTree is\n',str_tree(t),end='')
    print('is_min_heap =',is_min_heap(t))  
          
    t = list_to_tree([1,[2,None,None],[3,None,None]]) 
    print('\nTree is\n',str_tree(t),end='')
    print('is_min_heap =',is_min_heap(t))  
    
    t = list_to_tree([2,[1,None,None],[3,None,None]]) 
    print('\nTree is\n',str_tree(t),end='')
    print('is_min_heap =',is_min_heap(t))  
          
    t = list_to_tree([3,[2,None,None],[1,None,None]]) 
    print('\nTree is\n',str_tree(t),end='')
    print('is_min_heap =',is_min_heap(t))  
    
    t = list_to_tree([1,None,[3,None,None]]) 
    print('\nTree is\n',str_tree(t),end='')
    print('is_min_heap =',is_min_heap(t))  
           
    t = list_to_tree([1,[2,None,None],None]) 
    print('\nTree is\n',str_tree(t),end='')
    print('is_min_heap =',is_min_heap(t))  
    
    t = list_to_tree([3,None,[1,None,None]]) 
    print('\nTree is\n',str_tree(t),end='')
    print('is_min_heap =',is_min_heap(t))  
           
    t = list_to_tree([2,[1,None,None],None]) 
    print('\nTree is\n',str_tree(t),end='')
    print('is_min_heap =',is_min_heap(t))  
    
    t = list_to_tree(
            [5,
              [8,
                [16,
                   [32,None,None],
                   [46,
                      [70,None,None],
                      [82,None,None]
                   ]
                ],
                None],
              [12,
                 [24,
                    None,
                    [30,
                       [40,None,None],
                       [70,None,None]
                    ]
                 ],
                 None
              ]
            ])
    print('\nTree is\n',str_tree(t),end='')
    print('is_min_heap =',is_min_heap(t))  
  
    t = list_to_tree(
            [5,
              [8,
                [16,
                   [32,None,None],
                   [32,
                      [70,None,None],
                      [82,None,None]
                   ]
                ],
                None],
              [12,
                 [30,
                    None,
                    [30,
                       [40,None,None],
                       [70,None,None]
                    ]
                 ],
                 None
              ]
            ])
    print('\nTree is\n',str_tree(t),end='')
    print('is_min_heap =',is_min_heap(t))  

    t = list_to_tree(
            [5,
              [8,
                [16,
                   [32,None,None],
                   [46,
                      [70,None,None],
                      [82,None,None]
                   ]
                ],
                None],
              [12,
                 [30,
                    None,
                    [30,
                       [40,None,None],
                       [70,None,None]
                    ]
                 ],
                 None
              ]
            ])
    print('\nTree is\n',str_tree(t),end='')
    print('is_min_heap =',is_min_heap(t))  
  

    print('\nTesting OptionMenuUndo')
    from tkinter import *
    print('Simulate using StringVar_WithHistory or build/test actual GUI')
    if prompt.for_bool('Simulate',default=True):
        # Needed for obscure reasons
        root = Tk()
        root.title('Widget Tester')
        main = Frame(root)
        
        # Construct an OptionMenuUndo object for simulation
        omu = OptionMenuUndo(main, 'Choose Option', 'option1','option2','option3')
        
        # Initially its value is 'Choose Option'
        print(omu.get(), '   should be Choose Option')
        
        # Select a new option
        omu.simulate_selection('option1')
        print(omu.get(), '         should be option1')
        
        # Select a new option
        omu.simulate_selection('option2')
        print(omu.get(), '         should be option2')
        
        # Select the same option (does nothing)
        omu.simulate_selection('option2')
        print(omu.get(), '         should still be option2')
        
        # Select a new option
        omu.simulate_selection('option3')
        print(omu.get(), '         should be option3')
         
        # Undo the last option: from 'option3' -> 'option2'
        omu.undo()
        print(omu.get(), '         should go back to option2')
         
        # Undo the last option: from 'option2' -> 'option1'
        omu.undo()
        print(omu.get(), '         should go back to option1')
         
        # Undo the last option: from 'option1' -> 'Choose Option'
        omu.undo()
        print(omu.get(), '   should go back to Choose Option')
         
        # Cannot undo the first option: does nothing
        omu.undo()
        print(omu.get(), '   should still be Choose Option')

         
        # Cannot undo the first option: does nothing
        omu.undo()
        print(omu.get(), '   should still be Choose Option')
        
    else: #Build/Test real widget

        # #OptionMenuToEntry: with title, linked_entry, and option_tuple
        # #get is an inherited pull function; put is a push function, pushing
        # #  the selected option into the linked_entry (replacing what is there)
        # 
        root = Tk()
        root.title('Widget Tester')
        main = Frame(root)
        main.pack(side=TOP,anchor=W)
         
        omu = OptionMenuUndo(main, 'Choose Option', 'option1','option2','option3')
        omu.grid(row=1,column=1)
        omu.config(width = 10)
         
        b = Button(main,text='Undo Option',command=omu.undo)
        b.grid(row=1,column=2)
         
        root.mainloop()    
