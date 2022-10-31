word = input("Enter a word: ")
if word[::-1] == word[0:]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
