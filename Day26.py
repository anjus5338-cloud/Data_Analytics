import numpy as np
import matplotlib.pyplot as plt

#scatter()
plt.scatter
#compare plot:
x = np.array([1,2,3])
y = np.array([4,5,6])
plt.scatter(x,y,color = "green")

x = np.array([9,8,7])
y = np.array([1,2,3])
plt.scatter(x,y,color = "red")
plt.show()

#color in array 
color = np.array(["blue","orange","purple"])
x = np.array([1,2,3])
y = np.array([4,5,6])
plt.scatter(x,y,c = color)

x = np.array([5,7,9])
y = np.array([0,2,1])
plt.scatter(x,y,c = color)

x = np.array([5,4,3])
y = np.array([3,5,9])
plt.scatter(x,y,c = color)
plt.show()

#size:
size = np.array([10,20,30])
color = np.array(["blue","orange","purple"])
x = np.array([1,2,3])
y = np.array([4,5,6])
plt.scatter(x,y,c = color,s = size)

x = np.array([5,7,9])
y = np.array([0,2,1])
plt.scatter(x,y,c = color,s = size)

x = np.array([5,4,3])
y = np.array([3,5,9])
plt.scatter(x,y,c = color,s = size)
plt.show()

#alpha:
size = np.array([10,20,30])
color = np.array(["blue","orange","purple"])
x = np.array([1,2,3])
y = np.array([4,5,6])
plt.scatter(x,y,c = color,s = size,alpha = 0.5)

x = np.array([5,7,9])
y = np.array([0,2,1])
plt.scatter(x,y,c = color,s = size,alpha = 0.7)

x = np.array([5,4,3])
y = np.array([3,5,9])
plt.scatter(x,y,c = color,s = size,alpha=0.9)
plt.show()

#bars:
x = np.array(["A","B","C","D"])
y = np.array([70,80,90,80])
plt.bar(x,y,color = "red",width = 0.9)
plt.show()

x = np.array(["A","B","C","D"])
y = np.array([70,80,90,80])
plt.barh(x,y,color = "green",height = 0.9)
plt.show()

#histogram:
x = np.random.normal(100,10,10)
plt.hist(x)
plt.show()

#pie
y = np.array([35,25,25,15])
plt.pie(y)
plt.show()

#label:
x = np.array([20,40,55,70])
mylabel = np.array(["Apple","Orange","Banana","Grapes"])
plt.pie(x,labels=mylabel)
plt.show()

#startangle:
x = np.array([20,40,55,70])
mylabel = np.array(["Apple","Orange","Banana","Grapes"])
plt.pie(x,labels=mylabel,startangle=90)
plt.show()

#explode:
x = np.array([20,40,55,70])
mylabel = np.array(["Apple","Orange","Banana","Grapes"])
explode = np.array([0.1,0,0,0])
plt.pie(x,labels=mylabel,explode=explode)
plt.show()

#shadow:
x = np.array([20,40,55,70])
mylabel = np.array(["Apple","Orange","Banana","Grapes"])
plt.pie(x,labels=mylabel,shadow = True)
plt.show()

#color:
x = np.array([20,40,55,70])
mylabel = np.array(["Apple","Orange","Banana","Grapes"])
explode = np.array([0.1,0,0,0])
color = np.array(["red","green","blue","orange"])
plt.pie(x,labels=mylabel,explode=explode,colors = color)
plt.show()








