# Submitter: yihanx2(Xu, Yihan)
# Partner  : zihaog(Gao, Zihao)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable=False):
    def show_listing(s):
        for i, l in enumerate(s.split('\n'),1):
            print('{num: >3} {txt}'.format(num = i, txt = l.rstrip()))
    if type(type_name) != str:
        raise SyntaxError
    legal_bool1 = re.match('^[(a-z)(A-Z)]([\w\d(_\w)]+)?$', type_name)
    if legal_bool1 == None:
        raise SyntaxError
    elif legal_bool1 != None:
        if type_name in keyword.kwlist:
            raise SyntaxError
    
    if type(field_names) == list:
        for names in field_names:
            legal_bool2 = re.match('^[(a-z)(A-Z)]([\w\d(_\w)]+)?$', names)
            if legal_bool2 == None:
                raise SyntaxError
            elif legal_bool2 != None:
                if names in keyword.kwlist:
                    raise SyntaxError
    
    elif type(field_names) == str:
        if ',' in field_names:
            field_names = field_names.replace(' ', '')
            field_names = field_names.split(',')
            for names in field_names:
                legal_bool3 = re.match('^[(a-z)(A-Z)]([\w\d(_\w)]+)?$', names)
                if legal_bool3 == None:
                    raise SyntaxError
                elif legal_bool3 != None:
                    if names in keyword.kwlist:
                        raise SyntaxError 
        else:
            field_names = field_names.split(' ')
            for i in field_names:
                if i == ' ':
                    field_names.remove(i)
            for names in field_names:
                legal_bool3 = re.match('^[(a-z)(A-Z)]([\w\d(_\w)]+)?$', names)
                if legal_bool3 == None:
                    raise SyntaxError
                elif legal_bool3 != None:
                    if names in keyword.kwlist:
                        raise SyntaxError
    else:
        raise SyntaxError 
    l1 = []
    for names in field_names:
        if names not in l1:
            l1.append(names)
    field_names = l1
        
    class_name_template = '''\
class {type_name}:\n'''
    
    def gen_init(field_names):
        init_template = '''\
    def __init__(self'''
        for i in field_names:
            init_template += ',' + str(i)
        init_template += '):\n'
        for i in field_names:
            init_template += '        self.' + str(i) + '=' + str(i) + '\n'
        init_template += '        self._fields = '+ str(field_names)+ '\n'
        init_template += '        self._mutable = '+ str(mutable)+ '\n'
        return init_template
        
    def gen_repr(type_name, field_names):
        repr_template = '''\
    def __repr__(self):\n'''
        repr_template += '        return ' + "'"+type_name + "('"
        for i in field_names:
            repr_template +=  '+str(' +"'"+ i +"'"+ ')+"="+str('+'self.' + str(i)+ ')+","'
        repr_template = repr_template[:-4] + "+')'" + '\n'
        return repr_template
    
    def gen_get(field_names):
        get_template = ''
        for i in field_names:
            get_template += '    def get_' + str(i) + '(self): \n        return self.' + str(i)+'\n'
        return get_template
    
    def gen_getitem(type_name, field_names):
        getitem_template = '    def __getitem__(self, int_str):\n'
        for i in field_names:
            getitem_template += '        if int_str ==' +"'" + str(i) + "'" +':\n' 
            getitem_template += '            return ' + type_name + '.get_' + str(i) +'(self)' +'\n'
            getitem_template += '        if int_str ==' + str(field_names.index(i)) + ':\n'
            getitem_template += '            return ' + 'self.' + str(i) + '\n'
        getitem_template += '        else:\n'    
        getitem_template += '            raise IndexError\n'
        return getitem_template   
    
    def gen_eq(type_name, field_names):
        eq_template = '    def __eq__(self, target):\n'
        eq_template += '        if type(target) is ' + type_name + ' and ' + 'len(target._fields) == len(self._fields): \n'        
        for i in range(len(field_names)):
            eq_template += '            if self[' + str(i) + ']' + '!= target[' + str(i) + ']:\n'
            eq_template += '                return False\n'
        eq_template += '            return True\n'
        eq_template += '        return False\n'
        return eq_template
    
    def gen_replace(type_name, field_names):
        replace_template = '    def _replace(self, **kargs):\n'
        replace_template += '        for keys, values in kargs.items():\n'
        replace_template += '            if keys not in self._fields:\n'
        replace_template += '                raise TypeError\n'
        replace_template += '        if self._mutable == True:\n'
        replace_template += '            for keys, values in kargs.items():\n'
        replace_template += '                self.__dict__[keys] = values\n'
        replace_template += '        if self._mutable == False:\n'
        replace_template += '            new_class = '+ type_name + '(' 
        for i in field_names:
            replace_template += 'self[' + "'" + str(i)+ "'" +'],' 
        replace_template = replace_template[:-1] + ')\n'
        replace_template += '            for keys, values in kargs.items():\n'
        replace_template += '                new_class.__dict__[keys] = values\n'
        replace_template += '            return new_class\n'
        return replace_template
    
    def gen_setatt(field_names):
        setatt_template = '    def __setattr__(self,name,value):\n'
        setatt_template += '        if "_mutable" in self.__dict__:\n'
        setatt_template += '            if self._mutable == False:\n '
        setatt_template += '                if "_mutable" not in self.__dict__ or "_fields" not in self.__dict__ or'
        for i in field_names:
            setatt_template += "'"+str(i)+"'"+ ' not in self.__dict__ or '
        setatt_template = setatt_template[:-4] + ':\n'
        setatt_template += '                     self.__dict__[name] = value\n'
        setatt_template += '                 else:\n'
        setatt_template += '                     raise AttributeError\n'
        setatt_template += '            else:\n'
        setatt_template += '                self.__dict__[name] = value\n'
        setatt_template += '        else:\n'
        setatt_template += '            self.__dict__[name] = value'
        return setatt_template
    
    class_definition = \
      class_name_template.format(type_name = type_name) + gen_init(field_names) + gen_repr(type_name, field_names) + gen_get(field_names) + gen_getitem(type_name, field_names) + gen_eq(type_name, field_names) + gen_replace(type_name,field_names) + gen_setatt(field_names)
    

    
             
        
        
        
        

    # put your code here
    # bind class_definition (used below) to the string constructed for the class



    # For initial debugging, always show the source code of the class
    #show_listing(class_definition)
    
    # Execute the class_definition string in a local namespace and bind the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   show the error
    name_space = dict(__name__='pnamedtuple_{type_name}'.format(type_name=type_name))
    try:
        exec(class_definition, name_space)
        name_space[type_name].source_code = class_definition
    except(SyntaxError, TypeError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]
    
if __name__ == '__main__':
    import driver
    driver.driver()
    x = pnamedtuple('Point', 'x y', mutable=False)
    print(x)
