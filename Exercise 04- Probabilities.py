#Beginner   C

#Intermediate

import random

def main():
  prob = 0.20
  if random.random() > prob:
    print('dog')
  else:
    print('cat')

main()

#Advanced

import random

def main():
  prob = 0.10

  if random.random() < prob:
    favourite = "bats"
  elif random.random() >= (1-prob):
    favourite = "cats"
  else:
    favourite = "dogs"

  print("I love " + favourite) 


main()