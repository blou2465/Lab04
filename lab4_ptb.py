
#created Mon Feb 27 7:40 2023
#Ileana Lopez
#CSE5408 LAB 4
#part b: write a program containing a function to 
# check if user imputted number is prime
number = int(input("Enter any number: "))

# prime number is greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1 its not prime
else:
    print(number, "is not a prime number")