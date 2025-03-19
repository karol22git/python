import math

def czy_liczba_pierwsza(n: int) -> bool:
    for i in range(2, round(math.sqrt(n)) +1) :
        if n % i == 0:
            return False
    return True
