sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence.upper())

#Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
word_list = ["Simple","is","better","than","complex."]
print(" ".join(word_list))

#Replace in the following sentence:
#If the implementation is hard to explain, it might be a bad idea.
#the following pairs of words:
#hard --> easy
#bad --> good
#and display the sentence with both words modified.
sentence = "If the implementation is hard to explain, it might be a bad idea."
sentence1 = sentence.replace("hard","easy")
print(sentence1.replace("bad","good"))