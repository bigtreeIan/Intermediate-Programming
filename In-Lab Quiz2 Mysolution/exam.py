class Table:
    def __init__(self,name,fields,checks):
        if type(name) != str:
            raise AssertionError('The name should be a string')
        if type(fields) != list or len(fields) == 0:
            raise AssertionError('The fields should be a list')
        else:
            check_set = set()
            for i in fields:
                check_set.add(i)
            if len(check_set) != len(fields):
                raise AssertionError('String in fields must unique')
        if type(checks) != list or len(checks) == 0:
            raise AssertionError('check must be a list')
        else:
            if len(checks) != len(fields):
                raise AssertionError('check and fields should have same length')
            for i in checks:
                if callable(i) == False:
                    raise AssertionError('element in checks must be callable')    
        self.name = name
        self.fields = fields
        self.checks = checks
        self.records = []
    # If the attributes name, fields, and records are set correctly, __str__ returns
    #   a string that will print nicely (see the specificaitons).
    def __str__(self):
        def just(v,l):
            return (str(v).rjust(l) if type(v) is int else str(v).ljust(l))
        
        lengths = [len(field) for field in self.fields]
        for i in range(len(lengths)):
            lengths[i] = max([lengths[i]]+[len(str(r[i])) for r in self.records])
    
        return 'Table: ' + self.name + ' (with '+str(len(self.checks))+' checks)\n'+\
               ' | '.join([str(self.fields[i]).ljust(lengths[i]) for i in range(len(self.fields))])+'\n'+\
               '-+-'.join([lengths[i]*'-' for i in range(len(lengths))]) + '\n' +\
               '\n'.join([' | '.join([just(r[i],lengths[i]) for i in range(len(self.fields))]) for r in self.records])


    def raw(self):
        return\
             'self.name    = '+str(self.name)+'\n'+\
             'self.fields  = '+str(self.fields)+'\n'+\
             'self.checks  = '+str(self.checks)+'\n'+\
             'self.records = '+str(self.records)

    def add_record(self,*record):
        current_list1 = []
        if len(record) != len(self.fields):
            raise AssertionError('record and fields should have same length')
        for i in record:
            index1 = record.index(i)
            if self.checks[index1](i) != True:
                raise AssertionError('This do not pass check')
            else:
                current_list1.append(i)
        self.records.append(current_list1)
        return self.records
    
                
    def __call__(self,field):
        if type(field) != str or (field not in self.fields):
            raise AssertionError('field not in fields')
        index2 = self.fields.index(field)
        return index2
                                    
        
            

    def __getitem__(self,i):
        if type(i) != int and type(i) != tuple:
            raise IndexError('Input is not int or 2-tuple')
        if type(i) == tuple:
            if len(i) != 2:
                raise IndexError('Input is not int or 2-tuple')
            if type(i[0]) != int or type(i[1]) != str:
                raise AssertionError('not legal tuple')
            else:
                if i[0] < 0 or i[0] >= len(self.records) or i[1] not in self.fields:
                    raise AssertionError('i is not a legal record')
                else:
                    index3 = self.fields.index(i[1])
                    result = self.records[i[0]][index3]
                    return result
                          
        if type(i) == int:
            if i < 0 or i >= len(self.records):
                raise AssertionError('i is not a legal record')
            else:
                return self.records[i]
            
    def select_records(self,name,predicate):
        if type(name) != str or callable(predicate) != True:
            raise AssertionError('Input is not legal')
        else:
            g = Table(name, self.fields, self.checks)
            for i in g.records:
                if predicate(i) == False:
                    g.records.remove(i)
        return g
            
    
    
    def project(self,*fields):
        for i in fields:
            if type(i) != str:
                raise AssertionError('input should be all str')
            elif i not in self.fields:
                raise AssertionError('input not in fields')
            else:
                self.fields.remove(i)
                
        
    def __iter__(self):
        pass # will raise an exception if called
       

    def __add__(self,right):
        pass
    


if __name__ == '__main__':
    # Write any other code here to test Table before doing bsc test; for example
    
    # Here are simple tests not raising exceptions (illustrated in the problem statement)
    # Comment out any tests you no longer want to perform
    # The driver is run at the bottom of this script
    import prompt
    print('For simple test __init__ and beyond to work, __init__ must work correctly')
    print('  for cases when it does not need to throw exceptions.')
    print('Also, calling __iter__ will raise an exception if it is implemented')
    print('   by just pass')
    if prompt.for_bool('\nDo you want to perform simple tests before bsc tests',False):
        # Table (__init__)
        print('\n\n-->Testing Table (__init__), simply')
        employee = Table('Employee', ['Name', 'EmpId', 'DeptName'], [lambda v: type(v) is str, lambda v: type(v) is int and 1000<=v<=9999, lambda v: v in ['Finance','Sales']])
        print(employee)
        print(employee.raw())
        
        
        # add_record
        print('\n\n-->Testing add_record simply')
        employee = Table('Employee', ['Name', 'EmpId', 'DeptName'], [lambda v: type(v) is str, lambda v: type(v) is int and 1000<=v<=9999, lambda v: v in ['Finance','Sales']])
        employee.add_record('Bob',2241,'Sales')
        employee.add_record('Cathy',3401,'Finance')
        employee.add_record('Alice',3415,'Finance')
        employee.add_record('David',2202,'Sales')
        print(employee)
        print(employee.raw())
        
    
        # __call__
        print('\n\n-->Testing __call__ simply')
        employee = Table('Employee', ['Name', 'EmpId', 'DeptName'], [lambda v: type(v) is str, lambda v: type(v) is int and 1000<=v<=9999, lambda v: v in ['Finance','Sales']])
        for i in ['Name', 'EmpId', 'DeptName']:
            print(i,'is in self.fields at index',employee(i))
            
        
        # __getitem__
        print('\n\n-->Testing __getitem__ simply')
        employee = Table('Employee', ['Name', 'EmpId', 'DeptName'], [lambda v: type(v) is str, lambda v: type(v) is int and 1000<=v<=9999, lambda v: v in ['Finance','Sales']])
        employee.records = [['Bob', 2241, 'Sales'], ['Cathy', 3401, 'Finance'], ['Alice', 3415, 'Finance'], ['David', 2202, 'Sales']]
        print(employee[0])
        print(employee[2])
        print(employee[0,'Name'])
        print(employee[0,'EmpId'])
        print(employee[0,'DeptName'])
        
       
        # select_records
        print('\n\n-->Testing select_records simply')
        employee = Table('Employee', ['Name', 'EmpId', 'DeptName'], [lambda v: type(v) is str, lambda v: type(v) is int and 1000<=v<=9999, lambda v: v in ['Finance','Sales']])
        employee.records = [['Bob', 2241, 'Sales'], ['Cathy', 3401, 'Finance'], ['Alice', 3415, 'Finance'], ['David', 2202, 'Sales']]
        sales = employee.select_records('Sales',lambda r : r[employee('DeptName')] == 'Sales')   
        print(sales)
        
        
        #  project
        print('\n\n-->Testing project simply')
        employee = Table('Employee', ['Name', 'EmpId', 'DeptName'], [lambda v: type(v) is str, lambda v: type(v) is int and 1000<=v<=9999, lambda v: v in ['Finance','Sales']])
        employee.records = [['Bob', 2241, 'Sales'], ['Cathy', 3401, 'Finance'], ['Alice', 3415, 'Finance'], ['David', 2202, 'Sales']]
        employee.project('Name','DeptName')
        print(employee)
        print(employee.raw())
        
        #  __iter__
        print('\n\n-->Testing __iter__ simply')
        employee = Table('Employee', ['Name', 'EmpId', 'DeptName'], [lambda v: type(v) is str, lambda v: type(v) is int and 1000<=v<=9999, lambda v: v in ['Finance','Sales']])
        employee.records = [['Bob', 2241, 'Sales'], ['Cathy', 3401, 'Finance'], ['Alice', 3415, 'Finance'], ['David', 2202, 'Sales']]
        for i in employee:
            print(i)
        
        
        #  +
        if prompt.for_bool('\nDo you want to perform extra credit + test',False):
            print('\n\n-->Testing + simply: 1 point extra credit')
            employee = Table('Employee', ['Name', 'EmpId', 'DeptName'], [lambda v: type(v) is str, lambda v: type(v) is int and 1000<=v<=9999, lambda v: v in ['Finance','Sales']])
            employee.records = [['Bob', 2241, 'Sales'], ['Cathy', 3401, 'Finance'], ['Alice', 3415, 'Finance'], ['David', 2202, 'Sales']]
            department = Table('Department', ['Manager', 'DeptName'], [lambda v: type(v) is str, lambda v: v in ['Finance', 'Sales', 'Production']])
            department.records = [['George', 'Finance'], ['Harriet', 'Sales'], ['Charles', 'Production']]
            print(employee+department)


    print('\n\n')
    import driver
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
    driver.driver()
