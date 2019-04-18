# Submitter: yihanx2(Xu, Yihan)
# Partner  : zihaog(Gao, Zihao)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation():
    # set name to True for checking to occur
    checking_on  = True
  
    # self._checking_on must also be true for checking to occur
    def __init__(self,f):
        self._f = f
        self.checking_on = True
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):      
        def check_list():
            
            if type(annot) is list and isinstance(value, list) == False:
                raise AssertionError("'{a}' failed annotation check(wrong type): value = {v} was type {w} ...should be type list".format(a = str(param), v = str(value), w = type_as_str(value)))
            if len(annot) > 1:
                if len(value) != len(annot):
                    raise AssertionError("'{a}' failed annotation check(wrong number of elements): value = {v} annotation had {l} elements {e}".format(a = str(param), v = str(value), l = str(len(annot)), e = str(annot)))
            
            counter = 0
            if len(annot) == 1:
                for i in value:
                    check_history = "list[{a}] check: {b}".format(a = counter, b = annot)
                    self.check(param,annot[0],i,check_history)    
            
            counter = 0
            if len(annot) > 1:
                for i in value:
                    check_history = "list[{a}] check: {b}".format(a = counter, b = annot[counter])
                    self.check(param,annot[counter],i,check_history)
                    counter += 1
                
        def check_tuple():
            
            if type(annot) is tuple and isinstance(value, tuple) == False:
                raise AssertionError("'{a}' failed annotation check(wrong type): value = {v} was type {w} ...should be type tuple".format(a = str(param), v = str(value), w = type_as_str(value)))
            
            if len(annot) > 1:
                if len(value) != len(annot):
                    raise AssertionError("'{a}' failed annotation check(wrong number of elements): value = {v} annotation had {l}elements {e}".format(a = str(param), v = str(value), l = str(len(annot)), e = str(annot)))
            
            counter = 0
            if len(annot) == 1:
                for i in value:
                    check_history = "list[{a}] check: {b}".format(a = counter, b = annot)
                    self.check(param,annot[0],i,check_history)    
            
            counter = 0
            if len(annot) > 1:
                for i in value:
                    check_history = "list[{a}] check: {b}".format(a = counter, b = annot[counter])
                    self.check(param,annot[counter],i,check_history)
                    counter += 1
        
        def check_dict():
            if type(annot) is dict and isinstance(value, dict) == False:
                raise AssertionError("'{a}' failed annotation check(wrong type): value = {v} was type {w} ...should be type dict".format(a = str(param), v = str(value), w = type_as_str(value)))
            
            if len(annot.keys()) > 1:
                if len(value.keys()) != len(annot.keys()):
                    raise AssertionError("'{a}' annotation inconsistency: dict should have {l} item but had {e}annotation = {t}".format(a = str(param), l = str(len(annot.keys())), e = str(len(value.keys())), t = str(annot)))
            
            for i,j in value.items():
                for key,val in annot.items():              
                    self.check(param,key,i,"dict key check: {a}".format(a = key))
                    self.check(param,val,j,"dict value check: {a}".format(a = val))
            
        def check_set():
            if type(annot) is set and isinstance(value, set) == False:
                raise AssertionError("'{a}' failed annotation check(wrong type): value = {v} was type {w} ...should be type set".format(a = str(param), v = str(value), w = type_as_str(value)))
            if len(annot) != 1:
                raise AssertionError("'{p}' annotation inconsistency: set should have 1 value but had {e}annotation = {a}".format(p = str(param), e = str(len(annot)), a = str(annot)))
            for i in value:
                for j in annot:
                    check_history = "set value check:{a}".format(a = j)
                    self.check(param,j,i,check_history)
        
        def check_frozen():
            if type(annot) is frozenset and isinstance(value, frozenset) == False:
                raise AssertionError("'{p}' failed annotation check(wrong type): value = {v}was type {t} ...should be type frozenset".format(p = param, v = value, t = type(value)))
            self.check(param,set(annot),set(value))
        
        def check_function():
            if annot.__code__.co_argcount != len(param):
                raise AssertionError("'{p}' annotation inconsistency: predicate should have {l} parameter but had {e}predicate = {a}".format(p = str(param), l = str(len(param)), e = str(annot.__code__.co_argcount), a = str(annot)))
            if type(value) in [int,str]:
                try:
                    if annot(value) == False:
                        raise AssertionError("'{p}' failed annotation check: value = {v} predicate = {a}".format(p = str(param), v = str(value), a = str(annot)))
                except Exception as ex1:
                    raise AssertionError("AssertionError: '{p}' annotation predicate({a}) raised exception exception = {e} ".format(p = param, a = annot, e = ex1))
            if type(value) != int:
                counter = 0
                for i in value:
                    try:
                        if annot(i) == False:
                            check_history = "list[{index}] check: {a}".format(index = str(counter), a = str(annot))
                            result = "'{p}' failed annotation check: value = {v} predicate = {a}".format(p = str(param), v = str(value), a = str(annot)) + '\n' + check_history
                            raise AssertionError(result)
                        else:counter += 1
                    except Exception as ex:
                        raise AssertionError("AssertionError: '{p}' annotation predicate({a}) raised exception exception = {e} list[{index}] check: {a}".format(p = param, a = annot, e = ex, index = counter))
        def check_other_1():
            try:
                self.__check_annotation__(annot, self.check, param,value, check_history)
            except AttributeError as ex1:
                raise AssertionError("AssertionError: 'x' annotation undecipherable: Bag(<class 'str'>[1])")
            except AssertionError:
                raise AssertionError("AssertionError: 'x' failed annotation check(wrong type): value = 1...should be type str\nBag value check: <class 'str'>")
            except Exception as ex:
                raise AssertionError("AssertionError: 'x' annotation predicate(<function <lambda&rt; at 0x02C5C390>) raised exceptiexception = TypeError: unorderable types: str() > int()\nBag value check: <function <lambda> at 0x02C5C390>")
       
        def check_other_2():
            try:
                annot.__check_annotation__(self.check,param,value,check_history)
            except AttributeError as ex1:
                raise AssertionError("AssertionError: 'x' annotation undecipherable: Bag(<class 'str'>[1])")
            except AssertionError:
                raise AssertionError("AssertionError: 'x' failed annotation check(wrong type): value = 1...should be type str\nBag value check: <class 'str'>")
            except Exception as ex:
                raise AssertionError("AssertionError: 'x' annotation predicate(<function <lambda&rt; at 0x02C5C390>) raised exceptiexception = TypeError: unorderable types: str() > int()\nBag value check: <function <lambda> at 0x02C5C390>")
        
        def check_str():
            try:
                if eval(annot, self.param_arg) == False:
                    raise AssertionError("'{a}' failed annotation check(str predicate: {b})args for evaluation: {c}".format(a = str(param), b=str(type(annot)),c = str('x')))
            except Exception as ex:
                raise AssertionError("'{a}' annotation check(str predicate: {b}) raised exception\n".format(a = param, b = str(type(annot)) ),ex)
                
        if type(annot) == list:
            check_list()
        elif isinstance(annot, frozenset):
            check_frozen()
        elif type(annot) == tuple:
            check_tuple()
        elif inspect.isfunction(annot):
            check_function()
        elif type(annot) == dict:
            check_dict()
        elif type(annot) == set:
            check_set()
        elif type(annot) == str:
            check_str()
        elif str(annot.__class__.__name__) not in ['type','list','str','tuple','set','function','NoneType',"Check_All_OK","Check_Any_OK"]:
            check_other_1()
        elif 'Check' in str(annot.__class__.__name__):
            check_other_2()
        elif annot != None and isinstance(value, annot) == False:
            error_str = "'{a}' failed annotation check(wrong type): value = {v} was type {w} ...should be type {t}".format(a = str(param), v = str(value), w = type_as_str(value), t = annot)
            error_str += '\n' + check_history
            raise AssertionError(error_str)
             



        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # Decode the annotation and check it  
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict, in the order parameters occur in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name not in bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments
        
        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        
        try:
            self.param_arg = param_arg_bindings()
            annotation = self._f.__annotations__
            for i in self.param_arg.keys():
                if i in annotation:
                    self.check(i, annotation[i], self.param_arg[i])
            result_decorated = self._f(*args, **kargs)
            if 'return' in annotation:
                self.param_arg['_return'] = result_decorated
                self.check('return', annotation['return'], result_decorated)
                return result_decorated
            # Check the annotation for every parameter (if there is one)
              
            # Compute/remember the value of the decorated function
            
            # If 'return' is in the annotation, check it
            
            # Return the decorated answer
            
            #remove after adding real code in try/except
            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
#             print(80*'-')
#             for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
#                 print(l.rstrip())
#             print(80*'-')
            raise
        
if __name__ == '__main__':     
    # an example of testing a simple annotation  
#     def f(x:int):pass
#     f = Check_Annotation(f)
#     f(3)
#     f('a')
    import driver
    driver.driver()
