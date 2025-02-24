import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize('running', pos='v'))
print(lemmatizer.lemmatize('runs', pos='v'))
print(lemmatizer.lemmatize('run', pos='v'))
print(lemmatizer.lemmatize('ran', pos='v'))
print(lemmatizer.lemmatize('runner', pos='n'))
print(lemmatizer.lemmatize('studies', pos='n'))
