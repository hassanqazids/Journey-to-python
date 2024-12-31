import numpy as np
# arr = np.array((1,2))# tuple (1,2)
# arr = np.array(42)# number
# arr = np.array([[1,2,3],[5,6,7],[8,9,0]]) # 2d array
#arr = np.array( [ [ [1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3d arr
#print(arr)

#Higher Dimensional Arrays
# arr = np.array([[1,2,3],[5,6,7],[5,6,7],[5,6,7],[5,6,7]], ndmin=5)

#arr = np.array([1,2]) #list [1,2]
#print(arr[0])
# print('number of dimensions :', arr.ndim)

#array
# arr = numpy.zeros((2, 3)) # values , 0
# arrr = numpy.ones((3, 3)) # values , 1

# print(arrr)

# arr = numpy.random.rand(3, 2) # 3x2
# arrr = numpy.random.randint(1, 10, (2, 2)) # 2x2
# print(arrr)

# 4 Mathematical Operations:
# arr = np.array([66,6,8,9])
# print(np.mean(arr))
# print(np.sqrt(arr))
# print(np.sum(arr))

# 5 Reshaping Arrays:
#
# array = np.array([1,2,3,4,5,6,7,8])
# #reshaped = array.reshape(3, 3)
# newarr = array.reshape(2, 2, -3)
# print(newarr)