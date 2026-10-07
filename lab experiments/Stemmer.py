from nltk.stem import PorterStemmer
ps = PorterStemmer()
example_word = ["loved","played","running","died"]
for w in example_word:
     print(ps.stem(w))
