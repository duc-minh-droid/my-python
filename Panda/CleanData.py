import pandas as pd

csv = pd.read_csv('/Users/ducminh/Documents/GitHub/my-python/python/Panda/dirtydata.csv')

# dropna() returns a copy of the csv
new_csv = csv.dropna()
# pass parameter inplace=True to change the original csv

# fillna() remove every Na value with the value 130 (the row containing the Na values)
# new_csv.fillna(130, inplace=True)
new_csv['Calories'].fillna(130, inplace=True)
# mean() returns the average as a dataframe or a number
x = new_csv['Calories'].mean(axis=0, skipna=True)
new_csv['Calories'].fillna(x, inplace=True)
# mode() returns the most frequent appeared number in the dataframe
x = new_csv['Calories'].mode()[0]
# meadian() sorts the list and returns the middle number
x = new_csv['Calories'].median()

# pd.to_datetime() returns the the dataframe containing the fixed dataframe
new_csv['Date'] = pd.to_datetime(new_csv['Date'])

# remove NaT value
new_csv.dropna(subset=['Date'], inplace = True)

for x in new_csv.index:
    if new_csv.loc[x, 'Duration'] > 120:
        new_csv.loc[x, 'Duration'] = 120
        # or directly remove the row
        new_csv.drop(x, inplace = True)
        # pass the row and inplace for modifying original dataframe

# returns a dataframe containing the boolean whether the row is duplicated
print(new_csv.duplicated())

# removing duplicate
new_csv.drop_duplicates(inplace = True)




































