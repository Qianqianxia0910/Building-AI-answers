#Beginner   C C B 

#Intermediate  
# input values for three mökkis: 
#  - size [m^2], 
#  - size of the sauna [m^2], 
#  - distance to water [m], 
#  - number of indoor bathrooms, 
#  - proximity of neighbors [m]
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200 , -50, 5000, 100]

def predict(X, c):
  for i in range(len(X)):
    value = X[i]
    coe_value = zip(value,c)
    res = []
    for num in coe_value:
      res.append(num[0] * num[1])
    price = sum(map(int,res))
    # write a loop that goes over the cabin data and for each cabin prints out 
    # the predicted price of the cabin you can assume that the number of inputs
    # and the number of coefficients are the same           
    print(price)

predict(X, c)

#Advanced

# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    for i in range(len(X)):
        value = X[i]
        coe_value = zip(value,c)
        res = []
        for num in coe_value:
            res.append(num[0] * num[1])
        price = sum(map(int,res))
    
              
        print(price)

predict(X, c)

