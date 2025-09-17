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
arr5[arr5 % 2 == 1] = -1
print(arr5)
arr55 = np.array([0,1,2,3,4,5,6,7,8,9])
odd55 = arr55[1::2]
odd55[:] = -1
print(arr55)
arr555 = np.array([0,1,2,3,4,5,6,7,8,9])
arr555 = np.where(arr555 % 2 == 1, -1, arr555)
print(arr555)
##6
print("#6")
arr = np.arange(10)
result = arr.reshape(2,5)
print(result)
##7
print("#7")
# Input
arr = np.array([1,2,3,4,5,6,7,8,9,10])
# Enter your code here
mu = arr.mean()
med = np.median(arr)
sd = arr.std()
print(mu)
print(med)
print(sd)
##8
print("#8")
arr = np.array([1,2,3,4,5,6,7,8,9,10])
percentiles = [5, 95]
result = np.percentile(arr, percentiles)
print(result)
##9
print("#9")
arr = np.array([3, 4, 2, 1, 1, 1, 2, 3, 1, 3])
values, counts = np.unique(arr, return_counts=True)
index_of_max_elem = np.argmax(counts)
result = values[index_of_max_elem]
print(result)
##Intermediate

##1
print("#1")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 == 1] = -1
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
print(out)
##2
print("#2")
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
res = np.concatenate((a,b), axis = 0)
print(res)
#3
print("#3")
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
res = np.concatenate((a,b), axis = 1)
print(res)
#4
print("#4")
a = np.array([1,2,3])
out = np.arange(1,4)
print(out)
#5
print("#5")
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
res = np.intersect1d(a,b)
print(res)
#6
print("#6")
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
out = np.setdiff1d(a,b)
print(out)
