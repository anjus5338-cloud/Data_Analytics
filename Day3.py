#String:
x = 'Hello'
y = "Hello"
z = '''hello word program'''


#for print the string
print(x)

#for checking  the type of variable value
print(type(x))

#for calculating the length of a string
print(len(x))

#for printing the first character of h string
print(x[0])



#Slicing in string:
x = "Hello world"
print(x[0:4])

#Modify string:
#1 .upper()
x = "ravi"
print(x.upper())

#2 .lower()
y = "RAVI"
print(y.lower())

#3 .strip()
z = "  Ravi  "
print(z.strip())

#4 .split():
x = "Hello"
y = x.split("e")
print(y)

#Questions related to modification of string:
#1. Convert strings first value in capital letter:
x = "hello"
y = x[0].upper()
x1 = x[1:5]
print(y + x1)

#2. Convert w in capital letter from the "helloworld" string:
x = "helloworld"
x1 = x[0:5]
y = x[5].upper()
y1 = x[6:10]
print(x1+y+y1)

#3. Take input from user name and age. Add 5 in user entered value for age.In name extra space have to be  erase and name have to be in correct form first letter will be capital or other letter will be small.
x = input("Enter user name")
y = int(input("Enter users age"))
print(y+5)
x1 = x.strip(" ")
x2 = x1[0].upper()
x3 = x1[1: ].lower()
print(x2+x3)

#4. Convert the string into uppercase:
text = "hello world"
print(text.upper())

#5. Covert the string into lowercase:
name = "PYTHON PROGRAMMING"
print(name.lower())

#6. Strip spaces and then split using comma:
data = "  apple,banana,grapes  "
data1 = data.strip("  ")
print(data1.split(","))

#7. Print "Python" using slicing:
msg = "PythonlsAwesome"
print(msg[0:6])

#8. Count how many times 'a' appears in the string:
word = "banana"
print(word.count("a"))

#9. Print "python" here:
sentence  = "I love python programming"
print(sentence[7:13])

#10. Convert the string into lower case using lower()
text2 = "HELLO"
print(text2.lower())

#11. Remove leading and trailing spaces:
info = "  welcome to python  "
print(info.strip("  "))

#12. Split the string by spaces into a list:
fruits = "apple orange mango"
print(fruits.split("  "))

#13. Print characters from index 4 to 9 using slicing:
course = "DataScience"
print(course[4:10])





