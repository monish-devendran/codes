

def countConstruct(target, wordBank, memo={}):

    count = 0
    if(target in memo): return memo[target]
    if(target == ''): return 1;

    for word in wordBank:
        if(target.startswith(word)):
            newTarget = target[len(word):]
            out = countConstruct(newTarget,wordBank)
            count +=out
    memo[target] = count
    return count

s = countConstruct('purple',['purp','p','ur','le','purpl'])
l= countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"])
print(s,l)