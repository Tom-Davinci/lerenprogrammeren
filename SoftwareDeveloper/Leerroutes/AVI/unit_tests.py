from functies import *

# test 1: getNumberOfCharacters
if getNumberOfCharacters('aap') == 3:
    print("Test geslaagd 1")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog wat extra testen voor getNumberOfCharacters

if getNumberOfCharacters("aard, appel") == 9:
    print("Test geslaagd 2")
else:
    print("Deze test is niet geslaagd")

if getNumberOfCharacters("") == 0:
    print("Test geslaagd 3")
else:
    print("Deze test is niet geslaagd")

# test 2: getNumberOfSentences
if getNumberOfSentences(getText('easy')) == 14:
    print("Test geslaagd 4")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog een extra testen voor getNumberOfSentences (gebruik test.txt).

# test 3: getNumberOfWords
print(getNumberOfWords(getText('data\difficult1.txt')))
if getNumberOfWords(getText('data\difficult1.txt')) == 82:
    print("Test geslaagd 5")
else:
    print("Deze test is niet geslaagd")

if getNumberOfWords(getText('data\easy1.txt')) == 11:
    print("Test geslaagd 6")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog een extra testen voor getNumberOfWords (gebruik test.txt).



# test 4: getAVIscore
if getAVIscore(getText("easy")) == 5:
    print("Test geslaag 6")
else:
    print("Deze test is niet geslaagd")