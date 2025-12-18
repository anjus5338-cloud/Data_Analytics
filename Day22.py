#pandas:
import pandas as pd
import numpy as np
arr = np.array([1,7,2])

#Series:
arr_1 = pd.Series(arr)
#print(arr_1)

df = pd.read_csv("Exam_Score_Prediction.csv")
print(df.to_string())

arr= np.array(df)
print(arr)

#Labels:
a = np.array([1,7,2])
a1 = pd.Series(a)
print(a1[0])

#create lables:
a = np.array([1,7,2])
data = pd.Series(a,index = ("x","y","z"))
print(data["y"])

x = {"a":1,
     "b":2,
     "c":4}
data = pd.Series(x)
print(data)

#dataframes:
x = pd.DataFrame(df)
print(x)

x1 = pd.DataFrame(df)
print(x.loc[0])
print(df.head())
print(df.tail())








