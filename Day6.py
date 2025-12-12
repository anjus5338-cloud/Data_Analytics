#match
num = int(input("Enter a number"))
match num:
    case a if 0<=a<=24:
        print("lesser")
    case a if a==25:
        print("Winner")
    case a if 26<=a<=50:
        print("greater")

#Loop:
#1.while loop
start = 1
while(start<11):
    print(start)
    start+=1

#Q
start = 1
while(start<=10):
    print(start)
    start+=2

#Q
start = 1
sum = 0
while(start<=10):
    sum = start + sum
    start+=1
print(sum)

#Q
start = 1
sum = 0
while(start<=10):
    sum = sum + start
    start+=2
print(sum)

#Q
s = 1
while(s<=10):
    if(s%2 == 0):
      print(s)
    s+=1

#Q
sum = 0
s = 1
while(s<=10):
    if (s%2==0):
        print(s)
        sum+=5
    s+=1
print(sum)

#Q
text="hello world"
s = 0
while(s<(len(text))):
    print(text[s])
    s+=1

#Q
text = "Hello world"
count = 0
s = 0
while(s < len(text)):
    if text[s]=="l":
        count += 1
    s+=1
print(count)

#Q
text = input("Enter the string")
char = input("Enter a character")
i = 0
count = 0
while i<len(text):
    if text[i]==char:
        count+=1
    i+=1
print(count)







