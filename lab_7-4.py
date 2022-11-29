# author: JHR 11/18/22

# defining function 
def find_sum(num1, num2):
    '''Finds the value of the sum of 2 numbers'''
    num_sum = num1 + num2
    return num_sum

# test cases
print (find_sum(111,222) == 333)
print (find_sum(1,1) == 2)
print (find_sum(0,6000000) == 6000000)
print (find_sum(2,2) == 5)