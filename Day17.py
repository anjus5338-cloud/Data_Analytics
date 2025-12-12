#array in numpy:
import numpy as np
x = np.array([1,2,3,4,5,6])
y = np.array([[1,2,3],[4,5,6]])

#build in functions of numpy array:
#1.np.zeros([row,col])
zeros_array = np.zeros([2,2])
print(zeros_array)

#2.np.ones([row,col])
ones_array = np.ones([3,2])
print(ones_array)

#3.np.full([row,col],value)
full_array = np.full([2,2],7)
print(full_array)

#4.np.eye()
eye_array = np.eye(3)
print(eye_array)

#5.np.arrange(start,stop,step):
arange_array = np.arange(10,20,2)
print(arange_array)

#6.np.linspace(start,stop,num)
linspace_array = np.linspace(10,20,10)
print(linspace_array)

#7.np.random.rand(m,n)
random_array = np.random.rand(3)
print(random_array)

#8.np.random.randint(start,stop,(x,y))
array = np.random.randint(10,50,[3,3])
print(array)

#Attributes:
#1.arr.shape
array = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
print(array.shape)

#2.arr.size
array = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
print(array.size)

#3.arr.ndim
array = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
print(array.ndim)

#4.arr.dtype
array = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
print(array.dtype)

#change datatype:
n = np.array([1,2,3], dtype=float)
print(n)
print(n+5)

#Q.create an array of number 1 to 20 using np.arange()
#1.shape
#2.size
#3.datatype

arr = np.arange(1,20)
print(arr)
print(arr.shape)
print(arr.size)
print(arr.dtype)

#Q.create 3*3 random number 10 to 50:
arr = np.random.randint(10,50,(3,3))
print(arr)
print(np.min(arr)) 
print(np.max(arr)) 
print(np.mean(arr))
    





