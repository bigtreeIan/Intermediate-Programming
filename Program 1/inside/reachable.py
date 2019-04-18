# Submitter: yihanx2(Xu, Yihan)
# Partner: zihaog(Gao, Zihao)
# We certify that we worked cooperatively on this programming
#    assignment, according to the rules for pair programming
import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    graph = defaultdict(set)
    for i in file:
        graph[i[0]].add(i[2])
    return dict(graph)

def graph_as_str(graph : {str:{str}}) -> str:
    result = ''
    for i,j in sorted(graph.items(), key = lambda item : item[0]):
         result += '  ' + str(i) + ' -> ' + str(sorted(list(j))) + '\n'
    return result
          
def reachable(graph : {str:{str}}, start : str) -> {str}:
    source = set()
    change_list = [start]
    while len(change_list) != 0:
        dest = change_list.pop(0)
        if dest in graph and dest not in source:
            change_list += list(graph.get(dest, set()))
        source.add(dest)
    return source  
        


if __name__ == '__main__':
    # Write script here
    file_name = input('pleas enter a file name: ')
    file_text = open(file_name, 'r')
    graph = read_graph(file_text)
    graph_as_str(graph)
    while True:
        text = input('Enter a starting node name: ')
        if text != 'quit':
            if reachable(graph, text) == set():
                print('Entry Error: '+ text + ';' + ' Illegal: not a source node' + '\n' + 'Please enter a legal String')
                continue
            else:
                print(reachable(graph, text))
        else:
            break 
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
