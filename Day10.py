#Set:
set = {"Apple","Mango","Orange"}
print(type(set))
#unordered
#Unchangable
#unique values
print(len(set))
set.add(4)
print(set)
set.remove("Apple")
print(set)
set.pop()
print(set)

#dict:
x = {
    "brand":"vivo",
    "year" : "2"   
}
print(len(x))
a =dict(name = "ravi", age = 17)
print(a)
#Ordered
#Changable
print(x["brand"])
#copy:
data = x.copy()
print(data)

for key in x.keys():
    print(key)
    
for value in x.values():
    print(value)
    
for keys, values in x.items():
    print(keys,values)
    


