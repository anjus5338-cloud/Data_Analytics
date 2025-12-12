import numpy as np
#indexing in 1D array:
x = np.array([1,2,3,4,5,6])
print(x[0])

#indexing in 2D array:
x = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
'''[[1,2,3],
    [4,5,6],
    [7,8,9]]'''  
    
print(x[0,0])
print(x[1,2])
print(x[0])
print(x[:,1]) 

#slicing in 1D array:
arr = np.array([1,2,3,4,5,6,7])
print(arr)
print(arr[1:4])
print(arr[:4])
print(arr[3:])
print(arr[::2]) 

#slicing in 2D array:
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) 
'''[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]'''  
    
print(arr)
print(arr[:2,:])   
print(arr[:,:2])
print(arr[0:2,1:3])   

#Advance slicing in 1D array: 
#to access more than one value by indexing:
arr = np.array([1,2,3,4,5,6])
indices = [0,2,3,5]
print(arr[indices])

#Advance slicing in 2D array:
arr = np.array([[11,12,13],[21,22,23],[31,32,33]])
print(arr)
print(arr[0:2,1:2])

#Boolean indexing:
x = np.array([10,20,30,40,50])
print(x>30)
print(x[x>30])

#Operarions on array:
arr = np.array([5,10,15,20,25,30])
print(arr%2==0)
print(arr[arr%2==0])
print((arr<25) & (arr>10))
print(arr[(arr<25) & (arr>10)])

#replace value with condition:
arr = np.array([10,40,20,5,60])
print(arr<20)
print(arr[arr<20])
arr[arr<20] = 0
print(arr)

#not operator:
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[~((arr<7)&(arr>3))])

#conditional relacement:
arr = np.array([35,45,66,43,12,56,2])
x = np.where(arr<36,"fail","pass")
print(x)

#Q1. Create an array 10 to 50 and print only even number from the given range and also print number which is greater than 30 and also replace small value from 20 into 0.
arr = np.arange(10,51)
print(arr)
#print all even number
print(arr[arr%2 == 0])
#print number greater then 30
print(arr[arr>30])
#replace number smaller than 20 into 0
arr[arr<20] = 0
print(arr)

#Q2. Create an 2D array 1 to 12 range which is in 3*4 formate.Perform opertion to print 2nd row,3rd row,2row and 3rd column.Extract value smaller than 6.
arr = np.arange(1,13)
#convert array in 3*4
new_arr = arr.reshape(3,4)
print(new_arr)
#print 2nd row
print(new_arr[1,:])
#print 3rd row
print(new_arr[2,:])
#print first 2 row and 3 col
print(new_arr[:2,:3])
#extract value smaller than 6
print(new_arr[new_arr<6])

#Q3. Given array = [25,60,45,80,35,90,55]. Print student who are pass[array>=40],replace fail marks with 40and find average of new array created after replacing the value.
array = np.array([25,60,45,80,35,90,55])
#print student who pass(array>=40)
x = np.where(array>=40,"Pass","Fail")
print(x)
#replace fail marks with 40
array[array<40] = 40
print(array)
#find average of new array
sum = 0
len = 0
for i in array:
    sum = sum+i
    len +=1
print(sum/len)

#Q4. Create an 2D array 1 to 100 range with 10*10 formate. Extract only even number and extract all numbers in 2nd and 4th row.Replace value<50 into 0.
arr = np.arange(1,101)
#convert array in 10*10
new_arr = arr.reshape(10,10)
print(new_arr)
#extract only even number:
print(new_arr[new_arr%2==0])
#extract all number of 2nd row and 4th row
print(new_arr[[1,3], : ])  
#replace values which are smaller then 50 into 0
new_arr[new_arr<50] = 0
print(new_arr)



                            


