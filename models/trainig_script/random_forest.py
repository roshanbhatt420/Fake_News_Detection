# importing the radndomo forest
from sklearn.ensemble import  RandomForestClassifier
#  import  functio for the spillting the data into the traning and testing
from sklearn.model_selection import train_test_split
# vectorizing function
from Vectorization.vectorization_function import vectorWord
# importing the other dependecies
import pandas as pd
import numpy as np

# getting data from the traning_data.csv

data=pd.read_csv("../../Data/Training_data.csv")
X=vectorWord(data["clean_text"])
Y=data["label"]

# spilting the data into the two set

x_train,x_test,y_train,y_test=train_test_split(X,Y,random_state=42,test_size=0.2)
