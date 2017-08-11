def primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)/(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def primes1(n):
    sieve = [True] * int((n/2))
    for i in range(3,int(n**0.5)+1,2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int(((n-i*i-1)/(2*i)+1))
    return [2] + [2*i+1 for i in range(1,int(n/2)) if sieve[i]]
limit = 2000000000
#listOfPrimes = primes(limit)
listOfPrimes = primes1(limit)
print("There are " + str(len(listOfPrimes)) + " primes from 0 to " + str(limit))
#216816 to 3 million
