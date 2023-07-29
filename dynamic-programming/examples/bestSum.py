def bestSum(target_sum, numbers, memo={}):
    if(target_sum in memo): return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None
    for num in numbers:
        remain = target_sum - num
        reminder_combination = bestSum(remain, numbers, memo)

        if reminder_combination is not None:
            reminder_combination = reminder_combination.copy()+[num]
            if(shortest_combination is None or len(reminder_combination) < len(shortest_combination)):
                shortest_combination = reminder_combination
    memo[target_sum] = shortest_combination
    # print("--",memo)
    return shortest_combination

out = bestSum(8,[2,3,5])
print(out)