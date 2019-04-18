# Submitter: yihanx2(Xu, Yihan)
# Partner: zihaog(Gao, Zihao)
# We certify that we worked cooperatively on this programming
#    assignment, according to the rules for pair programming
import goody
from collections import defaultdict

def read_fa(file : open) -> {str:{str:str}}:
    num_list = []
    str_list = []
    key_list = []
    final_list = []
    final_dict = defaultdict(dict)
    for i in file:
        items = i.split(';')
        items[-1] = items[-1].replace('\n','')
        key_list.append(items.pop(0))
        for j in items:
            try:
                num_list.append(str(int(j)))
            except:
                str_list.append(j)
        final_list.append(dict(zip(num_list, (str_list))))
    for i in range(len(key_list)): 
        final_dict[key_list[i]] = final_list[i]
    
    return final_dict
    
def fa_as_str(fa : {str:{str:str}}) -> str:
    result = ''
    for i, j in sorted(fa.items()):
        result += '  ' + str(i) + ' transitions: ' + str(list(sorted(j.items()))) + '\n'  
    return result

def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    result_list = []
    result_list.append(state)
    for i in inputs:
        i = i.replace('\n', '')
        state_tuple = ()
        try:
            state = fa[state][str(int(i))]            
            state_tuple += (i,)
            state_tuple += (state,) 
            result_list.append(state_tuple) 
        except:
            state_tuple += (i,)
            state_tuple += (None,)
            result_list.append(state_tuple)     
    return result_list

def interpret(fa_result : [None]) -> str:
    str1 = ''
    str1 +='Start state = '+ str(fa_result.pop(0))+'\n'
    for i in range(len(fa_result)):
        if fa_result[i][1] == None:
            str1 += '  Input = ' + str(fa_result[i][0]) + '; illegal input: simulation terminated' + '\n'
        else:
            str1 += '  Input = ' + str(fa_result[i][0]) + '; new state = ' + str(fa_result[i][1])+ '\n'
    #print('11111111', str1 +'  Stop state = ' + str(fa_result[-1][-1])+'\n')
    return str1 +'Stop state = ' + str(fa_result[-1][-1])+'\n'
        
if __name__ == '__main__':
    # Write script here
    file = input('Enter file with finite automaton: ')
    print()
    print('Finite Automaton')
    opened_file = open(file, 'r')
    fa = read_fa(opened_file)
    for i, j in fa.items():
        print(i, 'transitions: ', sorted(j.items()))
    print()
    fa_as_str(fa)
    state_open = input('Enter file with the start-state and input: ')
    print()
    state = open(state_open,'r')
    for i in state:
        splited_state = i.split(';')
        fa_result = process(dict(fa), splited_state[0], splited_state[1:])
        print('Starting new simulation')
        print(interpret(fa_result))
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
