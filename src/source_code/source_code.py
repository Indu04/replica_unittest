'''
Created on Sep 4, 2017
test edit
@author: Indu
'''
import sys


 
 
def is_prime(number):
    """Return True if *number* is prime."""
    for element in range(number):
        if number % element == 0:
            return False
    return True



def fact(n):
    """
    Factorial function
    """
    if n == 0:
        return 1
    return n * fact(n -1)

def divTen(n):
    """
    Just divide 10 with given number
    """
    res = 10 / n
    return res


# def is_prime(number):
#     """Return True if *number* is prime."""
# #     if number < 0:
# #         return False
# #      
# #     if number in (0, 1):
# #         return False
#     
#     if number <=1 :
#         return False
#  
#        
#     for element in range(2, number):
#         if number % element == 0:
#             return False
#     return True

def main(n):
    print "main"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
        

        
#     if number <= 1:
#         return False
