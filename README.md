# CS412-Course-Project
A course project involving categorization of Instagram accounts and prediction of like counts for posts.

* Overview of the repository:

annotation_combiner.py (https://github.com/mberketatar/CS412-Course-Project/blob/patch-1/annotation_combiner.py) was used to merge the annotation files of the group members.

filter_dataset.py (https://github.com/mberketatar/CS412-Course-Project/blob/patch-1/filter_dataset.py) was used to remove certain fields from the data.

Classification.ipynb (https://github.com/mberketatar/CS412-Course-Project/blob/patch-1/Classification.ipynb) main part of the classification step.

Regression.ipynb (https://github.com/mberketatar/CS412-Course-Project/blob/patch-1/Regression.ipynb) main part of the regression step.

* Methodology:
  
During the project we came up with several ideas some of which did not make it to do final product. 

For the classification step we initially used the Naive Bayes model given to us and were able to increase it accuracy to an extend but we were not satisfied with it. We also considered lemmatization using Zeyrek library, but due to its speed we were not able to use it. Later we switched to BERTurk, which is a LLM derived from Bert.

For the regression step

At one point we considered inclusion of annoted files by our members (the ones we did before the first round) and decided the categories of the accounts by the  majority vote. Even though this increased the sample size it decreased the accuracy which is likely due to our annotation accuracy. In the end we decided to exclude them, but we included the .py file in the repository for the sake of completeness.

  High-level explanation of things considered
and solutions offered.

* Results:
  
Confusion matrix for the classification step of round 3
![WhatsApp Image 2025-01-12 at 19 11 18](https://github.com/user-attachments/assets/07cf66b5-3893-4c46-89ed-5dc59c824cdd)
Graph of Predicted Likes to Actual Likes
![WhatsApp Image 2025-01-12 at 19 10 42](https://github.com/user-attachments/assets/055d65fe-e6bd-4cef-9671-c0eb860fc298)

* Team contributions:
* Deniz
* Berke
* Utku
* Özgür
* Alp
