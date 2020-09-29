"""machine-learning Code that detects Fake News"""
import os
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

CORPUS = []
LABEL = []

DIR_1 = '../Data/size_normalized_texts/fake/'
LIST_1 = os.listdir(DIR_1)
NUMBER_FILES = len(LIST_1)

for i in range(NUMBER_FILES):
    title = LIST_1[i]
    LABEL.append(1)
    with open(DIR_1 + title, 'r') as reader:
        doc = reader.read()
        doc.lower()
        doc.split()
        CORPUS.append(doc)

DIR_0 = '../Data/size_normalized_texts/true/'
LIST_0 = os.listdir(DIR_0)
NUMBER_FILES = len(LIST_0)

for i in range(NUMBER_FILES):
    title = LIST_0[i]
    LABEL.append(0)
    with open(DIR_0 + title, 'r') as reader:
        doc = reader.read()
        doc.lower()
        doc.split()
        CORPUS.append(doc)

assert len(CORPUS) == len(LABEL)

def vectors_and_df(corpus, label):
    """
    creates vectors for articles/news and returns dataframe with news
    as word vectors indexed by 1(Fake) or 0(Not Fake).

    Parameters
    ----------
    corpus : Trained scikit-learn model pipeline.
    label : str

    Returns
    ---------
    dataframe, vectorized corpus
    """

    cv = TfidfVectorizer()
    cv.fit(corpus)
    corpus_vecs = cv.transform(corpus)

    return pd.DataFrame(corpus_vecs.todense(), index=label,
                        columns=cv.get_feature_names()), cv

DATAFRAME, CV = vectors_and_df(CORPUS, LABEL)

X = DATAFRAME
Y = DATAFRAME.index

LRM = LogisticRegression(C=2e7, max_iter=300)
LRM.fit(X, Y)

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

    prediction = LRM.predict(ynew)
    result = prediction[0]

    return result
