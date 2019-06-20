import random
 
characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
              'A', 'Z', '=', '+', '#', '.', '<', ':', '&', '$']
 
while True:
    matrix = random.choice(characters)
    for i in matrix:
        print(i, end='\t')
