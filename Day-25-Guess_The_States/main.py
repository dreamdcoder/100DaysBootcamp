import pandas as pd

df = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
pd.set_option("display.max_columns",150)

new_df = df["Primary Fur Color"].value_counts().to_frame()

new_df.to_csv("output.csv")

print (new_df)
