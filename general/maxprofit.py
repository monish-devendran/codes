def MaxprofitSell(arr):
    profit = 0
    cost = 0
    start = arr[0]
    for i in range(1,len(arr)):
        cost = arr[i] - start
        profit = max(cost,profit)
        start = min(start,arr[i])

    return profit

p = MaxprofitSell([4,8,10,6])
print(p)