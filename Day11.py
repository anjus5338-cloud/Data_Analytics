#🔹 Q1. Unique Cities Finder
cities = ["Delhi", "Mumbai", "Pune", "Delhi", "Pune", "Jaipur", "Mumbai"]

# Task:
# 1. List se unique cities ka set banao
a = set(cities)
print(a)
# 2. Total unique cities count print karo
print(len(a))

#🔹 Q2. Remove Duplicates from List Using Set
nums = [1, 2, 3, 2, 4, 1, 5, 3, 6, 5]

# Task:
# 1. Set use karke duplicates remove karo
x = set(nums)
print(x)
# 2. Result ko wapas list me convert karke print karo
y = list(x)
print(y)

#🔹 Q3. Count Word Frequency (Dictionary)
text = "apple mango apple orange mango apple"

# Task:
# 1. Ek dictionary banao jisme:
#    key = word, value = word count
# 2. Output: {'apple': 3, 'mango': 2, 'orange': 1}

text1 = text.split(" ")
print(text1)
dict = {}
for i in text1:
    if i in dict:
        dict[i]+=1
    else:
        dict[i] = 1
print(dict)

#🔹 Q4. Student Marks Dictionary
marks = {
    "Ajay": 85,
    "Rohit": 92,
    "Simran": 78,
    "Neha": 90
}

# Task:
# 1. Sab students ke names print karo
for key in marks.keys():
    print(key)
# 2. Average marks print karo
sum = 0
for value in marks.values():
    sum+=value
average = sum/len(marks)
print(average)
# 3. Highest marks laane wale student ka naam print karo
highest_marks = 0
topper = ""
for name, marks_value in marks.items():
    if marks_value > highest_marks:
        highest_marks = marks_value
        topper = name

print(topper, highest_marks)

#🔹 Q5. Price Updater
prices = {
    "pen": 10,
    "pencil": 5,
    "notebook": 50
}

# Task:
# 1. Sab items ki price 10% badhao
prices = {
    "pen": 10,
    "pencil": 5,
    "notebook": 50
}

new_prices = {}

for item, price in prices.items():
    new_prices[item] = price * 1.10   # 10% increase

print(new_prices)
# 2. Nayi dictionary print karo (Example: pen -> 11, pencil -> 5.5)
print(new_prices)



    




