import math

prime_numbers = (2,3,5,7)
upperBound = 1000
def number_of_digits(n: int) -> int :
    counter = 0
    while n>0 :
        counter += 1
        n = n //10
    return counter

def is_prime(n: int) -> bool :
    for i in range(2,round(math.sqrt(n))) :
        if n % i ==0:
            return False
    return True

def is_number_of_digits_prime(n: int) -> bool:
    numberOfDigits = number_of_digits(n)
    if numberOfDigits in prime_numbers:
        return True
    else:
        return False

def is_sequence(n: int) -> bool :
    first_digit = n % 10
    n = n - first_digit
    n = n // 10
    if n == 0 :
        return True
    second_digit =  n %10
    if second_digit >= first_digit:
        return False
    step = second_digit - first_digit
    first_digit = second_digit
    n = n - first_digit
    n = n//10
    while n>0:
        second_digit = n %10
        if second_digit >= first_digit:
            return False
        if second_digit - first_digit != step:
            return False
        first_digit = second_digit
        n = n - first_digit
        n = n//10
    return True

def sum_of_digits(n: int) -> int:
    sum = 0
    while n>0 :
        sum += n%10
        n = n - (n%10)
        n = n//10
    return sum

def condition4(n: int) -> bool:
    return sum_of_digits(n) % number_of_digits(n) == 0


result = []



for i in range(1, upperBound) :
    if is_sequence(i) and is_number_of_digits_prime(i) and condition4(i) and is_prime(i) :
        result.append(i)

print(result)