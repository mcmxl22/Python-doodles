import random
 
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 
while True:
    matrix = random.choice(num)
    for i in matrix:
        print(i, end='\t')
