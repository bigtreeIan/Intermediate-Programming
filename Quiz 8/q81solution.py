from performance import Performance
from goody import irange
from graph_goody import random_graph, spanning_tree

# Put script here to generate data for Problem #1
# In case you fail, the data appears in sample8.pdf in the helper folder

def creat_random(n):
    global correct_size
    correct_size = random_graph(n, lambda n: n*10) 
for i in irange(0, 7):
    n = 1000
    n = n * (2**i)
    p = Performance(lambda: spanning_tree(correct_size), lambda: creat_random(n), 5, title = 'Spanning Tree of size {}'.format(n))
    p.evaluate()
    p.analyze()
    print()