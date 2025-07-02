import pandas as pd
data=pd.read_csv("../../Data/fake_news_dataset.csv")
data['label']=data['label'].map({'fake':0,'real':1})
# dropping the use columns 
# for this project i  am using text and title as feature so both only used other thing is dropped
data=data.drop(['date','source','author','category'],axis=1)
data.to_csv("../../Data/fake_news_dataset.csv" ,index=False)