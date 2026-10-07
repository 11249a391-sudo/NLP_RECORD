import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text=input("enter a text:")

tokens = word_tokenize(text)

tagged_words = pos_tag(tokens)

print("\nPart_of_Speech Tagged Sentence")
print("-"*40)

for word,tag in tagged_words:
    print(f"{word:<15} {tag}")
