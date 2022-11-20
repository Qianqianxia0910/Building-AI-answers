#Beginner   C

#Intermediate
def main():
  countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
  populations = [5615000, 5439000, 324000, 5080000, 9609000]
  fishers = [1891, 2652, 3800, 11611, 1757]

  total_fishers = sum(fishers)
    
  # write your solution here

  for c,num in zip(countries,fishers):
    p = num/total_fishers
    print("%s %.2f%%" % (c,p * 100))

main()

#Advanced

countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
  if winner_gender == 'female':
    fishers = female_fishers
  else:
    fishers = male_fishers

  # write your solution here

  guess = None
  biggest = 0.0
  total_fishers = sum(fishers)
  max_index = fishers.index(max(fishers))
  guess = countries[max_index] 
  biggest = fishers[max_index]/total_fishers
  return (guess, biggest)

def main():
  country, fraction = guess("male")
  print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction * 100))
  country, fraction = guess("female")
  print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction * 100))

main()
