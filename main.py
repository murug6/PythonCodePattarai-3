#importing libs
import pandas as pd
import numpy as np

#### this is the first block

# df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
# print(df)


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data) # to create dataframe from dictionary
print(df)

# print(df.at[1, 'attempts']) # to print 1st row and '' column
# print(df.loc[1])  # to print 1st row
# print(df.iat[1, 2]) # to print 1st row 2nd column value

# # selecting single column
# print(df['name']) # this returns a single column
# subsetDF = df[['name','score']] # this returns a data frame
# print(subsetDF)
# Using filter conditions
# print(df['name'] == 'Michael')
# print(df[df['name'] == 'Michael'])
print(df[df['score'] == df['score'].max()])

# #selecting max & min of a column
# print(df['score'].max())
# print(df['score'].min())
#
# # head and tails
# print(df.head(2))
# print(df.tail(2))
# # working with files
# # read
# titanic = pd.read_csv("data/titanic.csv")
# titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
#
# # write
# titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
# df.to_csv("./player.csv")