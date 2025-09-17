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
#7
print("#7")
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
mask = (a == b)
print(mask)
res = np.where(mask)[0]
print(res)
#8
print("#8")
a = np.array([2, 6, 1, 9, 10, 3, 27])
mask = (a >= 5) & (a <= 10)
indexes = np.where((a >= 5) & (a <= 10))
print(indexes)
print(a[indexes])
print(a[mask])
#9
print("#9")
def maxx(x, y):
    """Get the maximum of two items"""
    return x if x >= y else y


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
maxx_vect = np.vectorize(maxx)
print(maxx_vect(a,b))
#10
print("#10")
arr = np.array([[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]])
arr2 = np.array([[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]])
arr[:, 0:2] = arr[:, 1::-1]
#arr2[:, [0,1]] = arr2[:, [1,0]]
arr2 = arr2[:,[1,0,2]]
print(arr)
print(arr2)
#11
print("#11")
arr = np.array([[3, 4, 5],
                [0, 1, 2],
                [6, 7, 8]])
arr2 = np.array([[3, 4, 5],
                [0, 1, 2],
                [6, 7, 8]])
arr[0:2, :] = arr[1::-1, :]
arr2 = arr2[[1, 0, 2],:]
print(arr)
print(arr2)
#12
print("#12")
arr = np.array([[3, 4, 5],
                [0, 1, 2],
                [6, 7, 8]])
arr[::,:] = arr[::-1, :]
print(arr)
#13
print("#13")
arr = np.array([[3, 4, 5],
                [0, 1, 2],
                [6, 7, 8]])
arr2 = np.array([[3, 4, 5],
                [0, 1, 2],
                [6, 7, 8]])
out = arr2[:, ::-1]
arr[:, ::] = arr[:, ::-1]
print(arr)
print(out)
#14
print("#14")
arr = np.random.uniform(5, 10, size = (5,3))
arr2 = np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3))
print(arr)
print(arr2)
#15
print("#15")
arr = np.array([[1,2,3,4,5],
                [1,2,3,4,5],
                [1,2,3,4,5],
                [1,2,3,4,5]])
extract_column_index = 4
column = arr[:, extract_column_index]
print(column)
#16
print("#16")
arr = np.array([(1,2,3,4,5),
                (1,2,3,4,5),
                (1,2,3,4,5),
                (1,2,3,4,5)])
extract_column_index = 4
res = arr[:, extract_column_index]
res2 = np.array([row[extract_column_index] for row in arr])
print(res)
print(res2)
#17
print("#17")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
min = arr.min()
max = arr.max()
arr_norm = (arr - min) / (max - min)
print(arr_norm)
#18
print("#18")
matr = np.array([[1.,2.,3.],
                 [1.,2.,3.],
                 [1.,2.,3.]])

first_indexes = np.random.randint(low = 0, high = 3, size = 2)
second_indexes = np.random.randint(low = 0, high = 3, size = 2)
matr[first_indexes, second_indexes] = np.nan
print(matr)
#19

