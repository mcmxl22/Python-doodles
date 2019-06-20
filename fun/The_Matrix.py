import random
 
num0 = '0'
num1 = '1'
num2 = '2'
num3 = '3'
num4 = '4'
num5 = '5'
num6 = '6'
num7 = '7'
num8 = '8'
num9 = '9'
 
while True:
    matrix = random.choice([num0, num1, num2, num3, num4,
                            num5, num6, num7, num8, num9])
    for i in matrix:
        print(i, end='\t')