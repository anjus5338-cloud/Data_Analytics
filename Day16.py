#numpy:
#numerical python

#1.normal:
x=[1,2,3,4,5]
for i in x:
    print(i*2)
    

#2.by numpy:    
import numpy as np
x = np.array([1,2,3,4,5])
print(x*2)

#example:
import time
lst = list(range(1_000_000))
start = time.time()
[x*2 for x in lst]
print(time.time()-start)

import time
import numpy as np
arr = np.arange(1_000_000)
start = time.time()
arr*2
print(time.time()-start)
    