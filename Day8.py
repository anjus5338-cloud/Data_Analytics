#Function:
num1 = int(input("Enter a number"))
num2 = int(input("Enter second number"))
def add(a,b):
    print(a+b)

add(num1,num2)

#return:
def add(a,b):
    return a+b
result = add(10,6)
print(result)

#Default value:
def details(name="Raj",age = 0):
    print(name)
    print(age)
details()
details("anju")
details("anju","20")

#Lambda function:
add = lambda a,b : a+b
result = add(10,6)
print(result)

'''Q.def test(a,b)
       return a if a>b else b
       print(test(test(2,5),test(10,3)))'''
   
def test(a,b):
    if a>b:
        return a
    else:
        return b
result1 = test(2,5)
result2 = test(10,3)
result3 = test(result1,result2)
print(result1)
print(result2)
print(result3)


    