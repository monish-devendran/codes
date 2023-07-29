def gridTraverese(r,c, routes = {}):
    path = str(r)+'x'+str(c)

    if(path in routes):
        return routes[path]
    if(r == 0  or c == 0):
        return 0
    elif(r == 1 and c == 1):
        return 1
    else:
        routes[path] = gridTraverese(r-1,c,routes) + gridTraverese(r,c-1,routes)
        return routes[path]

o= gridTraverese(20,30)
print(o)