#conditional statements:
#if
age = 45
if age>=18:
    print("you can drive")

#if else
age = 45
if age>=18:
    print("you can drive")
else:
    print("you can't drive")

#if elif else
day = 5
if day==1:
    print("Sunday")
elif day==2:
    print("Monday")
elif day==3:
    print("Tuesday")
elif day==4:
    print("Wednesday")
elif day==5:
    print("Thursday")
elif day==6:
    print("Friday")
elif day==7:
    print("Saturday")
else:
    print("please enter number between 1 to 7")

#Conditional statements with Logical operators:
a = 18
b = "Hema"
if a>=18 or b == 'H':
    print("Yes")
else:
    print("No")

#Q1.
num = 25
if num == 25:
    print("Winner")
else:
    print("looser")

#Q2.
num = 20
if num>=0 and num<=24:
    print("lesser")
elif num == 25:
    print("Winner")
elif num>=26 and num<=50:
    print("Greater")
else:
    print("Enter a valid number between 0 to 50")

#Q3.
num = 21
if num>=0 and num<=20:
    print("lesser")
if num>=21 and num<=24:
    print("near to win(lesser)")
elif num == 25:
    print("Winner")
elif num>=26 and num<=30:
    print("near to win(Greater)")
elif num>=31 and num<=50:
    print("Greater")
else:
    print("Enter a valid number between 0 to 50")

#Match:
#Q1.
day = 2
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Enter a valid number")

#Q2.
month = int(input("Enter a number"))
match month:
    case 1:
        print("January")
    case 2:
        print("Februray")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("december")
    case _:
        print("Enter a number between 1 to 12")










