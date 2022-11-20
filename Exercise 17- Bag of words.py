#Beginner   the 3rd and the 4th  

#Intermediate  
# this data here is the bag of words representation of This Little Piggy
data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
    # fix this function so that it returns 
    # the sum of differences between the occurrences
    # of each word in row1 and row2.
    # you can assume that row1 and row2 are lists with equal length, containing numeric values.
  total = 0
  for i in range(len(row1)):
    total = total + abs(row1[i] - row2[i])
  return total

def all_pairs(data):
  # this calls the distance function for all the two-row combinations in the data
  # you do not need to change this
  dist = [[distance(sent1, sent2) for sent1 in data] for sent2 in data]
  print(dist)

all_pairs(data)

#Advanced

import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
  total = 0
  for i in range(len(row1)):
    total = total + abs(row1[i] - row2[i])
    # fix this function so that it returns 
    # the sum of differences between the occurrences
    # of each word in row1 and row2.
    # you can assume that row1 and row2 are lists with equal length, containing numeric values.
  return total

def find_nearest_pair(data):
  N = len(data)
  dist = np.empty((N, N), dtype=np.float64)
  dist = np.array([[distance(sent1, sent2) for sent1 in data] for sent2 in data])
  for i in range(N):
    dist[i][i] = 1000000000000   # assign the value np.inf (the maximum possible floating point value)
  nearest_index = np.unravel_index(np.argmin(dist), dist.shape)
  print(nearest_index)

find_nearest_pair(data)
