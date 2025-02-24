import Stemmer

stemmer = Stemmer.Stemmer('english')
print(stemmer.stemWord('running'))
print(stemmer.stemWord('runs'))
print(stemmer.stemWord('run'))
