import random

# create list of random number
randlist = random.sample(range(0, 100), 10)
b=list()
# for run in range(len(randlist)):
#     for minimum in range(len(randlist) - run):
#      if min(randlist)<101:
#           minimum = min(randlist)
#           b.append(minimum)
#           randlist.remove(minimum)
while randlist:
    minimum = min(randlist)
    b.append(minimum)
    randlist.remove(minimum)
print(b)
list_even = list()
list_odd = list()

for i in b:
    # found even value, if number divide on 2 without remainder- value even
        if (i % 2) == 0:
            list_even.append(i)

        elif (i % 2) != 0:
            list_odd.append(i)
try:
    avg_even=sum(list_even)/len(list_even)
    avg_odd=sum(list_odd)/len(list_odd)

except ZeroDivisionError:
        print("division on 0")
   # try:
        #if (0%2)
    #except:
print("List of off: ", list_odd)
print("List of even ", list_even)
print("Avg of odd", avg_odd)
print("Avg of even", avg_even)


