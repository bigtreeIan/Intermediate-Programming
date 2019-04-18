# Submitter: yihanx2(Xu, Yihan)
# Partner  : zihaog(Gao, Zihao)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from _collections import defaultdict

class GraphError(Exception):
    pass
    
 
class Graph:
    def legal_tuple2(self,t):
        return type(t) is tuple and len(t) == 2 and\
               type(t[0]) is str and type(t[1]) is str

    def legal_tuple3(self,t):
        return type(t) is tuple and len(t) == 3 and\
               type(t[0]) is str and type(t[1]) is str and self.is_legal_edge_value(t[2])

    def __init__(self,legal_edge_value_predicate,*edges):
        self.edges = defaultdict(dict)
        self.is_legal_edge_value = legal_edge_value_predicate
        check_list = []
        check_list2 = edges
        check_list3 = []     
        for i in edges:
            counter = 0
            for j in check_list2:
                if i == j:
                    counter += 1
            if counter >= 2:
                raise GraphError('The same tuple error')            
        for edge in edges:
            if Graph.legal_tuple3(self,edge) == True:
                if edge[0] not in self.edges:
                    dic = defaultdict(int)
                    dic[edge[1]] = edge[2]
                    self.edges[edge[0]] = dict(dic)
                    check_list3.append(edge[0])
                    check_list3.append(edge[1])
                    check_list.append(edge[1])
                else: 
                    self.edges[edge[0]][edge[1]] = edge[-1]
                    check_list.append(edge[1])
            elif type(edge) == str and len(edge) == 1:
                if edge not in check_list3:
                    self.edges[edge] = {} 
                else: raise GraphError('The string and tuple is duplicated') 
            else:
                raise GraphError('The parameter should be a tuple ends with an integer')
        for i in check_list:
            if i not in self.edges:
                self.edges[i] = {}

    def __str__(self):
        result = ''
        result2 = ''
        for i, j in sorted(self.edges.items()):
            for a, b in sorted(j.items()): 
                result +=  ' ' + str(a) + '(' + str(b) + ')' + ','
            result = result[:-1]
            result2 += '  ' + str(i)+ ':' + result + '\n'
            result = ''
        return '\nGraph:\n'+result2[:-1]
    
    def __getitem__(self, item_tuple):
        if Graph.legal_tuple2(self, item_tuple) == True:
            if item_tuple[0] in self.edges:
                if item_tuple[-1] in self.edges[item_tuple[0]]:
                    num = self.edges[item_tuple[0]][item_tuple[-1]]
                    return num
                else:
                    raise GraphError('The edge in tuple is not reachable')
            else:
                raise GraphError('The edge in tuple is not reachable')
        elif type(item_tuple) == str and len(item_tuple) == 1:
            if item_tuple in self.edges:
                return self.edges[item_tuple] 
            else:
                raise GraphError('The string is not in dictionary')
        else:
            raise GraphError('The item should be a string or a tuple')
    
    def __setitem__(self, item_tuple2, distance):
        if type(distance) != int:
            raise GraphError('Distance should be integer')
        if Graph.legal_tuple2(self, item_tuple2) == True:
            if item_tuple2[0] in self.edges:
                if item_tuple2[-1] not in self.edges:
                    self.edges[item_tuple2[-1]] = {}
            elif item_tuple2[0] not in self.edges:
                if item_tuple2[-1] not in self.edges:
                    self.edges[item_tuple2[-1]] = {}
                self.edges[item_tuple2[0]] = {} 
            self.edges[item_tuple2[0]][item_tuple2[-1]] = distance      
        else:       
            raise GraphError('The edge in tuple is not reachable')
                
    def node_count(self):
        return len(self.edges.keys())
    
    def __len__(self):
        counter = 0
        for i in self.edges.values():
            if i != {}:
                counter += len(i)               
        return counter
    
    def out_degree(self,node):
        if node in self.edges and type(node) is str:
            return len(self.edges[node])
        else:
            raise GraphError('No such node that matched')
    
    def in_degree(self,node):
        check_list = []
        for i, j in self.edges.items():
            for k in j:
                check_list.append(k)
        counter = 0
        for l in check_list:
            if l == node:
                counter+=1
        if node not in check_list and node not in self.edges:
            raise GraphError('No such node')            
        return counter

    def __contains__(self, item_input):
        if type(item_input) == str:
            if item_input in self.edges.keys():
                return True
            else:
                return False
        elif Graph.legal_tuple2(self, item_input) == True:
            if item_input[0] in self.edges:
                if item_input[-1] in self.edges[item_input[0]]:
                    return True
                else:
                    return False
            else:
                return False
        elif Graph.legal_tuple3(self,item_input) == True:
            if item_input[0] in self.edges:
                if item_input[1] in self.edges[item_input[0]]:
                    if self.edges[item_input[0]][item_input[1]] == item_input[-1]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            raise GraphError('Parameter should me a string or tuple')
    
    def __delitem__(self, item_input2):
        if type(item_input2) == str:
            if item_input2 in self.edges:
                self.edges.pop(item_input2, None)
                for keys, values in self.edges.items():
                    if item_input2 in values:
                        values.pop(item_input2, None) 
        elif Graph.legal_tuple2(self, item_input2) == True:
            if item_input2[0] in self.edges:
                if item_input2[-1] in self.edges[item_input2[0]]:
                    self.edges[item_input2[0]].pop(item_input2[-1], None)
        else:
            raise GraphError
    
    def __call__(self, d):
        result = {}
        result1 = defaultdict(dict)
        check_list=[]
        for node, edge in self.edges.items():
            for i in edge:
                if i not in result1:  
                    check_list.append(i)                
                    result[node] = edge[i]
                    result1[i] = result
                    result = {}
                else:
                    result1[i][node] = edge[i]
        if d not in check_list and d not in self.edges:
            raise GraphError('Input not in graph')
        else:
            for i in dict(result1):
                if i != d :
                    result1[i] = None 
            return result1[d]

    def clear(self):     
        self.edges.clear()
    
    def dump(self, opened_file, string = ':', f = lambda x : str(x)):
        file_str = ''
        for keys, values in sorted(self.edges.items()):
            file_str += str(keys)
            for sub_keys, sub_values in sorted(values.items()):
                file_str += string + sub_keys + string + f(sub_values)
            file_str += '\n'
        print(file_str[:-1],file = opened_file)
        opened_file.close()
                 
    def load(self, opened_file, string = ':', f = lambda x : int(x)):
        dic1 = {}
        for i in opened_file:
            inner_dic = {}
            i = i.replace('\n','')
            items = i.split(string)
            key = items.pop(0)
            if key == '':
                break
            while  items != [] :
                inner_dic[items.pop(0)] = f(items.pop(1))
            self.edges[key] = inner_dic
        opened_file.close()
    
    def reverse(self):
        lis1 = []
        new_graph = 'Graph(self.is_legal_edge_value, '
        for i in self:
            if Graph.legal_tuple3(self, i) == True:
                j = list(i)
                j[0],j[1] = j[1],j[0]
                j = tuple(j)
                lis1.append(j)
            else:
                lis1.append(i)
        for j in lis1:
            if type(j) == str:
                j = "'" + j + "'"
            new_graph += "{0},".format(j)
        new_graph = eval(new_graph[:-1] + ')')
        return new_graph
    
    def natural_subgraph(self, *nodes):   
        new_graph = "Graph(self.is_legal_edge_value, "
        for i in self:
            if type(i) == str:
                i = "'" + i + "'"
            new_graph += "{0},".format(i)
        new_graph = new_graph[:-1]
        new_graph = eval(new_graph[:-1] + "')")
        
        check_set = set()
        if not any(type(node) is str for node in nodes):
            raise GraphError('Nodes must be a string')
        else:
            for keys in self.edges:
                check_set.add(keys)
                for sub_keys in self.edges[keys]:
                    check_set.add(sub_keys)
            for new_nodes in nodes:
                if new_nodes in check_set:
                    check_set.remove(new_nodes)
            for item_input2 in check_set:
                if item_input2 in self.edges:
                    new_graph.edges.pop(item_input2, None)
                    for keys, values in new_graph.edges.items():
                        if item_input2 in values:
                            values.pop(item_input2, None) 
        return new_graph 
    
    def __iter__(self):
        for ori_nodes, des_nodes in sorted(self.edges.items()):
            if des_nodes != {}:
                for sub_nodes, values in sorted(des_nodes.items()):
                     yield (ori_nodes, sub_nodes, values)
            else:
                if not any(ori_nodes in values for values in self.edges.values()):
                    yield ori_nodes

    def __eq__(self, graph):
        return self.edges == graph.edges
    
    def __ne__(self, graph):
        return self.edges != graph.edges
    
    def __le__(self,graph):
        for ori_nodes, des_nodes in self.edges.items():
            if ori_nodes not in graph.edges: 
                return False
        for ori_nodes2, des_nodes2, values in self:
            if (ori_nodes2, des_nodes2) not in graph or values != graph[ori_nodes2][des_nodes2]:
                return False
            elif (ori_nodes2, des_nodes2) in graph and values != graph[ori_nodes2][des_nodes2]:
                return False
            elif (ori_nodes2, des_nodes2) not in graph and values == graph[ori_nodes2][des_nodes2]:
                return False
        return True

    def __add__(self, target_graph):
        new_graph = 'Graph(self.is_legal_edge_value, '
        for i in self:
            new_graph += "{0},".format(i)
        new_graph = eval(new_graph[:-1] + ')')
        key_list = []
        new_edges = new_graph.edges
        if type(target_graph) == type(self):
            for target_outer_key in target_graph.edges:
                if target_outer_key not in self.edges:
                    new_edges[target_outer_key] = target_graph.edges[target_outer_key]
                else:
                    for i in target_graph[target_outer_key]:
                        print(target_graph,i)
                        if i not in self.edges[target_outer_key]:
                            new_edges[target_outer_key][i] = target_graph[target_outer_key][i]
            return new_graph
        elif type(target_graph) == str:
            if target_graph not in self.edges:
                new_graph.edges[target_graph] = {} 
                return new_graph
        elif Graph.legal_tuple3(self,target_graph) == True:
            new_edges[target_graph[0]][target_graph[1]] = target_graph[2]
            if target_graph[1] not in new_edges:
                new_edges[target_graph[1]] = {}
            return new_graph
        else:
            raise GraphError
        
    def __radd__(self, left):
        return(self + left)
        
    def __iadd__(self,new_graph):
        self = self + new_graph
        return(self)
    
    def __setattr__(self,name,value):
        if 'edges' not in self.__dict__ or 'is_legal_edge_value' not in self.__dict__:
            self.__dict__[name] = value
        else:
            raise AssertionError('cannot add new attribute or rebinding old attribute')

        
        
    
    
            
            
            
                
        
    
        
    

            
        
        
        
g = Graph( (lambda x : type(x) is int), ('a','b',1),('a','c',3),('b','a',2),('d','b',2),('d','c',1),'e')
f = g.reverse()
print(f.edges)#-->{'b': {'a': 1, 'd': 2}, 'e': {}, 'a': {'b': 2}, 'c': {'a': 3, 'd': 1}, 'd': {}}       
        
        
        
         
if __name__ == '__main__':
    #Put code here to test Graph before doing bsc test; for example
    g = Graph( (lambda x : type(x) is int), ('a','b',1),('a','c',3),('b','a',2),('d','b',2),('d','c',1),'e')
    print(g)
    print(g['a'])
    print(g['a','b'])
    print(g.node_count())
    print(len(g))
    print(g.out_degree('c'))
    print(g.in_degree('a'))
    print('c' in g)
    print(('a','b') in g)
    print(('a','b',1) in g)
    print(g('c'))
    opened_file = open('project_2_test_file','w')
    string = ':'
    f = lambda x : str(x)
    g.dump(opened_file, string, f)
    
    opened_file = open('project_2_test_file','r')
    f = lambda x : int(x)
    g.load(opened_file, string, f)
    
    print(g.reverse())
    print(g.natural_subgraph('a','b','c'))
    print()    
    import driver
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
