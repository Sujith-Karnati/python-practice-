def twin_primes():
    primes = []
    for num in range(2,100):
        is_prime = True
        for i in range(2,num//2 + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    twin_primes_list = []
    for i in range(len(primes)-1):
        if primes[i+1] - primes[i] == 2:
            twin_primes_list.append((primes[i], primes[i+1]))   
            
    return twin_primes_list

print(twin_primes())

# method 2 
def twin_primes_v2():
    primes = []
    for num in range(2, 100):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    twin_primes_list = [(primes[i], primes[i+1]) for i in range(len(primes)-1) if primes[i+1] - primes[i] == 2]
    
    return twin_primes_list

print(twin_primes_v2()) 