import random

# create list of random number
randlist = [random.randrange(0, 1000) for i in range(100)]

# start sorted list, run for repetitive iteration
for run in range(len(randlist) - 1):
    for i in range(len(randlist) - 1 - run):

        # if 1 value bigger than 2, changed it
        if randlist[i] > randlist[i + 1]:
            randlist[i], randlist[i + 1] = randlist[i + 1], randlist[i]
# print our list
print("Random number list is : " + str(randlist))
# set started values
sum_even = 0
sum_odd = 0
even_count = 0
odd_count = 0
for i in randlist:
    # found even value, if number divide on 2 without remainder- value even
    if (i % 2) == 0:
        # summary od all event value
        sum_even += i
        # count even value
        even_count += 1
        average_even = sum_even / even_count

    # found odd value, if number divide on 2 with remainder - value odd
    elif (i % 2) != 0:
        # summary od all odd value
        sum_odd += i
        # count odd value
        odd_count += 1
        average_odd = sum_odd / odd_count

print("SUM of odd numbers is: ", sum_odd)
print("Count of odd numbers is: ", odd_count)
print("Average of odd numbers is: ", average_odd)
print("SUM of even numbers is: ", sum_even)
print("Count of even numbers is: ", even_count)
print("Average of even numbers is: ", average_even)
