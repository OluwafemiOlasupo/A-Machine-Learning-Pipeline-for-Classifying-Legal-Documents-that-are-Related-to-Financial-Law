#PROJECT: 
A Rule-Based (Heuristics) System for Classifying Documents that are relevant to Financial Law

#INSTALLATION AND SET-UP: 
This project was written in a virtual environment (Kaggle Notebook), to handle large datasets without crashing

#PACKAGES AND LIBRARIES:
This project was written in Python 3.10, and some of the packages and libraries used are: 
pandas
pylint
matplotlib
seaborn
scikit-learn
pytest (to test the behaviour of the rule-based system)

#Data Used: 
Two major datsets were used (from which other subsets were created):
- the RELEVANCE DATASET, which has 4 features
- the REGULATIONS DATASET, which has 8 features
- 
#Key Important Observations
1. There were 117 unique source languages.

2. Analysis on the “RequirementSource" column showed that Guidance formed the bulk of the false labels (over 50% ), 
and subsequently had the least true labels. Though regulations performed better, they were also about 36% of the false labels. 
- However, most of the true labels came from the “Regulations” document.

3. 39 source languages were within less than 5% of the total true labels.

4. English, Russian, and Spanish documents alone formed a total of about 70% of the true documents, 
which means that most of the true labels are from these languages. 
- It might be that most of the keywords that are being used to indicate relevance are found in documents from these source languages.

5. Documents from English, Russian, Spanish, Ukrainian, Portuguese, and Mandarin Chinese formed about 93% of the total true labels, 
which means that more attention should be paid to documents that have these source languages, as well as the regulators that labeled these source languages.

6. Documents with English as the source language were the most relevant (about 35% of the total relevant documents).

7. The source of the documents, whether PDF or a web URL did not have a tangible effect on the labeling.

8. Only about 8.4% of the total documents are relevant to financial law, showing that the distribution is highly imbalanced.

9. There were about 832 unique “RegulatorId”s. To reduce the category, they were all grouped into two categories, based on the relevance of 
the documents that each regulator. The categories are:
a. Relevance: Regulators whose documents are usually relevant or irrelevant
b. Volume (of documents Released): High, Medium, and Low.

- At the end, for the Volume category, the low category was 35, 184, High was 29, 940, and Medium was 9, 690. 
- It was seen that about 96% of documents in the “High” category did not contain relevant regulations (False). 
- About 4% of documents in the “High” category contain relevant regulations (True).
- About 89% of documents in the “Low” category column do not contain relevant regulations (False), 
while about 11% of documents in the “Low” category column contain relevant regulations (True)
- About 87% of documents in the “Medium” category do not contain relevant regulations (False).
- About 13% of documents in the “Medium” category contain relevant regulations (True).

Overall, it is safe to say that an average of about 90% (or more) of the total documents are irrelevant to financial law.

10. Using a list of keywords that are relevant to financial law from the top 4 languages that have true
labels, I tried to look for their instances in the unlabeled data, to make predictions for the unlabeled data.

- However, it was quite difficult to get these keywords out (a number of them were actually 
gotten by studying “Content” columns of the top 4 “SourceLanguages” in the labeled data), 
due to the ambiguity of each “Content” column, even after initial cleaning 
(such as removal of HTML tags, and other ambiguous characters).

#. A key limitation of this system is that it uses only a set/number of keywords, which limit the scope of the system, thus, resulting in lower accuracy.

#EVALUATION METRICS: ACCURACY
- The accuracy of this system can be better improved upon, if more relevant words/phrases/patterns can be gotten.

#. THE ROLE HUMANS PLAY: 
1. Defining not just the most important or relevant keywords that point to relevance, 
but how these keywords should be combined for a document to be termed relevant, 
e.g, if “merger” is a recognized keyword, what of instances where it is used to connote something else, probably not in a financial law instance, 
e.g, “merger” can be used to describe the resultant effect of combining two political parties, 
and if “merger” alone were to be considered in that case, that would be a wrong classification, thus, reducing the overall accuracy of the system.

2. Constant improvement of the system's evaluation metrics, by creating more relevant features, to aid future predictions,
and also to save time

#Question to Ask: Do I then need Machine Learning to solve this problem? If “Yes”, why?
- Deciding if a document is relevant or not must be automated since there is just a 3-days window period before clients must be informed 
about documents that are relevant, to save time.
- Documents that have early Publication Dates (that is, when they were released) must be considered first, 
so they can be sorted before the end of the 72 hours window.
Sending the result of the automated labeling should also be automated, to reduce time.
