import time

reminder = input("What shall I remind you about? ")
local_time = int(input("In how many minutes? "))
local_time = local_time * 60
time.sleep(local_time)
print(reminder)