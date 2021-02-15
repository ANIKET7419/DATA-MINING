
#Import Pandas library
import pandas as pd

# Read the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user) in a data frame 'users'
users=pd.read_table("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user",sep='|')

# Display the first 15 entries from 'users'

print(users.head(15))

# Display the last 10 entries from 'users'
print(users.tail(10))


# What is the number of observations in the dataset?

print(len(users))

# What is the number of attributes in the dataset?
print(users.shape[1])


# How is the dataset indexed?
print(users.index)



# What is the data type of each column?

print(users.dtypes)


# Print only the occupation column
print(users['occupation'])


# How many different occupations are in this dataset?

print(users['occupation'].drop_duplicates().size)

#  Summarize the DataFrame.

print(users.describe())


