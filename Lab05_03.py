words = input("Enter more than 2 words: ")
words = words.strip()
index = words.find(' ')

if index == -1:
    print("the first word is:",words)
else:
    print("the first word is:",words[:index])
