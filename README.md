# FAKE: A Fake News detector
- Brazilian Fake News detector: Final Data Science Project at SPICED Academy. 
- The Presentation for the project can be found [here](https://my.visme.co/view/pvgoqz1e-spiced-final-project).

## Description
The increase of social media usage has led to a more interconnected society, but has also led to problems never faced by our society before. One of these problems is the fast spread of misinformation -- fake news, as it is popularly referred to. I believe the massive spread of fake news to be one of most urgent problems we should tackle as a global and interconnected society right now, and this is why I chose to develop this Fake News detector as my final project during a Data Science bootcamp. 

I developed a fake news detector specifically for Brazilian Portuguese texts, because in the past years I have noticed a massive amount of this type of misinformation being spread in Brazil which is very alarming! Brazil has one of the largest online populations in the world. In fact, according to The Guardian, Brazil has over 120 million Whatsapp users alone, while the number of Facebook users is currently even higher. Brazil also faces the issue of lack of regulation and WhatsApp executives have already acknowledged that Brazilian accounts were the target of massive spamming operations by digital marketing agencies before the 2018 election, in a breach of the app’s terms and conditions. Not only that, but according to Folha de S. Paulo, Bolsonaro supporters --  far-right supporters -- had paid digital marketing firms up to 12 million reais ($3.26 million) each to spread tens of thousands of attack ads. We can only imagine how much impact those endless fake news attacks had on the elections and the final outcome, which had consequences on the lives of millions and millions of people. Thus, the importance of tackling such a viral and harming problem.

"The vast majority of false information shared on WhatsApp in Brazil during the presidential election favoured the far-right winner, Jair Bolsonaro, a Guardian analysis of data suggests", [The Guardian](https://www.theguardian.com/world/2019/oct/30/whatsapp-fake-news-brazil-election-favoured-jair-bolsonaro-analysis-suggests).

**FAKE** is a fake news detector developed with a NLP classifier model trained on a dataset with over 7.000 articles. Flask-app is used to create a web-application in order to make the model accessible to third-party users. 

## Visual Analysis
Through the collection of all texts from the database it was possible to analyze the content of real, reliable news and the fake ones. An analysis of the Meta Data was also possible thanks to the dataset that collected such data and made it available for studies. While the Meta Data did not gave me insights that I ended up using in this program, it was interesting to confirm a few pre-conceptions, such as the fact that Fake News has a higher percentage of spelling errors and more links inside the news. On the other hand, a study on the most frequent used words in each sub-set -- true news and fake news -- showed an overview of the content of each. While true news had a more balanced word choice, fake news focused a lot on names of left-wing leaders who were the main target of those texts. Besides the overuse of the words Lula and Dilma, the word Brasil also appeared quite a lot. This was not at all surprising for me, due to the fact that when I was exposed to fake news I noticed it was mostly spread by the far-right and had a nationalist agenda. 

#### Most used words in real news:
  <img src="https://github.com/brauliotegui/FAKE/blob/master/images/real_truncatednews_wordcloud.png">
  

#### Most used words in fake news:
  <img src="https://github.com/brauliotegui/FAKE/blob/master/images/fakenews_wordcloud.png">

## Technology and tools used:
* Python
* Scikit-learn
* Pickle
* Flask
* Heroku
* HTML
* CSS
 
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
      
     
## Web-App
FAKE - the fake news web-application can be accessed on https://detectordementiras.herokuapp.com/

## The Data
The Dataset used was Fake.Br Corpus. I would like to thank Roney Santos and everyone involved in the development of this dataset, which was incredibly well done and saved me a lot of time and work. This project would not have been possible with such outcomes without a nicely collected and cleaned-up data, like the one from Fake.Br Corpus.

``Monteiro R.A., Santos R.L.S., Pardo T.A.S., de Almeida T.A., Ruiz E.E.S., Vale O.A. (2018) Contributions to the Study of Fake News in Portuguese: New Corpus and Automatic Detection Results. In: Villavicencio A. et al. (eds) Computational Processing of the Portuguese Language. PROPOR 2018. Lecture Notes in Computer Science, vol 11122. Springer, Cham``
