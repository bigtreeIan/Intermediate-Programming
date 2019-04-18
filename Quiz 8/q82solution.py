import cProfile
from graph_goody import random_graph, spanning_tree
import pstats

# Put script here to generate data for Problem #2
# In case you fail, the data appears in sample8.pdf in the helper folder
correct_size_1 = random_graph(50000, lambda n: n * 10)
cProfile.run('spanning_tree(correct_size_1)', 'correct_size_1')
p = pstats.Stats('correct_size_1')
p.sort_stats('calls').print_stats()
correct_size_2 = random_graph(100000, lambda n: n * 10)
cProfile.run('spanning_tree(correct_size_2)', 'correct_size_2')
p = pstats.Stats('correct_size_2')
p.sort_stats('time').print_stats()