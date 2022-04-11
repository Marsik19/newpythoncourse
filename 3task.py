import string
import re

textstring = """homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
# text to small latter
lowerText = textstring.replace('\n', '').lower()
# create new array
allSentences = []
# devide string by dot
allSentences = lowerText.split('.')
updatedAllSentences = []
lastSentence = ""

#
for sentence in allSentences:
    if len(sentence) == 0:
        continue
    # found last word in every sentences
    # devide sentence
    wordsInSentence = sentence.split(" ")
    # found last word
    lastWord = wordsInSentence[len(wordsInSentence) - 1]
    # add last words from sentences
    lastSentence += lastWord + " "
    # change mistake with "iz", first letter big
    strippedSentence = sentence.strip().capitalize().replace(' iz ', ' is ').replace('"is"', 'iz').replace("  ", " ") + ". "
    # update array of sentences
    updatedAllSentences.append(strippedSentence)
# big first letter, change dot
updatedLastSentence = (lastSentence.capitalize() + '.').replace(' .', '. ')
# create last sentence
indexForLastSentence = 0
for sentence in updatedAllSentences:
    #find sentence with "paragraph."
    if "paragraph." in sentence:
        # find index this sentences- and index new sentence
        indexForLastSentence = updatedAllSentences.index(sentence) + 1
# insert new sentence
updatedAllSentences.insert(indexForLastSentence, updatedLastSentence)
finalString = ""
# convert array to string
finalString = finalString.join(updatedAllSentences).replace('\n', '')
print(finalString)
# count whitespace
countWhitespaces = len(re.findall(r"\s", finalString))
print(countWhitespaces)

