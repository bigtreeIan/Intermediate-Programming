# Define a special exception for use with the Graph class methods
# Use like any exception: e.g., raise GraphError('Graph.method...error indication...')
 
class GraphError(Exception):
    pass # Inherit all methods, including __init
 
 
class Graph:
    # HELPER METHOD: useful for checking legal arguments to methods below
    # Call as Graph.legal_tuple(t2, 2) or as Graph.legal_tuple(t3, 3),
    #   where t2 = ('a','b') - an edge, or t3 = ('a','b',1). an edge value
    @staticmethod
    def legal_tuple(t,needed_len):
        return type(t) is tuple and len(t) == needed_len and\
               type(t[0]) is str and type(t[1]) is str
        
 
    # Write __getitem__ and especially __setitem__ before __init__; they can be/are tested
    #   by setting self.edges directly; once these methods are written, __init__ can be
    #   written more simply/easily by using __setitem__.
         
    # item can be either a str, origin node, or a 2-tuple, (origin node, destination node)        
    def __getitem__(self,item):
        if type(item) is str and item in self.edges:
            return self.edges[item]
        elif Graph.legal_tuple(item,2) and item[0] in self.edges and item[1] in self.edges[item[0]]:
            o,d = item
            return self.edges[o][d]
        else:
            raise GraphError('__getitem__: argument('+str(item)+') illegal or not in Graph')
   
     
    # item must be a 2-tuple, (origin node, destination node)        
    def __setitem__(self,item,value):
        if Graph.legal_tuple(item,2):
            o,d = item
            if o not in self.edges:
                self.edges[o] = {}
            if d not in self.edges:
                self.edges[d] = {}
            self.edges[o][d] = value
        else:
            raise GraphError('Graph.__setitem__: argument('+str(item)+') must be two strings (node names)')
 
 
    # __str__ and many bsc tests use the name self.edges for the outer/inner-dict.
    # So __init__ should use self.edges for the name for this dictionary
    # self should store NO other attributes: compute all results from self.edges ONLY
    # Each value in the edges tuple can be either a 
    #   (a) str = origin node
    #   (b) 3-tuple = (origin node, destination node, edge value) 
    def __init__(self,*edges):
        self.edges = {}
        for odv in edges:
            if type(odv) is str:
                if odv in self.edges:
                    raise GraphError('__init__: illegal node: already in Graph('+str(odv)+')')
                else:
                    self.edges[odv] = {}
 
            elif Graph.legal_tuple(odv,3):
                o,d,v = odv
                if o in self.edges and d in self[o]:
                    raise  GraphError('__init__: illegal edge: already in Graph('+str(odv)+')')
                self[o,d] = v
            else:
                raise GraphError('__init__: illegal node/edge specification('+str(odv)+')')
 
 
    def __str__(self):
        return '\nGraph:\n  '+'\n  '.join(str(o)+': ' + ', '.join(str(d)+'('+str(v)+')' for d,v in sorted(dv.items())) for o,dv in sorted(self.edges.items()))
 
    def all_nodes(self):
        return set(self.edges.keys())
    
    def __len__(self):
        return sum(len(o) for o in self.edges.values())
 
     
    # item can be either a str, node, or a 2-tuple, (origin node, destination node), or a
    #   3-tuple, (origin node, destination node, edge value)         
    def __contains__(self,item):
        if type(item) is str:
            return item in self.edges
        elif Graph.legal_tuple(item,2):
            o,d = item[0],item[1]
            return o in self.edges and d in self.edges[o]
        elif Graph.legal_tuple(item,3):
            o,d,v = item[0],item[1], item[2]
            return o in self.edges and d in self.edges[o] and v == self[o,d]
        else:
            return False
     
     
    # item can be either a str, node, or a 2-tuple, (origin node, destination node)        
    def __delitem__(self,item):
        if type(item) is str: # node only: delete node from graph and all incoming edges
            o = item
            if o not in self.edges:
                return
            del self.edges[o]
            for ao in self.edges:
                if o in self.edges[ao]:
                    del self.edges[ao][o]
        elif Graph.legal_tuple(item,2):
            o,d = item
            if o in self.edges and d in self.edges[o]:
                del self.edges[o][d]        
        else: 
            raise GraphError('Graph.__delitem__: argument('+str(item)+') must be string or two string tuple')
 
 
    # d must be a str, destination node     
    def __call__(self,d):
        if type(d) is str and d in self.edges:
            return {o:v for o,_dv in self.edges.items() for pd,v in self.edges[o].items() if d == pd}
        else:
            raise GraphError('Graph.__call__: argument('+str(d)+') must be node in Graph')
 
  
    # Produces str, nodes with no edges to/from them,
    #   or 3-tuple, (origin node, destination node, edge value),
    #   in alphabetic order by str/origin node 
    #      and by destination node for all edge values with the same origin node        
    def __iter__(self):
        for o in sorted(self.edges):
            if self.edges[o] == {} and not any(o in d for d in self.edges.values()):
                yield o
            else:
                for d in sorted(self[o]):
                    yield (o,d,self[o,d]) 
                                
 
    def __le__(self,right):
        for n in self.edges:
            if n not in right.edges:
                return False
        for o,d,v in self:
            if (o,d) not in right or v != right[o,d]:
                return False
        return True
    
    def out_degree(self,o):
        if o not in self:
            raise GraphError('Graph.out_degree: argument('+str(o)+') must be node in Graph')
        return len(self.edges[o])

    def in_degree(self,d):
        if d not in self:
            raise GraphError('Graph.in_degree: argument('+str(d)+') must be node in Graph')
        return sum(1 if d in destinations else 0 for destinations in self.edges.values())

    # This function is incorrect; don't fix it: I want a failed test in Problem #3 in Quiz #8.
    # It should return: self.out_degree(node) + self.in_degree(node)
    # It returns the correct value only for nodes whose out_degree is 0
    def degree(self,node):
        if node not in self:
            raise GraphError('Graph.__degree__: argument('+str(node)+') must be node in Graph')
        return self.in_degree(node)