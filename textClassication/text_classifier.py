# Text Classification

import numpy as np
import re
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files
nltk.download('stopwords')


# Importing dataset
reviews = load_files('txt_sentoken/')
X,y = reviews.data,reviews.target

# Storing as Pickle Files 

with open('X.pickle','wb') as f:
    pickle.dump(X,f)

with open('y.pickle','wb') as f:
    pickle.dump(y,f)


# Unpickling the dataset 

with open('X.pickle','rb') as f:
    X = pickle.load(f)
    
    with open('y.pickle','rb') as f:
        y = pickle.load(f)
        
        
# Creating the Corpus
corpus = []
for i in range(0,len(X)):
    review = re.sub(r'\W',' ',str(X[i]))
    review = review.lower()
    review = re.sub(r'\s+[a-z]\s+',' ',review)
    review = re.sub(r'^[a-z]\s+',' ',review)
    review = re.sub(r'\s+',' ',review)
    corpus.append(review)

#Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features=2000,min_df= 3, max_df=0.6,stop_words = stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()

# TF-IDF model
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
X = transformer.fit_transform(X).toarray()








        
