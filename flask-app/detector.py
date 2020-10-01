"""machine-learning Code that detects Fake News"""
import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


# Load pickled model
with open("logistic_model.pkl", 'rb') as file:
    PICKLE_MODEL = pickle.load(file)
# Load CV fitted
with open("CVfitted.pkl", 'rb') as file:
    CV = pickle.load(file)

def predict(new_text):

    """
    Takes the pre-trained model pipeline and predicts if the new text seems
    to be fake news or not.

    Parameters
    ----------
    new_text : str

    Returns
    ---------
    prediction : int

    """
    article = [new_text]
    # transform song into vector matrix
    new_article_vecs = CV.transform(article)
    ynew = new_article_vecs.todense()

    prediction = PICKLE_MODEL.predict(ynew)
    result = prediction[0]

    return result
