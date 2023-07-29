#leet code 324

import re 

s = "3[a2[c]1[y]]" #  accaccacc

def helper(stack,mul,result=''):
    if mul == []:
        print(stack)
        return result
    curr = stack.pop()+result
    print("Curr = "+curr)
    next = stack.pop()
    if(next == "["):
        result += mul.pop()*str(curr)
        stack.append(result)
        print(stack,mul)
        helper(stack,mul)
    else:
        print("alp")
        stack.append(next+curr)
        helper(stack,mul,result)
    # print("result ="+curr)
    # print("Stack = "+str(stack))
    # if(mul == []):
    #     print(result)
    # else:
    #     helper(stack,mul,result)


def Solution(s):
    stack = []
    mul = []
    string = list(s)
    print(string)
    for i,x in enumerate(s):
        if("[" in x):
            if(string[i-1].isnumeric() == False):
                print(i)
                string.insert(i,'1')
    for x in string:
        if "]" not in x:
            if(x.isnumeric()):
                mul.append(int(x))
            else:
                stack.append(x)
    print(string)       
    ou = helper(stack,mul,result='')
    print(ou)
out = Solution(s)