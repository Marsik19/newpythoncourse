import string
import re

textstring = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
def normalizeText(text):
    lowerText = text.replace('\n', '').lower()
    allSentences = lowerText.split('.')
    updatedAllSentences = __updateSentenses(allSentences)
    finalString = "".join(updatedAllSentences).replace('\n', '')
    return finalString

def __updateSentenses(allSentences):
    updatedAllSentences = []
    lastSentence = ""

    for sentence in allSentences:
        if len(sentence) == 0:
            continue

        wordsInSentence = sentence.split(" ")
        lastWord = wordsInSentence[len(wordsInSentence) - 1]
        lastSentence += lastWord + " "
        strippedSentence = __beautifySentenceWithReplaceIs(sentence, "iz", "is")
        updatedAllSentences.append(strippedSentence)

    updatedLastSentence = (lastSentence.capitalize() + '.').replace(' .', '. ')
    indexForLastSentence = 0
    for sentence in updatedAllSentences:
        if "paragraph." in sentence:
            indexForLastSentence = updatedAllSentences.index(sentence) + 1
    updatedAllSentences.insert(indexForLastSentence, updatedLastSentence)
    return updatedAllSentences

def __beautifySentenceWithReplaceIs(sentence, wordForChange, wordWhichIsReplaced):
    wordForChangeWithWhitespaces = ' ' + wordForChange + ' '
    wordWhichIsReplacedWithWhitespaces = ' ' + wordWhichIsReplaced + ' '
    wordWhichIsReplacedWithQuotes = '"' + wordWhichIsReplaced + '"'
    return sentence.strip().capitalize().replace(wordForChangeWithWhitespaces, wordWhichIsReplacedWithWhitespaces).replace(wordWhichIsReplacedWithQuotes, wordForChange).replace("  ", " ") + ". "

def __countWhitespaces(text):
    return len(re.findall(r"\s", normalizedString))

normalizedString = normalizeText(textstring)
countWhitespaces = __countWhitespaces(normalizedString)
print(normalizedString)
print(countWhitespaces)

