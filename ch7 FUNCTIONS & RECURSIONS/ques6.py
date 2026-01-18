# Write a python function to remove a given word from a list ad strip it at the same time.
def remove_and_strip(word_list, word_to_remove):
    stripped_list = [word.strip() for word in word_list if word.strip() != word_to_remove]
    return stripped_list
words = ["  apple  ", "banana", "  cherry  ", "date", "  banana  "]
word_to_remove = "banana"
result = remove_and_strip(words, word_to_remove)
print(result) 