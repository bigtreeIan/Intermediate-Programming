# primes is used to test code you write below
from predicate import is_prime

def primes(max=None):
    p = 2
    while max == None or p <= max:
        if is_prime(p):
            yield p
        p += 1 

# Generators must be able to iterate through any iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on any parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v
        
def peaks(iterable):
    iterable = iter(iterable)
    peak_list = []
    num1 = next(iterable)
    num2 = next(iterable)
    try:
        num3 = next(iterable)
        while True:
            if num2 > num1:
                if num2 > num3:
                    peak_list.append(num2)
            num1 = num2
            num2 = num3
            num3  = next(iterable)
    except StopIteration:
        return peak_list
            
def compress(vit,bit):
    vit = iter(vit)
    bit = iter(bit)
    try:
        while True:
            bool = next(bit)
            if bool == False:
                y = next(vit)
            elif bool == True:
                yield next(vit)
    except StopIteration:
        pass
                 
def stop_when(iterable,p):
    iterable = iter(iterable)
    try:
        while True:
            check = next(iterable)
            if p(check) == False:
                yield check
            else:
                break
    except StopIteration:
        pass
            
def start_when(iterable,p):
    iterable = iter(iterable)
    try:
        while True:
            check = next(iterable)
            if p(check) == True:
                yield check
            else:
                continue
    except StopIteration:
        pass
             
def alternate(*args):
    alter_list = [hide(arg) for arg in args]
    try:
        for i in range(len(alter_list)):
            while True:
                for item in alter_list:
                    item = iter(item)                   
                    result = next(item)
                    yield result
                break
    except StopIteration:
        pass

class Ordered:
    def __init__(self,aset):
        self.aset = aset

    def __iter__(self):
        if self.aset != set(): 
            initial_mini = min(self.aset)
            yield initial_mini
            while True:
                check_list = []
                for i in self.aset:
                    if i > initial_mini:
                        check_list.append(i)
                if check_list != []:
                    initial_mini = min(check_list)
                    yield initial_mini               
                else:
                    raise StopIteration
        else:
            raise StopIteration
                    
if __name__ == '__main__':
    from goody import irange
    # Test peaks; add your own test cases
    print('Testing peaks')
    print(peaks([0,1,-1,3,8,4,3,5,4,3,8]))
    print(peaks([5,2,4,9,6,1,3,8,0,7]))
    print(peaks([1,2,3,4,5]))
    print(peaks([0,1]))
    
    
    #prints a 1 for every prime preceded/followed by a non prime
    #below 5, 7, 11, 13, 17, 19 have that property the result should be a list of 6 1s
    #[1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]
    #[0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
    print(list(int(is_prime(p)) for p in irange(1,20)))
    print(peaks(int(is_prime(p)) for p in irange(1,20)))
    
    
    # Test compress; add your own test cases
    print('\nTesting compress')
    for i in compress('abcdefghijklmnopqrstuvwxyz',
                      [is_prime(i) for i in irange(1,26)]):
        print(i,end='')
    print()

    for i in compress('abcdefghijklmnopqrstuvwxyz',
                      (is_prime(i) for i in irange(1,26))):
        print(i,end='')
    print('\n')
    
    
    # Test stop_when; add your own test cases
    print('\nTesting stop_when')
    for c in stop_when('abcdefghijk', lambda x : x >='d'):
        print(c,end='')
    print()

    for c in stop_when(hide('abcdefghijk'), lambda x : x >='d'):
        print(c,end='')
    print('\n')

   
    # Test start_when; add your own test cases
    print('\nTesting start_when')
    for c in start_when(hide('abcdefghijk'), lambda x : x >='d'):
        print(c,end='')
    print()

    for c in start_when(hide('abcdefghijk'), lambda x : x >='d'):
        print(c,end='')
    print('\n')

              
    # Test alternate; add your own test cases
    print('\nTesting alternate')
    for i in alternate('abcde','fg','hijk'):
        print(i,end='')
    print()
       
    for i in alternate(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print()
       
    for i in alternate(primes(20), hide('fghi'),hide('jk')):
        print(i,end='')
    print('\n')
       
    
    # Test Ordered; add your own test cases
    print('\nTesting Ordered')
    s = {1, 2, 4, 8, 16}
    i = iter(Ordered(s))
    print(next(i))
    print(next(i))
    s.remove(8)
    print(next(i))
    print(next(i))
    s.add(32)
    print(next(i))
    print()
   
    s = {1, 2, 4, 8, 16}
    i = iter(Ordered(s))
    print([next(i), next(i), s.remove(8), next(i), next(i), s.add(32), next(i)])
    
    s = {1, 2, 4, 8}
    for v in Ordered(s):
        s.discard(8)
        s.add(10)
        print(v) 
    print('\n')
         
    import driver
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
