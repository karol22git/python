def add_numbers(a,b):
    return a + b

def multiply_numbers(a,b):
    return a*b

def substract_numbers(a,b):
    return a-b

def divide_numbers(a,b):
    return a/b

def main():
    while(True):
        command = input("Choose operation: \n 1. addition, \n 2. substraction,\n 3. division , \n 4. multiplication. \n")
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if command == "1":
            c = add_numbers(a,b)
         #   print(c)
        elif command == "2":
            c = substract_numbers(a,b)
          #  print(c)
        elif command == "3":
            c = divide_numbers(a,b)
           # print(c)
        elif command == "4":
            c = multiply_numbers(a,b)
           # print(c)
        else:
            break
        print("The result is: " + str(c))

if __name__ == "__main__":
   main()