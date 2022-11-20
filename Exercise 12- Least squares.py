#Beginner   C  

#Intermediate  
import numpy as np

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200 , -50, 5000, 100])    # coefficient values
 
def squared_error(X, y, c):
  sse = 0.0
  for xi, yi in zip(X, y):
        # add your code here: calculate the predicted price,
        # subtract it from the actual price yi, 
        # square the difference using (yi - prediction)**2, 
        # and add up all the differences in variable sse
    sse = sse + ((xi @ c) - yi)**2
  print(sse)

squared_error(X, y, c)

#Advanced
import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
  smallest_error = np.Inf
  best_index = -1
  new_y = []
  for coeff in c:
    new_y.append(X @ coeff)
  error = []
  for i in range(len(new_y)):
    k = 0.0
    for m,n in zip(y,new_y[i]):
      k = k + (m-n)**2
    error.append(k)
  best_index = error.index(min(error))
         # edit here: calculate the sum of squared error with coefficient set coeff and
         # keep track of the one yielding the smallest squared error
  print("the best set is set %d" % best_index)


find_best(X, y, c)
