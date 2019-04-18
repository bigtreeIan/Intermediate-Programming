################################################################################ 
################################################################################ 
#
# Program        : Collatz
#
# Author         : Richard E. Pattis
#                  Computer Science Department
#                  University of California, Irvine
#                  Irvine, CA 92617-3435
#                  e-mail: pattis@ics.uci.edu
#
# Maintainer     : Author
#
#
# Description:
#
#   The Collatz conjecture states: Any positive number will be eventually
# be reduced to 1 by repeating the following process
#
#   o If a number is even, divide it by 2
#   o If a number is odd,  multiply it by 3 and add 1
#     (the number will now be even, so it will next be divided by 2)
#
#   This program prompts the user for a legal starting value and implements
# the Collatz process, displaying the sequence of values guenerated by the
# process. When the number is reduced to 1, the program reports the total
# number of cycles it took (how many times it applied the process).
#
#   This program uses the BigInteger class, which slows it down (compared
# to using int) but removes any limit on number of digits. BigInteger
# objects are constructed from Strings (representing numbers). There
# are no operators on these objects: we must use BigInteger methods to
# perform arithmetic (add, multiply, divide, remainder, comparisons
# (equals), etc. See the original Collatz program and the changes required
# here. Note that ZERO and ONE are static values supplied by the class.
#
#   This program also uses a Timer object to time the speed of each
# Collatz process. The user is given an option to see intermediate
# results.
#
# Known Bugs     : None
#
# Future Plans   : Ensure user enters a positive value initially
#
# Program History:
#   5/18/01: R. Pattis - Operational for 15-100
#   1/25/02: R. Pattis - Added Timer object for timing process
#   2/23/13: R. Pattis - Converted to Python using similar libraries
#
################################################################################ 
################################################################################ 



import prompt
from  stopwatch import Stopwatch


original_number = prompt.for_int('Enter a positive number', is_legal=(lambda x : x > 0))
is_debugging    = prompt.for_bool('Display intermediate results',True)
cycle_count     = 1
test_number     = original_number

timer = Stopwatch(running_now = True)

while True:
    if is_debugging:
        print('Cycle', cycle_count, ': test number is now', test_number)
    
    ####################
    if test_number == 1:
        break;
    ####################

    cycle_count += 1
    if test_number % 2 == 0:
        test_number = test_number // 2
    else:
        test_number = 3*test_number + 1

timer.stop()

print('\n\nFor test number =',original_number,'cycles to 1 =',cycle_count)
print('Process took', timer.read(), 'seconds')
