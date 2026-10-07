import nltk
from nltk.tokenize import word_tokenize

sentence = input("enter a sentence:")

word = word_tokenize(sentence)
pos_tags = nltk.pos_tag(word)

print("\nword\t\tPOS_TAG")
print("-" * 30)

for word, tag in pos_tags:
    print(f"{word}\t\t{tag}")
