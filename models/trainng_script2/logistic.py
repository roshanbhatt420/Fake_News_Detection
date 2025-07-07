# importing the radndomo forest
from sklearn.linear_model import LogisticRegression
#  import  functio for the spillting the data into the traning and testing
from sklearn.model_selection import train_test_split
# vectorizing function
from vetorization_function import vectorWord
# importing the other dependecies
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import os 
# for witing in the file 
import json

import seaborn as sns
import matplotlib.pyplot as plt


# making sure we have model report directory
os.makedirs("modelreport",exist_ok=True)


# getting data from the traning_data.csv

data=pd.read_csv("../../Data/Training_data.csv")
X=vectorWord(data["clean_text"])
Y=data["label"]

# spilting the data into the two set

x_train,x_test,y_train,y_test=train_test_split(X,Y,random_state=42,test_size=0.2)


# random forest classifiers
rnd_clf=LogisticRegression(max_iter=1000)
rnd_clf.fit(x_train,y_train)
y_predi=rnd_clf.predict(x_test)

# making report
report=classification_report(y_test,y_predi,target_names=['fake','True'],output_dict=True)

# writing in the file

with open("modelreport/report4.txt","w") as f:
    json.dump(report,f)

# making the confusion matrix
cm=confusion_matrix(y_test,y_predi)

cm_df = pd.DataFrame(cm, index=['True', 'Fake'], columns=['True', 'Fake'])
plt.figure(figsize=(10, 7))
sns.heatmap(cm_df, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.savefig("modelreport/confusion_matrix4.png")




