from goody import irange
import driver

def fact1(n):
    return 0

def fact2(n):
    if type(n) is not int:
        raise TypeError('factorial('+str(n)+') must be called with an int argument')
    if n < 0:
        raise ValueError('factorial('+str(n)+') not defined for negative values')
    answer = 1
    for i in irange(2,n):
        answer *= i
    return answer

if __name__ == '__main__':
    driver.driver()
