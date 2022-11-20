#Beginner   C  

#Intermediate   

def flip(n):
  odds = 1.0
  r = 2         # start with 50% chance of the magic coin, which is the same as odds = 1:1
  for i in range(n):
    odds = odds * r           # edit here to update the odds
    i += 1
  print(odds)

n = 1
flip(n)

#Advanced
import numpy as np

p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]   # normal
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]   # loaded

def roll(loaded):
  if loaded:
    print("rolling a loaded die")
    p = p2
  else:
    print("rolling a normal die")
    p = p1

    # roll the dice 10 times
    # add 1 to get dice rolls from 1 to 6 instead of 0 to 5
  sequence = np.random.choice(6, size=10, p=p) + 1 
  for roll in sequence:
    print("rolled %d" % roll)
  return sequence

def bayes(sequence):
  odds = 1.0           # start with odds 1:1
  for roll in sequence:
  # edit here to update the odds
    if roll == 6:
      r = 0.5/(1/6)
    else:
      r = 0.1/(1/6)
      odds = odds * r
  if odds > 1:
    return True
  else:
    return False

sequence = roll(True)
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")
