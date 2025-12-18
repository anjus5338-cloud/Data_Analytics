#file handling:
#open and read:
file = open("demo.txt","r")
content = file.read()
file.close()
print(content)

#readline
with open("demo.txt",'r') as f:
    content = f.readline()
    print(content)
    
#readlines
with open("demo.txt",'r') as f:
    content = f.readline()
    print(content)
    
#write:
with open("demo.txt","a") as f:
    f.write("i am student of mca")
print("successfully created")
    
lines_to_write = [
    "This is first line\n",
    "This is second line\n",
    "This is third line\n"
]
with open("demo.txt",'w') as f:
    f.writelines(lines_to_write)
print("successfully created")
  

#create:
try:
    with open("temo.txt","x") as f:
       f.write("i am anju shekhawat")
    print("file created successfully")

except FileExistsError:
    print("error")
    
    
    
    


