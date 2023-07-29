


def fib(n,store={}):
    print(store)
    if(n in store):
        n = store[n]
        return n
    if(n<=2):
        return 1
    else:
        store[n] = fib(n-1,store)+fib(n-2,store)
        return store[n]
    
s = fib(50)

print(s)