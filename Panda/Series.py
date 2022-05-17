import pandas as pd

# A series is a column in the table

# Create a series
srs = [[1,2], 2, 3]
srs = pd.Series(srs, index=['first','mid','last'])

print(srs)

print(srs['first'][1])

srs = {'day 1': 'exercise', 'day 2': 'coding', 'day 3': 'miss her'}
srs = pd.Series(srs)

print(srs)

# Geting data only in day 1 and 2
srs = pd.Series(srs, index=['day 1', 'day 2'])
print(srs)

# DataFrame() for multidimensional data
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
mydata = pd.DataFrame(data)
print(mydata)

# loc() pass an index returns a row
print(mydata.loc[0])
# Getting data in row 1 and 2
print(mydata.loc[[0, 1]])

csv = pd.read_csv('/Users/ducminh/Documents/GitHub/my-python/python/Panda/dirtydata.csv')
print(csv)
# to_string() returns the whole csv
print(csv.head(10)) # print the first 10 rows

print(pd.options.display.max_rows) 















