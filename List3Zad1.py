import sys

user_input_str = input("Enter a number:")
try:
    user_input = int(user_input_str)
except ValueError:
    print("error")
    sys.exit()

#sposób pierwszy
sum1 = int(user_input*(user_input+1)/2)

#sposób drugi
sum2 = 0
for i in range(1,user_input +1) :
    sum2 +=i
print("Suma obliczona wzorem jawnym: " + str(sum1))
print("Suma obliczona symulacją: " + str(sum2))

#Metoda pierwsza jest szybsza i zużywa mniej pamięci
#Janwy wzór na pewno zwraca poprawne wyniki, bo istnieje na to formalny dowód
#Zalety jawnego wzoru to szybkość i pewność. Deklasuje on podejście iteracyjne.
# Np dla n = 10^((10^10^10)^10000^1000) możemy obliczyć wynik nawet na kartce. 
#Podejscie iteracyjne nie da nam odpwoiedzi