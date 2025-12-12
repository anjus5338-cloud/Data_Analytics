'''1.*
     * *
     * * *
     * * * *
     * * * * *'''
star = 1
while star<6:
    print("*" * star)
    star+=1

'''2.* * * * *
     * * * *
     * * *
     * *
     *'''
star = 5
while star>=1:
    print("*" * star)
    star-=1

#3.Write a program to print all even numbers from 1 to 50 (using for loop and if condition).
for x in range(1,51):
    if x % 2 == 0:
        print(x)

#4.Write a program that prints numbers from 1 to 20 but skips multiples of 3 using continue.
x = 1
while x<21:
    if x%3==0:
        x+=1
        continue
    print(x)
    x += 1

#5.Write a program to find the sum of numbers from 1 to 100 using a while loop.
num = 1
sum = 0
while num<101:
    sum = num+sum
    num+=1
print(sum)

#6.Write a program that takes a number from the user and checks if it is a prime number (use for loop, if-else, and boolean flag).
num = int(input("Enter a number: "))

is_prime = True   # assume number is prime

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")

#Q7.Write a program to print the multiplication table of any number (example: table of 7) using a for loop.
num = 7
for i in range(1,11):
    print(i*7)

#Q8.Write a program that prints numbers from 1 to 20 but stops the loop if the number becomes greater than 12 (use break).
for i in range(1,21):
    if i>12:
        break
    print(i)

#Q9.Write a program using a while loop that keeps asking the user for a password until the correct password is entered (use if-else + break).
correct_password = "abc123"

while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Wrong password. Try again.")
 
#Q10.Write a program to count the number of vowels in a string using a for loop and if condition.
string = '''In computer programming, a string is traditionally a sequence of characters, 
            either as a literal constant or as some kind of variable'''
count = 0
vowels = "aeiouAEIOU"
for ch in string:
    if ch in vowels:
        count+=1
print(count)
    

#Q11.Write a program to print numbers from 1 to 30 but only print numbers divisible by 5 OR 7 (use boolean operator OR).
for x in range(1,31):
    if x%5==0 or x%7==0:
        print(x) 

#Q12.Write a program to take 5 numbers from the user and find the largest number (use for loop and if condition).
largest = None

for i in range(5):
    num = int(input("Enter a number: "))
    
    if largest is None or num > largest:
        largest = num

print("The largest number is:", largest)
