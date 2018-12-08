# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


# Series 
# pd.Series(self, data = None ,index = None ,dtype = None , name = None, copy =false)

x = pd.Series([1,2,3,4,5])

x+ 100

(x ** 2)+ 100

x> 2


# any and all

larger_than_2 = x > 2

larger_than_2.any() # if single true returns

larger_than_2.all() # Must be all of them true for true return


# apply 
def f(x):
    if x % 2 == 0:
        return x ** 2
    else:
        return x ** 3
    
    
x.apply(f)

# Converting Types 

x.astype(np.float64)


# Copy

x
 
y = x
y[0] = 100

x = pd.Series([1,2,3,4,5])

y = x.copy()

# Dataframes
# pd.DataFrame(self,data =None, index= None, columns =None,dtype = None, copy = false)


data = [1,2,3,4,5,6,7,8,9]

df = pd.DataFrame(data,columns = ["x"])

df

# one column as a series

dataSeries = df["x"]

# Adding more columns

df["x_plus_2"] = df["x"] + 2
df

df["x_square"] = df["x"] ** 2

df["x_factorial"] = df["x"].apply(np.math.factorial)
df

df["is_even"] = df["x"]% 2
df


# deleting-dropping 
df = df.drop("is_even",1)
df

# selecting multiple coumns

df[["x", "x_plus_2"]]
df.describe()


#  read data from csv file   
#  dataset= pd.read_csv('matches.csv') 
















