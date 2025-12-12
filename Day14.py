#file handling:
#open:
file = open("demo.txt","r")
content = file.read()
file.close()
print(content)

#write:
file = open("demo.txt","w")
file.write("i am student of mca")
file.close()

#create:
try:
    with open("temo.txt","x") as f:
       f.write("i am anju shekhawat")
    print("file created successfully")

except FileExistsError:
    print("error")
    
    
    
    


