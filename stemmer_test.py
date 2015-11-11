from nltk.stem import WordNetLemmatizer

f = open('C:\Users\Young Suk Cho\Box Sync\Research_SpotOn Project\\04. Datasets\\1259 Leadership Nomination Data.xlsx', 'r');

wnl = WordNetLemmatizer()
print(wnl.lemmatize('dogs'))