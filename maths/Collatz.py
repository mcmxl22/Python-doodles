def collatz(num):
    result = []
    while len(result) < 25:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        result.append(int(num))
    print(result)


collatz(7)