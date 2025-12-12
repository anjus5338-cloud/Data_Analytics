#Modules:
#json:
import json
data = {
    "name" : "Alice",
    "age" : 30,
    "isStudent" : False,
    "courses" : "data science"
    }

y = json.loads(data)
print(y["age"])