def is_prime(n, prime):
    for i in range(len(prime)):
        if prime[i]**2 > n:
            return True
        elif n % prime[i] == 0:
            return False
    return True


def primes(n):
    count = 0
    prime = []
    for i in range(2, n+1):
        if is_prime(i, prime):
            count += 1
            prime.append(i)
    return count


print(primes(10))
