# Submitter: yihanx2(Xu, Yihan)
# Partner: zihaog(Gao, Zihao)
# We certify that we worked cooperatively on this programming
#    assignment, according to the rules for pair programming
import goody
from collections import defaultdict


def read_ndfa(file : open) -> {str:{str:{str}}}:
    info_dict = defaultdict(dict)
    inner_dict = defaultdict(set)
    key_list = []
    num_list = []
    str_list = []
    final_list = []
    for line in file:
        line_list = line.split(';')
        line_list[-1] = line_list[-1].replace('\n', '')
        if line_list != []:
            key = line_list.pop(0)
            for j in line_list:
                if line_list.index(j)%2 == 0:
                    num_list.append(j)
                else:
                    str_list.append(j)
            for i in range(len(str_list)):
                if num_list != [] and str_list != []:
                    inner_dict[num_list.pop(0)].add(str_list.pop(0))
            info_dict[key] = dict(inner_dict)
            inner_dict = defaultdict(set)  
    return dict(info_dict)

def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    result = ''
    for i, j in sorted(ndfa.items()):
        for k in j:
            j[k] = list(j[k])
        result += '  ' + str(i) + ' transitions: ' + str(sorted(list(sorted(j.items())))) + '\n'
    return result

def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    change_list = []
    change_list.append(state)
    stable_list = []
    stable_list.append(state)
    state_tuple = ()
    for i in inputs:
        i = i.replace('\n', '')
        state_set = set()
        while len(change_list) != 0:
            state = change_list.pop(0)
            if i in ndfa[state]:
                state_set = state_set.union(ndfa[state][i])
        state_tuple = (i, state_set)
        stable_list.append(state_tuple)
        change_list += list(state_set)
        if state_set == set():
            break
    return stable_list

def interpret(result : [None]) -> str:
    str2 = ''
    str2 += 'Start state = ' + str(result.pop(0))+'\n'
    for i in range(len(result)):  
        str2 += '  Input = '+str(result[i][0])+'; new possible states = '+str(sorted(list(result[i][1])))+'\n'
    str2 +='Stop state(s) = '+ str(sorted(list(result[-1][-1])))+'\n'
    print(str2)
    return str2

if __name__ == '__main__':
    file = input('Enter file with non-deterministic finite automaton: ')
    print()
    print('Non-Deterministic Finite Automaton')
    opened_file = open(file, 'r')
    ndfa_dict = read_ndfa(opened_file)
#     for i, j in ndfa_dict.items():
#         print(i, 'transitions: ', list(j.items()))
#     print()
    fa_str = ndfa_as_str(ndfa_dict)
    print(fa_str);
    state_file = input('Enter file with the start-state and input: ')
    print()
    opened_state_file = open(state_file, 'r')
    for i in opened_state_file:
        state = i.split(';')
        ndfa_result = process(ndfa_dict, state[0], state[1:])
        print('Starting new simulation')
        interpret(ndfa_result)
        print()
        
        
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
