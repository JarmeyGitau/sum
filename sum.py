# Find the sum of just the odd numbers in this list
total=0
numbers = [62, 60, 53, 53, 33, 3, 25, 61, 36, 1, 69, 55, 56, 39, 32, 76, 20, 62, 47]
for x in numbers:
  if x%2==1:
    total += x    
print(total)