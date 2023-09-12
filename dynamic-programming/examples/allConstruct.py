def allConstruct(target, wordBank):
    if target == '': return [[]]

    combinations = []

    for word in wordBank:
        if target.startswith(word):
            newTarget = target[len(word):]
            suffixCombinations = allConstruct(newTarget, wordBank)
            if(target != None):
                print(word)
                for combination in suffixCombinations:
               
                    combinations.append(combination+[word])


    return combinations
    #         for combination in suffixCombinations:
    #             combinations.append([word] + combination)

    # return combinations

s = allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])
print(s)