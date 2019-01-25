def sieve(n):
    num = 2
    values = []
    for i in range (2, n+1):
         values.append(i)

    while num <= n and num*2 <= n:
        start = 2
        while (start < n):
            factor = num*start
            if (factor <= n) and (factor in values):
                    values.remove(factor)
            start+=1 

        num+=1

    return (values)
