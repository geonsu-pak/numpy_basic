import numpy as np

# list
data1 = [1, 2, 3]

# list to ndarray
arr1 = np.array(data1)
# np.array vs np.asarray
# -> np.asarray does not copy if the input is already an ndarray

# 2d
arr2 = np.array([[1., 2., 3.], [4., 5., 6.]])

# create arrays of 0's or 1's
np.zeros(10)
np.zeros((3,6))
np.ones(10)
np.ones((3,6))
# np.ones_like, np.zeros_like
# -> create a zeros or ones array of the same shape and dtype of input

# without initializing its values
np.empty((3,6))

# ([0,......,9])
np.arrange(10)
# convert to 2d
arr = np.arrange(32).reshape((8,4))

# convert to a different ndarray type
arr = np.array([1,2,3])
# -> print(arr.dtype) : dtype('int64')
floaat_arr = arr.astype(np.float64)
# dtype('float64')



