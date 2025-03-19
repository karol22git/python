import sys
n_str,a_str,q_str = input("Podaj numer elementu, wartość pierwszego elementu oraz wartość kroku.").split()
try:
    n = int(n_str)
    a = int(a_str)
    q = int(q_str)
except ValueError:
    print("error")
    sys.exit()
print("Wartość " + str(n) + "-tego wyraz ciągu o wyrazie początkowym " + str(a) + " i ilorazie " + str(q) +" wynosi: " + str(q**(n-1)*a))