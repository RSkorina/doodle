#Pig Latttin
import re


def pigLatinWord(word):
	regEx = re.compile("(\"?)([a-zA-Z]{1}(?:[']?))([A-Za-z-]*)([.?!,]?)(\"?)")
	partsWord = regEx.match(word)
	# first capitol Letter
	firstLetter = partsWord.group(2)
	wordBody = partsWord.group(3)
	ending = partsWord.group(4)
	if(firstLetter.upper() == firstLetter):
		wordBody = wordBody.capitalize()
	toReturn = partsWord.group(1) + wordBody +  firstLetter.lower() + "ay" + ending + partsWord.group(5)
	print(toReturn)
	return toReturn

def toPigLatin(fullText):
	pigLatinArray = fullText.split(" ")
	for i in range(len(pigLatinArray)):
		pigLatinArray[i] = pigLatinWord(pigLatinArray[i])
	
	print(" ".join(pigLatinArray))
	return " ".join(pigLatinArray)
	
	
		
	
assert(pigLatinWord("hello") == 'ellohay')
assert(pigLatinWord("Hello") == 'Ellohay')
assert(pigLatinWord("Hello.") == 'Ellohay.')
assert(pigLatinWord("Hello,") == 'Ellohay,')
assert(pigLatinWord("Hello?") == 'Ellohay?')
assert(pigLatinWord("Hello!") == 'Ellohay!')
assert(pigLatinWord("He-llo.") == 'E-llohay.')
assert(pigLatinWord("H'e-llo.") == 'E-lloh\'ay.')
assert(pigLatinWord("\"H'e-llo.\"") == '"E-lloh\'ay."')
assert(pigLatinWord("O'Reilly") == 'Reillyo\'ay')
assert(pigLatinWord("O'Reilly!\"") == 'Reillyo\'ay!"')


assert(toPigLatin("\"There is a man named O'Reilly!\"") == '"Heretay siay aay anmay amednay Reillyo\'ay!"')
 
