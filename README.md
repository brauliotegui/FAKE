# FAKE: A Fake News detector
Brazilian Fake News detector: Final Data Science Project at SPICED Academy. 

The Presentation for the project can be found [here](https://my.visme.co/view/pvgoqz1e-spiced-final-project).

## Visual Analysis
Through the collection of all the news from the database,...

#### Most used words in real news:
  <img src="https://github.com/brauliotegui/FAKE/blob/master/images/real_truncatednews_wordcloud.png">
  

#### Most used words in fake news:
  <img src="https://github.com/brauliotegui/FAKE/blob/master/images/fakenews_wordcloud.png">

  
 
 ## NLP Model overview
 
 * TfidfVectorizer
 * Logistic Regression {'C': 20000000.0}
 * Metrics:
      - Train score: 100 %
      - Test score: 92.84 %
  
  #### Confusion Matrix:
  <img src="https://github.com/brauliotegui/FAKE/blob/master/images/confusion_matrix.png" width="65%" height="65%">
  
      - Accuracy: 92.85 %
      - Precision: 92.19 %
      - Recall: 93.36 %
      - Specificity: 92.35 %
      - Misclassification Rate: 7.08 %
      
 #### Cross-Validation:
 
      - cross-validation scores [0.92881944 0.90538194 0.91493056 0.90017361 0.9140625 ]
      
     
## App

## The Data
The Dataset used was Fake.Br Corpus. I would like to thank Roney Santos and everyone involved in the development of this dataset, which was incredibly well done and saved me a lot of time and work. This project would not have been possible with such outcomes without a nicely collected and cleaned-up data, like the one from Fake.Br Corpus.

``Monteiro R.A., Santos R.L.S., Pardo T.A.S., de Almeida T.A., Ruiz E.E.S., Vale O.A. (2018) Contributions to the Study of Fake News in Portuguese: New Corpus and Automatic Detection Results. In: Villavicencio A. et al. (eds) Computational Processing of the Portuguese Language. PROPOR 2018. Lecture Notes in Computer Science, vol 11122. Springer, Cham``
