def howSum(targetSum, numbers, memo = {}):
    if(targetSum in memo):
        return memo[targetSum]
    if(targetSum == 0):
        return []
    elif(targetSum < 0):
        return None
    else:
        for i in numbers:
            remainder = targetSum - i
            out = howSum(remainder,numbers,memo)
            if(out != None):
               memo[remainder] = i
               out.append(i)
               return out
s = howSum(8,[2,3])
print(s)