#Beginner   B  

#Intermediate  
import numpy as np

def main():
  np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
  x_train = np.array(
        [
            [25, 2, 50, 1, 500], 
            [39, 3, 10, 1, 1000], 
            [13, 2, 13, 1, 1000], 
            [82, 5, 20, 2, 120], 
            [130, 6, 10, 2, 600],
            [115, 6, 10, 1, 550 ]
        ]
    )   
    
  y_train = np.array([127900, 222100, 143750, 268000, 460700, 407000])

  # add the feature data for the two new cabins here. note: don't include the price data
  x_test = np.array([
        [36,3,15,1,850],
        [75,5,18,2,540]
    ])

  c = np.linalg.lstsq(x_train, y_train, rcond=-1)[0]

    # this will print the predicted prices for the six cabins in the training data
    # change this so that it predicts the prices of the two new cabins that are not
    # included in the training set

  print(x_test @ c)

main()

#Advanced
import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
  np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
  train_file = StringIO(train_string)
  test_file = StringIO(test_string)
    
  train_data = np.genfromtxt(train_file,dtype =None)
  test_data = np.genfromtxt(test_file,dtype =None)
    
  # Please write your code inside this function
  # read in the training data and separate it to x_train and y_train
  n = train_data.shape[1]
  x_train = train_data[:,0:n-1]
  y_train = train_data[:,n-1]

  # fit a linear regression model to the data and get the coefficients
  c = np.linalg.lstsq(x_train, y_train ,rcond=None)[0]

  # read in the test data and separate x_test from it
  x_test = test_data[:,0:n-1]

  # print out the linear regression coefficients
  print(c)

  # this will print out the predicted prics for the two new cabins in the test data set
  print(x_test @ c)


main()
