import numpy as np

##2
print("#2")
a2 = np.arange(10)
b2 = np.array([0,1,2,3,4,5,6,7,8,9])
c2 = np.linspace(0,9,10)
d2 = np.array(range(10))
print(a2)
print(b2)
print(c2)
print(d2)
##3
print("#3")
a3 = np.array([[True, True, True], [True, True, True], [True, True, True]])
b3 = np.ones(9, dtype=bool)
b3 = b3.reshape(3,3)
c3 = np.full((3,3), True, dtype=bool)
print(a3)
print(b3)
print(c3)
##4
print("#4")
arr4 = np.array([0,1,2,3,4,5,6,7,8,9])
res = arr4[arr4 % 2 == 1]
res2 = arr4[1::2]
res3 = np.where(arr4 % 2 == 1)
print(res)
print(res2)
print(res3)
##5
print("#5")
arr5 = np.array([0,1,2,3,4,5,6,7,8,9])
odd = arr5[1::2]
odd[:] = -1
print(arr5)
arr55 = np.array([0,1,2,3,4,5,6,7,8,9])
odd55 = arr55[1::2]
odd55[:] = -1
print(arr55)
arr555 = np.array([0,1,2,3,4,5,6,7,8,9])
arr555 = np.where(arr555 % 2 == 1, -1, arr555)
print(arr555)
