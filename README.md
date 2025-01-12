# CS412-Course-Project
CS412-Course-Project


A course project involving categorization of Instagram accounts and prediction of like counts for posts.


Overview of the repository:


annotation_combiner.py (https://github.com/mberketatar/CS412-Course-Project/blob/patch-1/annotation_combiner.py) was used to merge the annotation files of the group members.


filter_dataset.py (https://github.com/mberketatar/CS412-Course-Project/blob/patch-1/filter_dataset.py) was used to remove certain fields from the data.


Classification.ipynb (https://github.com/mberketatar/CS412-Course-Project/blob/patch-1/Classification.ipynb) main part of the classification step.


Regression.ipynb (https://github.com/mberketatar/CS412-Course-Project/blob/patch-1/Regression.ipynb) main part of the regression step.


Methodology:


During the project we came up with several ideas, some of which did not make it to the final product.
For the classification step, we initially used the tf-idf Naive Bayes model given to us and were able to increase its accuracy slightly by modifying the alpha variable and some other hyperparameters, but we were not satisfied with it. We also considered lemmatization using the Zeyrek library, but it was too slow so we were unable to use it. Later, we figured out that Word2Vec was better than tf-idf, and that BERT was better than Word2Vec due to its ability to understand semantics, so we switched to BERTurk for natural language processing. We combined a person's username, biography and all captions of their posts into a single column called ‘text’, and fine tuned the pre-trained BERTurk model to train it using the text column and training file which contained the categories of the annotated accounts.


We merged our annotation data into a single file, which in case of multiple people categorizing the same account differently, picked the majority vote among them. Then, we merged this combined annotation file with our training set, and gave it priority over conflicts as we believed our human annotations would be more accurate than the training data in that case, as the training data was likely to contain mislabeled accounts and outliers. Even though this increased the sample size, it decreased the accuracy estimations in our train-test split testing, which was likely due to our annotation accuracy. In the end we decided to exclude them, but we included the .py file in the repository for the sake of completeness. This may have been due to some human error and the lack of certain categories such as Politics and Religion, where certain accounts didn’t fit any of the given categories and we were forced to mark them as “Health and Lifestyle”, as that seemed to be the broadest category.


For the regression step, we created a feature called reach_like_count, which by using the timestamp data, found the 4 posts before and after it, taking the log of their like counts, averaging them, and exponentiating back, taking the average in log space helps lower the effect of outliers and reduces the disparity between unpopular people and extremely popular influencers. Guessing a posts like count as this feature was so accurate (0.43 log MSE avg) that we were unable to beat it using machine learning models (XGBoost was too hard to tune; we couldn’t improve the neural network enough to beat our current setup although it was the model we used for round 1 etc.), most of them had a higher log MSE and while trying them all, we found out that random forest performed similar to it, but allowed us to have machine learning model and more complex learning. We used average like count, average comment count, follower count and comments count for our predictions using the random forest. We also created comment_ratio and comment_delta features, but they were later scrapped due to them decreasing the accuracy when included. We later played around with the random forests hyperparameters by trial and error (GridSearchCV would have been better in hindsight) and settled on the ones we currently have, as they gave us the best validation accuracies in our 5 fold cross validation. We performed cross validation by splitting the training set into training and test sets. To mimic Onur Hoca’s test set, for the test set we took at most one post from each user to form the test set. In both tasks, we gave immense importance to preventing data leakage, making sure to do feature engineering in each fold after the train-test separation and making sure to only populate these new features using training data.
Results of our own testing:


Confusion Matrix for the Classification:


![image](https://github.com/user-attachments/assets/db7df959-913f-498c-9b8e-7a33642a9e75)


Graph of Predicted Likes to Actual Likes for the 5th fold:


![image](https://github.com/user-attachments/assets/8959a7ba-faa4-4f09-abdb-c76cf07f3b05)


Team contributions:


During the first round we worked collaboratively, but after the first round due to the nature of the project we decided to work individually and submit the results of the models we believed to be the most accurate, then collaboratively tried improving those by passing each other ideas.


Deniz: BERTurk implementation (classification, 1st round and onwards), neural network implementation (regression, 1st round 0.74 log MSE), random forest implementation (regression, 3rd round 0.43 log MSE according to our testing), feature engineering all-around


Özgür: Initial Naive Bayes optimization (classification, 1st round, unused due to better model existing), LightGBM implementation (regression, 3rd round unused due to better model existing), addition of feature ((avg like count/avg comment count per user)* comment count per post) (unused since it could not decrease the error)


Berke: Zeyrek library lemmatization (classification, unused due to speed), average like count as the prediction (regression, 2nd round), linear regression (regression, 3rd round, unused due to better model existing)


Utku: Neural network + random forest implementation (regression, 2nd round, unused  due to inefficiency+data leakage), minor recommendations towards the final product of 2nd and 3rd round like changing some variables/feature engineering.


Alp: Initial Naive Bayes optimization (classification, 1st round, unused due to better model existing), optimization/revision of the code between the 2nd and 3rd rounds


