#We need to install wikipedia package in python
import wikipedia
import numpy as np
import os
#print(wikipedia.summary("Python Programing Language"))
result = wikipedia.search("Neural Networks")
#print("Result search of 'Neural Networks':",result)
temp = wikipedia.summary(result[0])

#Partitioning into byte string, with n = 16*2
n = 16*2
split_string = [temp[i:i+n] for i in range(0,len(temp),n)]
#print(len(split_string[-1]))
#Since the last element might not be a multiple of n , we will drop it from consideration
final_split_string = split_string[:len(split_string)-1]
#print(len(final_split_string[-1]))
#temp = np.array(temp)
Array = np.array(final_split_string)



