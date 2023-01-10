#Let´s traduce your word to pig latin...

word = input("Let's see what are you thinking... write a word: ")

firstLetter = word[0]
lenght = len(word)
incompleteWord = word[1:lenght]

newWord = incompleteWord + firstLetter + "ay"

print(newWord)






