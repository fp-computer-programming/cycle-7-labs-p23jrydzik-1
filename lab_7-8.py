# author: JHR 11/29/22

# my first function
def function_1 (a,b):
    c = a + b
    return c

# my second function
def function_2 (d,e,f):
    g = d + e + f
    return g

# my third function with the others nested in it
def function_3 (h):
    i = function_1(h,1) + function_2(2,3,4)
    return i

# test cases for function_3
print(function_3(1))
print(function_3(13728347183471))
print(function_3(-6))
print(function_3(0))