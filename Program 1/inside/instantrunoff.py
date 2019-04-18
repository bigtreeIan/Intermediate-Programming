# Submitter: yihanx2(Xu, Yihan)
# Partner: zihaog(Gao, Zihao)
# We certify that we worked cooperatively on this programming
#    assignment, according to the rules for pair programming
import goody
from collections import defaultdict
from _ast import Num

def read_voter_preferences(file : open):
    graph = defaultdict(list)
    for i in file:
        perfer = i.split(';')
        for j in range(len(perfer[1:])):
            graph[perfer[0]].append(perfer[j + 1][0])
    return dict(graph)

def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    result = ''
    for i, j in sorted(d.items(), key = key, reverse= reverse):
        result += '  ' + str(i) + ' -> ' + str(j) + '\n'
    return result
    
def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    number_vote = defaultdict(int)
    for voter, candidates in vp.items():
        for candidate in candidates:
            if (candidate in cie) == True:
                number_vote[candidate] += 1
            else:
                candidates.remove(candidate)
                for candidate in candidates:
                    if (candidate in cie) == True:
                        number_vote[candidate] += 1
                    break  
            break
    return number_vote

def remaining_candidates(vd : {str:int}) -> {str}:
    remain_set = set()
    target = min(vd.items(), key = lambda x: x[1])
    for candidates, votes in vd.items():
        if votes > target[-1]:
            remain_set.add(candidates)
    return remain_set

def run_election(vp_file : open) -> {str}:
    pre_dict = read_voter_preferences(vp_file)
    dict_str = dict_as_str(pre_dict, lambda x: x[0])
    print('Voter Preferences')
    print(dict_str)
    candidates = list(pre_dict.values())[0]
    votes = evaluate_ballot(pre_dict, set(candidates)) 
    print('Vote count on ballot #1 with candidates (alphabetically) = ', set(candidates))
    alph_votes_str = dict_as_str(votes, key=lambda x :x[0], reverse = False) 
    print(alph_votes_str)      
    print('Vote count on ballot #1 with candidates (numerically) = ', set(candidates))
    num_votes_str = dict_as_str(votes, key=lambda x : x[1], reverse = True)
    print(num_votes_str)
    counter = 2
    while True:
        cie = remaining_candidates(votes)     
        if len(cie) > 1: 
            print('Vote count on ballot#',counter,'with candidates (alphabetically) = ',cie)
            votes = evaluate_ballot(pre_dict, cie)
            vote2_str = dict_as_str(votes, key=lambda x :x[0], reverse = False)
            print(vote2_str)
            print('Vote count on ballot#',counter,'with candidates (numerically) = ',cie)
            vote3_str = dict_as_str(votes, key=lambda x :x[1], reverse= False)
            print(vote3_str)
            counter += 1
        elif len(cie) <= 1:
            return cie 
   
if __name__ == '__main__':
    # Write script here
    file = input('Enter file with voter preferences: ')
    file_opened = open(file, 'r')
    result = run_election(file_opened)
    print('winner is : ', result)
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
