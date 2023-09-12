

# s = "abcdef"
# c = "ab"

# print(s.startswith(c))


def canConstruct(target, stringArr, memo = {}):
    if(target in memo): return memo[target]
    if(target  == "" ): return True
    else:
        for string in stringArr:
            if(target.startswith(string)):
                newtarget = target[len(string):]
                out = canConstruct(newtarget,stringArr,memo)
                if(out == True):
                    memo[target] = True
                    return True
    memo[target] = False
    return False

#canConstruct("abcdef",["ab","abc","cd","def","abcd"])
s=canConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"])
print(s)