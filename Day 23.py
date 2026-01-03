import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("clean_data.csv")
print(df.to_string)

x = np.array([0,6])
y = np.array([0,25])
plt.plot(x,y)
plt.show()

#ploting without line
a = np.array([1,8])
b = np.array([3,10])
plt.plot(a,b,'o')
plt.show()

a = np.array([1,2,6,8])
b = np.array([3,8,9,10])
plt.plot(a,b,'o')
plt.show()

a = df['Age']
b = df['Sex']
a1 = np.array(a)
b1 = np.array(b)
plt.plot(a1,b1,'o')
plt.show()

x1 = df['Chest pain type']
x2 = df['BP']
arr1 = np.array(x1)
arr2 = np.array(x2)
plt.plot(arr1,arr2,'o')
plt.show()

y1 = np.array(df['Cholesterol'])
y2 = np.array(df['FBS over 120'])
plt.plot(y1,y2,'o')
plt.show()


a2 = np.array(df['EKG results'])
b2 = np.array(df['Max HR'])
plt.plot(a2,b2,'o')
plt.show()


e = np.array(df['Exercise angina'])
p = np.array(df['ST depression'])
plt.plot(e,p,'o')
plt.show()


e1 = np.array(df['ST depression'])
e2 = np.array(df['Slope of ST'])
plt.plot(e1,e2,'o')
plt.show()


f1 = np.array(df['Number of vessels fluro'])
f2 = np.array(df['Thallium'])
plt.plot(f1,f2,'o')
plt.show()