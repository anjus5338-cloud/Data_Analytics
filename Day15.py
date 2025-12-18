#Modules:
#1.json:
import json
data = {
    "name" : "Alice",
    "age" : 30,
    "isStudent" : False,
    "courses" : "data science"
    }
#dump: load data into file
with open("data.json",'w') as f:
    json.dump(data,f)
    
with open("data.json",'r') as f:
    context = f.read()
    print(context)
    
#dumps: json data convert in string
json_string = json.dumps(data)
with open("data.json",'w') as f:
    f.write(json_string)
    
with open("data.json",'r') as f:
    context = f.read()
    print(context)
    
#load: access data
with open("data.json",'r') as f:
    json.load(f)
    
#2.csv file
import csv
#writer
with open("data.csv","w") as f:
    writer = csv.writer(f)
    #header
    writer.writerow(data.keys())
    #values
    writer.writerow(data.values())
    
with open("data.csv",'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        

#DictWriter()
fieldnames = ["name", "age", "isStudent", "courses"]        
with open("data.csv",'w',newline="") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(data)
    
#DictReader():
with open("data.csv",'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        print(i)

    

    
       


