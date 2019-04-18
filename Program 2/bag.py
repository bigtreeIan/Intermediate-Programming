# Submitter: yihanx2(Xu, Yihan)
# Partner  : zihaog(Gao, Zihao)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
from collections import defaultdict
from goody import type_as_str

class Bag:
    def __init__(self, *bags):
        self.bag = defaultdict(int)
        for bag_list in bags:
            for bag in bag_list:
                self.bag[bag] += 1
    
    def __repr__(self):
        bag_list = []
        result_str = ''
        for keys, values in sorted(self.bag.items(), key = lambda x : x[0]):
            for times in range(values):
                bag_list.append(keys)
        result_str += 'Bag' + '(' + str(bag_list) + ')'
        return result_str
        
    def __str__(self):
        current_str = ''
        final_str = ''
        compact_str = ''
        current_set = set()
        for keys, values in sorted(self.bag.items(), key = lambda x : x[0]):
            current_set.add((keys + '[' + str(values) + ']'))
        for i in current_set:
            final_str += (i + ',')
        final_str = final_str[:-1]
        compact_str = 'Bag(' + final_str + ')' 
        return compact_str
    
    def __len__(self):
        counter = 0
        for values in self.bag.values():
            counter += values
        return counter
    
    def unique(self):
        counter1 = 0
        unique_set = set()
        for keys in self.bag:
            unique_set.add(keys)
        for unique in unique_set:
            counter1 += 1
        return counter1
    
    def __contains__(self, bag):
        for keys in self.bag:
            if bag == keys:
                return True
    
    def count(self, bag):
        counter2 = 0
        for keys, values in self.bag.items():
            if bag == keys:
                counter2 += values
        return counter2
    
    def add(self, new_bag):
        if new_bag in self.bag.keys():
            self.bag[new_bag] += 1
        elif new_bag not in self.bag.keys():
            self.bag[new_bag] += 1
    
    def __add__(self,target):
        if type(target) != type(self) :
            raise TypeError       
        new_bag = Bag()
        for i in target.bag:
            if i not in self.bag:
                new_bag.bag[i] = target.bag[i]          
            else:
                new_bag.bag[i] = target.bag[i] + self.bag[i]    
        for j in self.bag:
            if j not in target.bag:
                new_bag.bag[j] = self.bag[j]        
        return new_bag

    def remove(self,target):      
        if target not in self.bag:
            raise ValueError(target+'could not be removed.')
        elif self.bag[target] == 1:       
            self.bag.pop(target,None)
        else:
            self.bag[target] = self.bag[target]-1

    def __eq__(self,target):
        return self.bag == target
    
    def __ne__(self,target):
        return self.bag != target
    
    def __iter__(self):
        iter_str = ''
        for keys, values in sorted(self.bag.items(), key = lambda x : (x[1], x[0])):
            iter_str += values * keys
        return (iter for iter in iter_str)
            


    

if __name__ == '__main__':
    #driver tests
    import driver
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
