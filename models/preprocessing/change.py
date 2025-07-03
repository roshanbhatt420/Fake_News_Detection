from preprocessing import Preprocessing_module
import pandas as pd

# Read the dataset
df = pd.read_csv("../../Data/fake_news_dataset.csv")

# Apply preprocessing
df["clean_text"] = df.apply(lambda row: Preprocessing_module(row["title"], row["text"]), axis=1)

# Select only 'clean_text' and 'label'
new_data = df[["clean_text", "label"]]  

# Save to new CSV
new_data.to_csv("../../Data/Training_data.csv", index=False)  
