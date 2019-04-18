from collections import defaultdict
from math import atan2, sqrt
from _ast import Num


def  compose(f : callable, g : callable):
    return lambda x: f(g(x)) 
        
def self_compose(f : callable, n : int) -> callable:   
    if n < 0:
        raise AssertionError
    elif n == 0:
        return lambda x: x
    elif n > 0:
        def final_result(x):
            mark = x
            for i in range(n):
                mark = f(mark) 
            return mark    
        return final_result
    
def sorted1 (ps : {int:(int,int)}) -> [(int,(int,int))]:
    return sorted(ps.items(), key = (lambda item1: item1[1][0]))

def sorted2 (ps : {int:(int,int)}) -> [(int,int)]:
    return sorted(ps.values(), key = (lambda item2: atan2(item2[1], item2[0]))) 

def sorted3 (ps : {int:(int,int)}) -> [int]:
    return sorted(ps.keys(), key = (lambda item3: atan2(ps[item3][1], ps[item3][0])))

def points (ps : {int:(int,int)}) -> [(int,int)]:
    return sorted(ps.values(), key = (lambda item4: ps.keys()))

def first_quad (ps : {int:(int,int)}) -> {(int,int):float}:
    return {value: sqrt(value[0]**2 + value[1]**2) for value in ps.values() if value[0] >= 0 and value[1] >= 0}
    
def called(db : {str:{str:int}}) -> {str:int}:
    return {keys: sum(sorted(db[keys].values())) for keys in db}

def got_called(db : {str:{str:int}}) -> {str:int}:
    d1 = defaultdict(int)
    for callers, sub_dic in sorted(db.items()):
        for callees, num in sorted(sub_dic.items()):
            d1[callees] += num
    return dict(d1)
            
def invert(db : {str:{str:int}}) -> {str:{str:int}}:
    d2 = defaultdict(dict)
    for callers, sub_dic in sorted(db.items()):
        for callees, num in sorted(sub_dic.items()):
            d2[callees][callers] = num
    return dict(d2)
            
if __name__ == '__main__':
    from goody import irange
   
    # Feel free to test other cases as well
    
    print('Testing compose')
    f = compose(lambda x : 2*x, lambda x : x+1)
    print( [(a,f(a)) for a in irange(0,10)] )
    g = compose(lambda x : x+1, lambda x : 2*x)
    print( [(a,g(a)) for a in irange(0,10)] )
     
    print('\nTesting self_compose')
    scl = [self_compose(lambda x : 2*x,i) for i in irange(0,6)]
    print([(1,f(1)) for f in scl])
         
    print('\nTesting sorted1')
    ps = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    print(sorted1(ps))
 
    print('\nTesting sorted2')
    ps = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    print(sorted2(ps))
 
    print('\nTesting sorted3')
    ps = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    print(sorted3(ps))
    
    print('\nTesting points')
    ps = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    print(points(ps))
 
    print('\nTesting first_quad')
    ps = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    print(first_quad(ps))
 
    print('\nTesting called')
    db = {'a':{'b':2,'c':1},'b':{'a':3,'c':1},'c':{'a':1,'d':2}}
    print(called(db))
     
    print('\nTesting got_called')
    db = {'a':{'b':2,'c':1},'b':{'a':3,'c':1},'c':{'a':1,'d':2}}
    print(got_called(db))
     

    print('\nTesting invert')
    db = {'a':{'b':2,'c':1},'b':{'a':3,'c':1},'c':{'a':1,'d':2}}
    print(invert(db))
     
    
    print('\ndriver testing with batch_self_check:')
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()           





























