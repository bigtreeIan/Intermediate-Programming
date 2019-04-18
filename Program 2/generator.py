# Submitter: yihanx2(Xu, Yihan)
# Partner  : zihaog(Gao, Zihao)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming


def hide(iterable):
    for v in iterable:
        yield v


def running_count(iterable,p):
    i = 0
    for j in iterable:
        if p(j) == True:
            i += 1
            yield i
        else:
            yield i

def n_with_pad(iterable,n,pad=None):
    i = 0
    for j in iterable:
        if i < n:
            yield j
            i += 1
    while i < n:
        yield pad
        i+=1

def overlap(iterable,n,m=1):
    iterable = iter(iterable)
    result = [next(iterable) for i in range(n)]
    try:
        while True:
            yield result
            add = [next(iterable) for i in range(m)]
            result = result[m:] + add 
    except StopIteration:
        pass
       
def yield_and_skip(iterable):
    iterable = iter(iterable)
    try:
        while True:
            x = next(iterable)
            yield x
            if type(x) == int:
                for i in range(x):
                    y = next(iterable)      
            elif type(x) ==  str:
                pass
    except StopIteration:
        pass

        
def skip_bad_and_next(iterable,p): # predicate p(n) true if n is good
    iterable = iter(iterable)
    counter = 0
    try:
        while True:
            x = next(iterable)
            if p(x) == True:
                if counter >= 1:
                    counter =0
                else:
                    yield x
            else:
                counter +=1
                
    except StopIteration:
        pass
                
def alternate(*args):

    store_list = []
    for i in args:
        if type(i) == str:
            store_list.append(i)
        else:
             store_list.append(''.join(i))
    while True:
        item = store_list.pop(0)
        if len(item) >= 1:
            yield item[0]
            store_list.append(item[1:])
        elif len(item) == 1:
            yield item
        if store_list == []:
            break
        
            
                
            
    
    
    
    
    
    
    
    
    
#    ar_list = list(args)
#     for i in ar_list:
#         print(i)
#     counter = 0
#     try:
#         while True:
#             for i in ar_list:
#                 try:  
#                     i = iter(i)
#                     yield next(i)
#                     counter += 1
#                 except StopIteration:
#                     pass
#             if counter >= 11 or counter >=13:
#                 break
#     except:
#         pass
    





if __name__ == '__main__':
    print('\nTesting running_count')
    for i in running_count('bananastand',lambda x : x in 'aeiou'): # is vowel
        print(i,end=' ')
    print()
    for i in running_count(hide('bananastand'),lambda x : x in 'aeiou'): # is vowel
        print(i,end=' ')
    print()
    

    print('\nTesting n_with_pad')
    for i in n_with_pad('abcdefg',3,None):
        print(i,end=' ')
    print()
    for i in n_with_pad(hide('abcdefg'),3,None):
        print(i,end=' ')
    print()
    for i in n_with_pad(hide('abcdefg'),10):
        print(i,end=' ')
    print()
    for i in n_with_pad(hide('abcdefg'),10,'?'):
        print(i,end=' ')
    print()
    for i in n_with_pad(hide('abcdefg'),10):
        print(i,end=' ')
    print()
    
     
    print('\nTesting overlap')
    for i in overlap('abcdefghijk',3,2):
        print(i,end=' ')
    print()
    for i in overlap(hide('abcdefghijk'),3,2):
        print(i,end=' ')
    print()
     
     
    print('\nTesting yield_and_skip')
    for i in yield_and_skip([1, 2, 1, 3, 'a', 'b', 2, 5, 'c', 1, 2, 3, 8, 'x', 'y', 'z', 2]):
        print(i,end=' ')
    print()
    for i in yield_and_skip(hide([1, 2, 1, 3, 'a', 'b', 2, 5, 'c', 1, 2, 3, 8, 'x', 'y', 'z', 2])):
        print(i,end=' ')
    print()
       
       
    print('\nTesting skip_bad_and_next')
    for i in skip_bad_and_next('abxcdxxefxgxxxxxxxabc',lambda x: x != 'x'):
        print(i,end=' ')
    print()
    for i in skip_bad_and_next(hide('abxcdxxefxgxxxxxxxabc'),lambda x: x != 'x'):
        print(i,end=' ')
    print()
       
       
#     print('\nTesting alternate')
#     for i in alternate('abcde','fg','hijk'):
#         print(i,end=' ')
#     print()
#     for i in alternate(hide('abcde'),hide('fg'),hide('hijk')):
#         print(i,end=' ')
#     print()
    
    
    print()
    #driver tests
    import driver
    driver.default_file_name = 'bsc3.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
