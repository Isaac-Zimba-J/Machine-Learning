# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:08:14 2023

@author: Zaac
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


# import the data
data = pd.read_csv("C:/Users/Zaac/Desktop/Workspace/python/torch/side machine learning/IMDB_ Naive_Bayes/IMDB Dataset.csv")

# convert data into a dataframe
dataframe = pd.DataFrame(data)


# process the data to properly be fed to the model
dataframe['sentiment'] = (dataframe['sentiment'] == 'positive').astype(int)
dataframe['review'] = dataframe['review'].str.replace('[^\w\s]','').str.lower()

# set the data to x samples and y to true values 
X = dataframe['review']
y = dataframe['sentiment']



vectorizer = CountVectorizer()
X_vectorised = vectorizer.fit_transform(X)


# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorised,y, test_size=0.2, random_state=42)

# prepare the model 
naive_bayes_model = MultinomialNB()
naive_bayes_model.fit(X_train, y_train)

y_predic = naive_bayes_model.predict(X_test)

# evaluate the data 
accuracy = accuracy_score(y_test, y_predic)
report = classification_report(y_test, y_predic)


print(f'Accuracy: {accuracy}')
print(report)
