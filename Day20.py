import numpy as np
#Mathematical and statical operations:
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
#print minimum of row:
print(np.min(arr,axis = 1))
#print minimum of column:
print(np.min(arr,axis = 0))
#print sum of row:
print(np.sum(arr,axis =1))
#print sum odf column:
print(np.sum(arr,axis = 0))

#cumulative:
#1.cumsum
print(np.cumsum(arr))
#2.cumprod:
print(np.cumprod(arr))

#Rounding,floor and ceil:
x = np.array([1.2356,5.6789,6.7843])
#round
print(np.round(x,2))
#floor
print(np.floor(x))
#ceil
print(np.ceil(x))

#normalization:
#x-np.min(x)/np.max(x) - np.min(x)

#concatenate:
x = np.array([1,2,3])
y = np.array([4,5,6])
print(np.concatenate((x,y)))
#print by column:
print(np.concatenate((x,y),axis = 0))

#Q.
arr = np.array([[45,78,56],[67,82,90],[85,65,70],[34,55,60],[76,88,97]])
#maths average numbers:
new_arr = np.mean(arr,axis=0)
print(new_arr[0])

#student1 max number:
new_arr = np.max(arr,axis =1)
print(new_arr[0])

#student4 min number:
new_arr = np.min(arr,axis = 1)
print(new_arr[3])

#avg number per student:
new_arr = np.mean(arr,axis = 1)
print(new_arr)

#avg number per subject:
new_arr = np.mean(arr,axis=0)
print(new_arr)

