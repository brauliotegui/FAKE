# FAKE: A Fake News detector
Brazilian Fake News detector: Final Data Science Project at SPICED Academy

## Visual Analysis
Through the collection of all the news from the database,...

#### Most used words in real news:
 <p align="center">
  <img src="https://github.com/brauliotegui/FAKE/blob/master/images/real_truncatednews_wordcloud.png">
  </p>

#### Most used words in fake news:
<p align="center">
  <img src="https://github.com/brauliotegui/FAKE/blob/master/images/fakenews_wordcloud.png">
  </p>
  
 
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
      
     
## App
