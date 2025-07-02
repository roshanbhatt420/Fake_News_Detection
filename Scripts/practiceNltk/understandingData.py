import pandas as pd
import numpy as np
import sklearn 
# reading the data
try:
    fake_data=pd.read_csv("../Data/Fake.csv")
    true_data=pd.read_csv("../Data/True.csv")
except FileNotFoundError:
    print("File not found ")
    exit()

# labeling the data
fake_data['label']=0
true_data['label']=1
# combining the datas

combined_data=pd.concat([fake_data, true_data],ignore_index=True)

# suffling the data  
cobined_data=combined_data.sample(frac=1).reset_index(drop=True)

# showing the first rows
print("Heads of Data:\n",combined_data.head())
# saving the combined data
combined_data.to_csv("../Data/Combined_data.csv")

# printing the success method
print("Data is creadted and suffeled successfully")
