import numpy as np
#Stacking aaray:
#1. vstack()
a = np.array([1,2,3])
b = np.array([4,5,6])
result = np.vstack((a,b))
print(result)

#2. hstack()
a = np.array([[1],[2],[3]])
b = np.array([[4],[5],[6]])
result = np.hstack((a,b))
print(result)

#stack():
a = np.array([1,2,3])
b = np.array([4,5,6])
result = np.stack((a,b), axis = 0)
result1 = np.stack((a,b), axis = 1)
print(result)
print(result1)

#spliting array:
arr = np.array([1,2,3,4,5,6])
result = np.split(arr,2)
print(result)

#append, insert:
arr = np.array([1,2,3])
result = np.append(a,4)
print(result)
result1 =np.append(a,[4,5])
print(result1)

arr = np.array([10,20,30,50])
result = np.insert(arr,2,40)
print(result)

#delete:
arr = np.array([10,20,30,40])
result = np.delete(arr,2)
print(result)

#Broadcasting and advance topics:
arr = np.array([1,2,3])
arr_1 = 5
print(arr+arr_1)

#2D add 1D
a = np.array([[1,2,3],[4,5,6]])
b = np.array([10,20,30])
print(a+b)

#np.any()
arr = np.array([10,20,0,10])
result = np.any(arr)
print(result)

#np.all()
result_1 = np.all(arr)
print(result_1)

#clip:
arr = np.array([10,20,30,40,50,60])
result = np.clip(arr,30,50)
print(result)

#sort():
arr = np.array([[10,90,30],[40,88,60]])
result = np.sort(arr,axis = 1)
print(result)
result_1 = np.sort(arr,axis = 0)
print(result_1)




