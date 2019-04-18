# Submitter: yihanx2(Xu, Yihan)
# Partner: zihaog(Gao, Zihao)
# We certify that we worked cooperatively on this programming
#    assignment, according to the rules for pair programming


import prompt 
from goody       import safe_open, irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    all_set = set()
    all_tuple = ()
    for i in fq:
        all_tuple += (i,)
        all_set.add(all_tuple)
    return all_set

def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    for a in all_prefixes(new_query):
        prefix[a].add(new_query)
    query[new_query] += 1
        
def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    prefix_dic = defaultdict(set)
    query_dic =  defaultdict(int)
    for i in open_file:
        str_tuple = ()
        for j in ((i.replace('\n', '')).split(' ')):
            str_tuple += (j,)
        add_query(prefix_dic,query_dic,str_tuple)
    final_tuple = ()
    final_tuple += (dict(prefix_dic),)
    final_tuple += (dict(query_dic),)
    return final_tuple
    
def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    str1 = ''
    for key1 in sorted(list(d.keys()), key = key, reverse = reverse):
        str1 += '  ' + str(key1) + ' -> '+ str(d[key1]) + '\n'
    return str1
    
def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    target_prefix = prefix[a_prefix]
    query_list = []
    final_list = []
    for i in target_prefix:
        num = query[i]
        query_list.append((i,num))
        order = sorted(query_list, key = lambda x: -x[1])
    top_3 =sorted(order[:n], key = lambda x: (-x[1],x))
    for i in top_3:
        final_list.append(i[0])
    return final_list
        

# Script

if __name__ == '__main__':
    # Write script here
    file = input('Enter file with full queries: ')
    opened_file = open(file, 'r')
    i,j = read_queries(opened_file)
    while True:
        print('Prefix dictionary:')
        prefix_str = dict_as_str(i, key = lambda y : (len(y), y), reverse = False)
        print(prefix_str)
        print('Query dictionary: ')
        query_str = dict_as_str(j, key = lambda y: (-j[y], y), reverse = False)
        print(query_str)
        input_str = input('Enter prefix (or quit): ')
        if input_str == 'quit':
            break
        else:
            input_tuple_1 = tuple(input_str.split(' '))
            print('  Top 3 (at most) full queries = ', top_n(input_tuple_1, 3, i, j))
        input_str_2 = input('Enter full query (or quit): ')
        if input_str_2 == 'quit':
            break
        else:
            input_tuple = tuple(input_str_2.split(' '))
            add_query(i, j, input_tuple)
    
    
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
