#Beginner   C  

#Intermediate  
import numpy as np


def main():
  np.set_printoptions(precision=1)

  x = np.array(
        [
            [25, 2, 50, 1, 500], 
            [39, 3, 10, 1, 1000], 
            [13, 2, 13, 1, 1000], 
            [82, 5, 20, 2, 120], 
            [130, 6, 10, 2, 600]
        ]
    )   
  x6 = np.array([[115,6,10,1,550]])
  x = np.concatenate((x,x6),axis = 0)
  y = np.array([127900, 222100, 143750, 268000, 460700])
  y = np.concatenate((y,[407000]),axis = 0)
  c = np.linalg.lstsq(x, y)[0]
  print(c)

  print(x @ c)

main()

#Advanced
import numpy as np
from io import StringIO

input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''
np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
 
def fit_model(input_file):
  # Please write your code inside this function
  a = np.genfromtxt(input_file,dtype = None)
  n = a.shape[1]
  x = a[:,0:n-1]
  y = a[:,n-1]   
  c = np.linalg.lstsq(x, y ,rcond=None)[0]
  # read the data in and fit it. the values below are placeholder values
  # c = np.asarray([])  # coefficients of the linear regression
  # x = np.asarray([])  # input data to the linear regression

  print(c)
  print(x @ c)

# simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)
