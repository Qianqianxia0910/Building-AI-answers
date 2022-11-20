#Beginner B

#Intermediate
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
    port1 = 0
    for port2 in range(1, 5):
      for port3 in range(1, 5):
        for port4 in range(1, 5):
          for port5 in range(1, 5):
            route = [port1, port2, port3, port4, port5]
            if 1 in route and 2 in route and 3 in route and 4 in route:
                    # Modify this if statement to check if the route is valid
                   
    
    
    # https://sea-distances.org/
    # nautical miles converted to km
              D = [
                            [0,8943,8019,3652,10545],
                            [8943,0,2619,6317,2078],
                            [8019,2619,0,5836,4939],
                            [3652,6317,5836,0,7825],
                            [10545,2078,4939,7825,0]
                        ]

    # https://timeforchange.org/co2-emissions-shipping-goods
    # assume 20g per km per metric ton (of pineapples)


              co2 = 0.020
              distance = D[route[0]][route[1]] + D[route[1]][route[2]] + D[route[2]][route[3]] + D[route[3]][route[4]]
              emissions = distance * co2
              print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)
    
main()


#Advanced

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    global smallest, bestroute
    if len(ports) < 1:
      distance = D[route[0]][route[1]]+D[route[1]][route[2]]+D[route[2]][route[3]]+D[route[3]][route[4]]
      if distance < smallest:
        smallest = distance
        bestroute = route
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]], ports[:i]+ports[i+1:])
    # write the recursive function here
    # remember to calculate the emissions of the route as the recursion ends
    # and keep track of the route with the lowest emissions
    pass

def main():
    global smallest
    # Do not edit any (global) variables using this function, as it will mess up the testing
    smallest = smallest *co2
    # this will start the recursion 
    permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()

