from collections import defaultdict


# Helper global variable for use in top and class_averages function
# Do not mutate it: example use, UCI['C+'] returns 2.3
UCI = {'A+': 4.0, 'A': 4.0,'A-': 3.7,
       'B+': 3.3, 'B': 3.0,'B-': 2.7,
       'C+': 2.3, 'C': 2.0,'C-': 1.7,
       'D+': 1.3, 'D': 1.0,'D-': 0.7,
       'F': 0.0}


def top(student_info : {(str,str)}) -> {str}:
    set1 = set()
    list1= []
    info_dic = dict(student_info)
    new_dic = info_dic.items()
    if student_info != set():
        for stu, score in new_dic:
            new_dic1 = sorted(new_dic, key = lambda x : UCI[x[-1]], reverse = True)
            set1.add(new_dic1[0][0])        
        return set1
    else:
        return set()
    
    
def read_db(file : open) -> {str:{(str,str)}} :
    info_dic = defaultdict(set)
    tuple1 = ()
    for line in file:
        l1 = line.split(':')
        key1 = l1.pop(0)
        for i in l1:
            l2 = i.split(',')
            for j in l2:
                z = j.replace('\n', '')
                tuple1 += z,
            info_dic[key1].add(tuple1)
            tuple1 = ()
    return dict(info_dic)
        
        
def class_averages(db : {str:{(str,str)}}) -> {str:float}:
    dic3 = defaultdict(int)
    score = 0
    for i, j in db.items():
        for a,b in j:
            score += int(UCI[b])
        av = score / len(j)
        score = 0
        dic3[i] = av
    return dict(dic3)
        
def class_roster(db : {str:{(str,str)}}) -> [str,[str]]:
    tuple2 = ()
    list2 = []
    list_big = []
    for i, j in db.items():
        tuple2 += i,
        for a, b in j:
            list2.append(a)
            new_list = sorted(list2)
        tuple2 += new_list,
        list2 = []
        list_big.append(tuple2)
        tuple2 = ()
        new1 = sorted(list_big, reverse = True)
    return new1
        
        
def student_view(db : {str:{(str,str)}}) -> {str:{(str,str)}}:
    dic1 = defaultdict(set)
    tuple1 = ()
    for i, j in db.items():
        for a,b in j:
            tuple1 += i,
            tuple1 += b,
            dic1[a].add(tuple1)
            tuple1 = ()
    return dic1
            



 

if __name__ == '__main__':
    import prompt
    
    # checks whether answer is correct, printing appropriate information
    # Note that dict/defaultdict will compare == if they have the same keys and
    #   associated values, regardless of the fact that they print differently
    def check (answer, correct):
        if (answer   == correct):
            print ('    Correct')
        else:
            print ('    INCORRECT')
            print ('      was       =',answer)
            print ('      should be =',correct)
        print()

####################


    if prompt.for_bool('Test top_students?', True):        
        students = {('Alice','C'),('Bob','B-'),('Carol','B-'),('David','D'),('Evelyn','C+')}
        print('  argument =',students)
        answer   = top(students)
        print('  answer   =', answer)
        check(answer, {'Bob','Carol'})
        
        students = {('Alice','B+'),('Bob','B'),('Carol','C'),('David','B-')}
        print('  argument =',students)
        answer   = top(students)
        print('  answer   =', answer)
        check(answer, {'Alice'})
        
        students = {('Alice','C'),('Bob','D'),('Carol','C'),('David','F'),('Evelyn','C')}
        print('  argument =',students)
        answer   = top(students)
        print('  answer   =', answer)
        check(answer, {'Alice','Carol','Evelyn'})
        
        students = set()            # No students
        print('  argument =',students)
        answer   = top(students)
        print('  answer   =', answer)
        check(answer, set())
        


    if prompt.for_bool('Test read_db?', True):        
        print('  argument = fall15.txt')
        answer   = read_db(open('fall15.txt'))
        print('  answer   =', answer)
        check(answer, {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')}, 'Math-3A': {('Bob', 'B'), ('Alice', 'A')}})

        print('  argument = spring15.txt')
        answer   = read_db(open('spring15.txt'))
        print('  answer   =', answer)
        check(answer, {'ICS-6D': {('Bob', 'B'), ('Alice', 'A')},
                       'Math-3A': {('Bob', 'B'), ('Alice', 'A'), ('Evelyn', 'A-'), ('Frank', 'C+')},
                       'ICS-31': {('Frank', 'C-'), ('Bob', 'B+'), ('Carol', 'C+'), ('David', 'B-')},
                       'English-28A': {('David', 'A'), ('Evelyn', 'A'), ('Carol', 'A')}})



    if prompt.for_bool('Test class_averages?', True):        
        db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')}, 'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
        print('  argument =',db)
        answer   = class_averages(db)
        print('  answer   =', answer)
        check(answer, {'Math-3A': 3.5, 'ICS-31': 3.0})

        db = {'ICS-6D': {('Bob', 'B'), ('Alice', 'A')},
              'Math-3A': {('Bob', 'B'), ('Alice', 'A'), ('Evelyn', 'A'), ('Frank', 'C')},
              'ICS-31': {('Frank', 'C'), ('Bob', 'B'), ('Carol', 'C'), ('David', 'B')},
              'English-28A': {('David', 'A'), ('Evelyn', 'A'), ('Carol', 'A')}}
        print('  argument =',db)
        answer   = class_averages(db)
        print('  answer   =', answer)
        check(answer, {'ICS-6D': 3.5, 'ICS-31': 2.5, 'Math-3A': 3.25, 'English-28A': 4.0})



    if prompt.for_bool('Test class_roster?', True):        
        db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')}, 'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
        print('  argument =',db)
        answer   = class_roster(db)
        print('  answer   =', answer)
        check(answer, [('Math-3A', ['Alice', 'Bob']), ('ICS-31', ['Bob', 'Carol', 'David'])] )

        db = {'ICS-6D': {('Bob', 'B'), ('Alice', 'A')},
              'Math-3A': {('Bob', 'B'), ('Alice', 'A'), ('Evelyn', 'A-'), ('Frank', 'C+')},
              'ICS-31': {('Frank', 'C-'), ('Bob', 'B+'), ('Carol', 'C+'), ('David', 'B-')},
              'English-28A': {('David', 'A'), ('Evelyn', 'A'), ('Carol', 'A')}}
        print('  argument =',db)
        answer   = class_roster(db)
        print('  answer   =', answer)
        check(answer, [('ICS-6D', ['Alice', 'Bob']),
                       ('English-28A', ['Carol', 'David', 'Evelyn']),
                       ('ICS-31', ['Bob', 'Carol', 'David', 'Frank']),
                       ('Math-3A', ['Alice', 'Bob', 'Evelyn', 'Frank'])] )



    if prompt.for_bool('Test student_view?', True):        
        db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')}, 'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
        print('  argument =',db)
        answer   = student_view(db)
        print('  answer   =', answer)
        check(answer, {'Carol': {('ICS-31', 'B')}, 'Alice': {('Math-3A', 'A')}, 'Bob': {('Math-3A', 'B'), ('ICS-31', 'A')}, 'David': {('ICS-31', 'C')}} )

        db = {'ICS-6D': {('Bob', 'B'), ('Alice', 'A')},
                       'Math-3A': {('Bob', 'B'), ('Alice', 'A'), ('Evelyn', 'A-'), ('Frank', 'C+')},
                       'ICS-31': {('Frank', 'C-'), ('Bob', 'B+'), ('Carol', 'C+'), ('David', 'B-')},
                       'English-28A': {('David', 'A'), ('Evelyn', 'A'), ('Carol', 'A')}}
        print('  argument =',db)
        answer   = student_view(db)
        print('  answer   =', answer)
        check(answer, {'Frank': {('ICS-31', 'C-'), ('Math-3A', 'C+')},
                       'David': {('ICS-31', 'B-'), ('English-28A', 'A')},
                       'Evelyn': {('Math-3A', 'A-'), ('English-28A', 'A')},
                       'Carol': {('ICS-31', 'C+'), ('English-28A', 'A')},
                       'Alice': {('Math-3A', 'A'), ('ICS-6D', 'A')},
                       'Bob': {('Math-3A', 'B'), ('ICS-31', 'B+'), ('ICS-6D', 'B')}} )
