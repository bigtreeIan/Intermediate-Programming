import unittest  # use unittest.TestCase
from graph import Graph, GraphError


class Test_Graph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(('a','b',1), ('a','c',3), ('b','a',2), ('d','b',2), ('d','c',1), 'e')
    
    def test_del(self):
        n = 5
        for i in self.graph:
            self.assertEqual(len(self.graph), n)
            if type(i) == tuple:
                del self.graph[i[0]][i[1]]
                n = n - 1
            
    def test_del_nd(self):
        self.keylist = []
        self.packstr = ''
        self.assertEqual(len(self.graph), 5)
        for i in self.graph.edges:
            self.keylist.append(i)
            self.sortedlist = sorted(self.keylist, reverse = True)
        for j in self.sortedlist:
            self.packstr += j
        pack = zip(self.packstr, (5, 3, 2, 0, 0))
        for i in pack:
            del self.graph[i[0]]
            self.assertEqual(len(self.graph), i[1])
    
    def test_del_rd(self):
        self.assertRaises(GraphError, self.graph.__delitem__, 1)
        self.assertRaises(GraphError, self.graph.__delitem__, ('a','b', 1, 1))
        self.assertRaises(GraphError, self.graph.__delitem__, (2, 'b'))
        self.assertRaises(GraphError, self.graph.__delitem__, ('b', 1))
        
    def test_in(self):
        for i, j in self.graph.edges.items():
            self.assertTrue(i in self.graph)
            for key in j.keys():
                self.assertTrue(key in self.graph)
                self.assertTrue((i, key) in self.graph)
                self.assertTrue((i, key, self.graph.edges[i][key]) in self.graph)
        self.assertFalse('y' in self.graph)
        self.assertFalse(('c', 'a') in self.graph)
        self.assertFalse(('a', 'c', 4) in self.graph)

    def test_degree(self):
        created_dic = {n: self.graph.degree(n) for n in self.graph.edges.keys()}
        self.assertDictEqual(created_dic, {'a':3, 'b':3, 'c':2, 'd':2, 'e':0})
            
        
        
        
        