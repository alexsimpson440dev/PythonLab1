#User enters in a sentence
userInput = input("Enter in a sentence or phrase to make it camel Case! ")
#splits the words up
splitString = userInput.split(' ')

#newString is assigned to the first word in list and lowers all of it
camelCase = splitString[0].lower()
#for all words in the splitString list after the first
#loop takes the first letter, makes it uppercase
#then adds the rest of the word to it and lowers the rest of the word
for words in splitString[1:]:
    words = words[:1].upper() + words[1:].lower()
    camelCase += words
#prints users new camel case phrase
print('This is your camel case phrase: ', camelCase)