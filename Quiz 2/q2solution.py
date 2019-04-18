import re
from goody import irange

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the file pattern.txt

def pages (page_spec : str) -> [int]: #result in ascending order (no duplicates)
    page_num_set = set()
    page_list = page_spec.split(',')
    for pages in page_list:
        result = re.match('^[1-9](\d+)?(-[1-9](\d+)?|-[1-9](\d+)?/[1-9](\d+)?)?$', pages)
        if result == None:
            raise AssertionError
        elif result != None:
            page_num = result.group(0)
            dash_index = page_num.find('-')
            if dash_index == -1:
                page_num_set.add(int(page_num))
            elif dash_index != -1:
                start_page = int(page_num[0: dash_index])
                slash_index = page_num.find('/')
                if slash_index == -1:
                    end_page = int(page_num[dash_index + 1:])
                    if start_page <= end_page:
                        for page in range(start_page, end_page + 1):
                            page_num_set.add(page)
                    elif start_page > end_page:
                        raise AssertionError
                elif slash_index != -1:
                    end_page = int(page_num[dash_index + 1: slash_index])
                    skip_page = int(page_num[slash_index + 1:])
                    if start_page <= end_page:
                        for page in range(start_page, end_page + 1, skip_page):
                            page_num_set.add(page)
                    elif start_page > end_page:
                        raise AssertionError
    page_num_list = sorted(list(page_num_set))
    return page_num_list

def expand_re(pat_dict:{str:str}):
    for key, value in pat_dict.items():
        remember_pattern = re.compile('#' + str(key) + '#')
        for new_key, new_value in pat_dict.items():
            pat_dict[new_key] = remember_pattern.sub('(' + str(value) + ')', new_value)
    return None
        

if __name__ == '__main__':
    print('Testing  examples of pages that returns lists')
    
if __name__ == '__main__':
    print('Testing  examples of pages that returns lists')
    
    print("  pages('5,3,9')        :", pages('5,3,9'))
    print("  pages('3-10,5-8,1-2') :", pages('3-10,5-8,1-2'))
    print("  pages(r'6-8,5-11/2,3'):", pages(r'6-8,5-11/2,3'))
    try:
        pages('5-3')
        print('  pages(5-3)            : Error: should have raised exception')
    except:
        print("  pages('5-3')          : raised exception (as it should)")
        
    print('\nTesting  examples of expand_re')
    pd = dict(digit=r'\d', integer=r'[=-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary {'digit': '\\d', 'integer': '[=-]?(\\d)(\\d)*'}
    
    pd = dict(integer       =r'[+-]?\d+',
              integer_range =r'#integer#(..#integer#)?',
              integer_list  =r'#integer_range#(?,#integer_range#)*',
              integer_set   =r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer'      : '[+-]?\\d+',
    #  'integer_range': '([+-]?\\d+)(..([+-]?\\d+))?',
    #  'integer_list' : '(([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*',   
    #  'integer_set'  : '{((([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*)?}'
    # }

    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'d': '(((correct)))',
    #  'c': '((correct))',
    #  'b': '(correct)',
    #  'a': 'correct',
    #  'g': '((((((correct))))))',
    #  'f': '(((((correct)))))',
    #  'e': '((((correct))))'
    # }
    print()
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
