def get_primes(N):
    nums = list(range(N+1))
    prime = 2
    while(prime <=N ):
        if nums[prime] == None:
            prime += 1
            continue
        n = prime*2
        while (n <= N):
            nums[n]=None
            n = n + prime
        prime += 1
    primes = []
    for num in nums:
        if num == None:
            continue
        else:
            primes.append(num)
    return (primes)

def get_koreny (a,b,c):
    """
    reší kvadratickou rovnici
    :return: koreny rovnice
    """
    import math
    D = b**2 - 4*a*c
    if D == 0:
       x=-b/2*a
       return (1,[x,x])
    if D>0:
        x1 = (-b + math.sqrt(D))/2*a
        x2 = (-b - math.sqrt(D))/2*a
        return (2,[x1,x2])
    else:
        print ('tato rovnice nema reseni v realnych cislech')
        return (0,[])
print(get_koreny (1,3,1))

#print(get_primes(1000))


