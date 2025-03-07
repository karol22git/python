import math

def is_prime(n: int) -> bool :
    for i in range(2,round(math.sqrt(n))) :
        if n % i ==0:
            return False
    return True


def find_unique_prime_factors(n :int) -> list :
    primes = []
    for i in range(2,n//2 +1) :
        if n % i == 0 and is_prime(i) :
            primes.append(i)
            while n%i == 0 :
                n = n//i
    return primes

def get_divisors(n: int) -> list :
    divisors = []
    for i in range(2, n//2 +1) :
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_perfect(n: int, lst: list) -> bool :
    lst = get_divisors(n)
    sum = 0
    for i in lst :
        sum += i
    return sum == n

def sum_of_digits(n: int) -> int:
    sum = 0
    while n>0 :
        sum += n%10
        n = n - (n%10)
        n = n//10
    return sum

def tajemnicza_funkcja(n: int) -> int :
    divisors = []
    uniquePrimeFactors = find_unique_prime_factors(n)
    if is_prime(n) :
        return 2*n +1
    elif len(uniquePrimeFactors) == 1:
        return n + uniquePrimeFactors[0]
    elif is_perfect(n,divisors) :
        return sum_of_digits(n)*divisors[-1]
    else :
        result = 1
        for i in uniquePrimeFactors:
            result *= i
        return result

    