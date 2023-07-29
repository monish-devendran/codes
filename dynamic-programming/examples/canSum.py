
import time
def canSum(targetsum, numbers, memo = {}):
    if(targetsum in memo):
        return memo[targetsum]
    if(targetsum == 0):
        return True
    elif(targetsum < 0):
        return False
    elif(targetsum == 1):
        return False
    else:
        for i in numbers:
            remainder = targetsum-i
            out = canSum(remainder,numbers, memo)
            if(out == True):
                memo[remainder] = True
                return True
            else:
                return False

o = canSum(290,[17,1,4,])
print(o)