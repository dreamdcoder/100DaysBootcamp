import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")






#TODO 1. Create a dictionary in this format: #{"A": "Alfa", "B": "Bravo"}

nato_dict ={row.letter:row.code for idx,row in nato_df.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a Word")
code_list = [value  for i in word for key,value in nato_dict.items() if i.upper()==key]

print(code_list)

