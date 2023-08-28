import math
user_input = int(input("Enter a number: "))
while user_input >= 10:
    round = math.ceil(user_input/10)
    mod = user_input % 10
    sum = round + mod
print(sum)