from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
example_word = "it is very important to be pythonly while you are pythoning with python.all pythoners have poorly pythoned atleast onces"
word = word_tokenize(example_word)
for w in word:
     print(ps.stem(w))
