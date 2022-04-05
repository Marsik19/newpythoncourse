import random
import string
dictionarylist = []
for i in range(random.randint(2, 10)): # random number of dictionaries
    size = random.randint(1, 5)    # random dictionary size
    keys = random.sample(string.ascii_lowercase,size)  # random letters
    values = random.sample(range(0, 100), size) # random numbers
    oneDict = dict(zip(keys, values))                      # assemble dict.
    dictionarylist.append(oneDict)                              # add it to the list
# рядок знизу для перевірки нуля
#dictionarylist=[{'u': 0,'l': 84, 'r': 90, 'w': 41, 'k': 25, 'f': 81}, {'w': 23, 'q': 96, 'i': 20, 'a': 68, 'h': 77}, {'v': 68}, {'t': 35, 'f': 80, 'p': 65, 'i': 44}, {'b': 74, 't': 8, 'f': 25, 's': 67}, {'s': 3}, {'h': 99, 's': 67, 'z': 27, 'v': 62, 'c': 89}, {'e': 82, 'i': 16, 'a': 7, 'r': 96, 't': 56}, {'v': 90, 'n': 20, 'w': 67}, {'i': 32, 'o': 87}]
print(dictionarylist)
dict_union = {}
# for oneDict in dictionarylist:
#     all_keys2.append([*oneDict])
#     for keys in oneDict:
#         all_keys.append(keys)
all_keys=set().union(*dictionarylist)
# перебрати дікшинарі , коли перебрали - з загального взяли перший дікшинаі- взяли ключ- і подивитись чи ключ в цьому словнику
 # результат  в ліст для ключаб словник
newdict={}
# перебираєм список ключів
for key in all_keys:
    # new list create
    keyValues=[]
    # dictionary in list
    for oneDict in dictionarylist:
        #get values by key
        values = oneDict.get(key)
        # all values add to list
        keyValues.append(values)
    #done temporary dictionary
    newdict.update({key: keyValues})
finaldict={}
# key and values in temporary dictionary
for k,v  in newdict.items():
    # filter value by none
    filterV = list(filter(None, v))
    # if value empty maximum = 0 , other find maximum value in list
    maximum = 0 if len(filterV) == 0 else max(filterV)
    #when value in list 1
    if len(filterV)==1:
        # write this value
         finaldict[k]=maximum
# if value in list empty(0)
    elif len(filterV) == 0:
        #writte 0
          finaldict[k]=maximum
    else:
        # find index of v
         indmax = v.index(maximum) + 1
        # index to string
         indmax = str(indmax)
        #key with index and maximum value from list
         finaldict[k + '_' + indmax] = maximum

print(finaldict)

