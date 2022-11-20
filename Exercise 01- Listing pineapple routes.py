#Beginner  C:6

#Intermediate
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
                    # Modify this if statement to check if the route is valid
                    if 1 in route and 2 in route and 3 in route and 4 in route:
                        # for i in range(0,5):

                        # do not modify this print statement
                        print(' '.join([portnames[i] for i in route]))

main()

#Advanced

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    # Write your recursive code here
    if len(ports) < 1:
    # Print the port names in route when the recursion terminates
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]], ports[:i]+ports[i+1:])

# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))


