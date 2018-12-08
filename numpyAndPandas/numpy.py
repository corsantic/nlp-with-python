# -*- coding: utf-8 -*-

import numpy as np

# arange()
#np.arange([start,] stop[, step,],dtype=None)
np.arange(10)

np.arange(1,10)

np.arange(1,10,2)

np.arange(1,10,0.5)

np.arange(1,10,dtype = 'float64')


arr = np.arange(1,10)

arr.ndim # dimension of array

arr.shape

arr.size
arr.dtype
arr.itemsize

#Memory Usage

arr.itemsize * arr.size

# Important functions in numpy
# List to array
np.asarray([1,2,3,4,5])

list2d = [[1,2,3],[4,5,6]]
arr2d = np.asarray(list2d)

# Generate zeros 
# zeros(shape, dtype = float ,order = 'C')

listzeros = np.zeros((3,4),dtype='int32')

# Linspace
#np.linspace(start,stop,num= 50 ,endpoint = True, retstep = False)

np.linspace(1,4,num=4)
np.linspace(1,4,num=8)
np.linspace(1,4,num=8, endpoint=False)


# Random generation
np.random.random((3,5))

# Max, min, mean, median, std etc
rarr = np.random.random((3,4))

np.max(rarr,axis= 0)
np.max(rarr,axis=1)

np.median(rarr,axis=0)
np.median(rarr,axis=1)

 # Reshaping
 # np.reshape(a,newshape, order = 'C')

new_rarr = np.reshape(rarr, (12,))
new_rarr = np.reshape(rarr, (4,3))


# Slicing

rarr = np.random.random((4,5))

rarr[:,:]

rarr[1:3,:]

rarr[:,1:]














