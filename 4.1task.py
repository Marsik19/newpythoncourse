import random
import string

def createRendomDictionaryList():
    dictionarylist = []
    for i in range(random.randint(2, 10)):  # random number of dictionaries
        size = random.randint(1, 5)  # random dictionary size
        keys = random.sample(string.ascii_lowercase, size)  # random letters
        values = random.sample(range(0, 100), size)  # random numbers
        oneDict = dict(zip(keys, values))  # assemble dict.
        dictionarylist.append(oneDict)  # add it to the list
    return dictionarylist

def getAllKeysFromDictionaries(list):
    return set().union(*list)

def createDictionaryFromOther(dictionaries, keys):
    newdict = {}
    for key in keys:
        # new list create
        keyValues = []
        # dictionary in list
        for oneDict in dictionaries:
            # get values by key
            values = oneDict.get(key)
            # all values add to list
            keyValues.append(values)
        # done temporary dictionary
        newdict.update({key: keyValues})
    return newdict

def createFinalDictionaryWithUpdatedKeys(dictionary):
    finaldict = {}
    for k, v in dictionary.items():
        # filter value by none
        filterV = list(filter(None, v))
        # if value empty maximum = 0 , other find maximum value in list
        maximum = 0 if len(filterV) == 0 else max(filterV)
        # when value in list 1
        if len(filterV) == 1:
            # write this value
            finaldict[k] = maximum
        # if value in list empty(0)
        elif len(filterV) == 0:
            # write 0
            finaldict[k] = maximum
        else:
            # find index of v
            indmax = v.index(maximum) + 1
            # index to string
            indmax = str(indmax)
            # key with index and maximum value from list
            finaldict[k + '_' + indmax] = maximum
    return finaldict

dictionarylist = createRendomDictionaryList()
print(dictionarylist)
dict_union = {}
all_keys = getAllKeysFromDictionaries(dictionarylist)
newdict = createDictionaryFromOther(dictionarylist, all_keys)
finaldict = createFinalDictionaryWithUpdatedKeys(newdict)
print(finaldict)
