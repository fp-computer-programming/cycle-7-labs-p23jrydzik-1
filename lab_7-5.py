# author: JHR 11/18/22

# lab 6-5
def lab_65(l1):
    sortaroonie = sorted (l1)
    if len(l1) <2:
        return ("error: list does not meet specifications")
    elif sortaroonie [0] == sortaroonie[-1]:
        return ("error: list does not meet specifications")
    else:
        return ("high: " + str(sortaroonie[-1]))
        return ("low: " + str(sortaroonie[0]))

# 6-5 test cases
print (lab_65([1]) == "error: list does not meet specifications" )
print (lab_65([6,6]) == "error: list does not meet specifications" )
print (lab_65([1,2,3]) == "high: 3")
print (lab_65([1,2,3]) == "error: list does not meet specifications" )

