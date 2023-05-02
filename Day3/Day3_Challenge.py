'''text = [input ("Enter a random text please: ")]
letter1 = input("Enter a first random letter: ")
letter2 = input("Enter a second random letter: ")
letter3 = input("Enter a third random letter: ")


#transform the sentence in list


#print(list)

#Use the commande 'count' to fin the number of apparitions of the letters declared
Numletter1 = str(text.count(letter1))
print(letter1 + " is present " + Numletter1 + " times in the sentence " + text)
Numletter2= str(list.count(letter2))
print(letter2 + " is present " + Numletter2 + " times in the sentence " + text)
Numletter3 = str(list.count(letter3))
print(letter3 + " is present " + Numletter3 + " times in the sentence " + text)

#how many words in the text
Number_Of_Spaces=list.count(" ")
NUmber_Of_words= str(Number_Of_Spaces + 1)
print(f"There are {NUmber_Of_words} words in the sentence")

#The first and latest letter in the sentence
print("The first letter in the sentence is " + list[0])
print("The last letter in the sentence is " + list[-1])


#Invert words order with the commande (list.xxx(xx:xx:-1)
Text_revers=list[::-1]
print(Text_revers)

#find the word "python" with the boolean ("python" in the list)
print("python" in text)'''

#Insert the text in variable
text = (input("Please, enter a sentence: "))
text = text.lower()

#Creation of the letter list
Letters = []
Letters.append(input("Please enter un first letter: "))
Letters.append(input("Please enter un second letter: "))
Letters.append(input("Please enter un third letter: "))

#Number of letter's apparition
print(f"The letter '{Letters[0]}' appared {text.count(Letters[0])} in the sentence")
print(f"The letter '{Letters[1]}' appared {text.count(Letters[0])} in the sentence")
print(f"The letter '{Letters[2]}' appared {text.count(Letters[0])} in the sentence")

#Number of words
words = text.split()
print(f"The are {len(words)} words in the sentence")

#The first and last letter
print(f"The first letter of the sentence is {words[0]}")
print(f"The latest letter of the sentence is {words[-1]}")

#Inverse the words
words.reverse()
words_reversed = " ".join(words)
print(f"If we reverse the sentence, we can read this : {words_reversed}")

#Presence of the word "Python"
word_python= "python" in text
dic = {True:"is",False:"is not"}
print(f"In the sentence, there {dic[word_python]} the word 'python'")
