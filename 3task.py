import string
textstring="""homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

lowerText = textstring.lower()

allSentences = []
allSentences = lowerText.split('.')
updatedAllSentences = []
lastSentence = ""

for sentence in allSentences:
    if len(sentence) == 0:
        continue

    wordsInSentence = sentence.split(" ")
    lastWord = wordsInSentence[len(wordsInSentence)-1]
    lastSentence += lastWord + " "
    strippedSentence = sentence.strip().capitalize().replace(' iz ', ' is ').replace('"is"', 'iz') + ". "
    updatedAllSentences.append(strippedSentence)

updatedLastSentence = lastSentence.capitalize()+'.'
updatedAllSentences.append(updatedLastSentence)

finalString = ""
finalString = finalString.join(updatedAllSentences)
print(finalString)


print(finalString.count(' '))

# count=0
# for i in finalString:
#   if  i==" " or i=="\n":
#        count=count+1
# print("Number of spaces in a string:",count)