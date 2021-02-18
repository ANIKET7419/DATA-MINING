
#Import Pandas library
import pandas as pd

# Read the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user) in a data frame 'users'
print("Read the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user) in a data frame 'users'\n\n")
users=pd.read_table("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user",sep='|')

# Display the first 15 entries from 'users'
print("Display the first 15 entries from 'users'\n\n")

print(users.head(15))

# Display the last 10 entries from 'users'
print("Display the last 10 entries from 'users'\n\n")

print(users.tail(10))


# What is the number of observations in the dataset?
print("What is the number of observations in the dataset?\n\n")


print(len(users))

# What is the number of attributes in the dataset?
print("What is the number of attributes in the dataset?\n\n")

print(users.shape[1])


# How is the dataset indexed?
print("How is the dataset indexed?\n\n")

print(users.index)



# What is the data type of each column?
print("What is the data type of each column?\n\n")

print(users.dtypes)


# Print only the occupation column
print("Print only the occupation column\n\n")
print(users['occupation'])


# How many different occupations are in this dataset?
print("How many different occupations are in this dataset?\n\n")
print(users['occupation'].drop_duplicates().size)

#  Summarize the DataFrame.
print("Summarize the DataFrame.\n\n")
print(users.describe())


# Summarize only the occupation column
print("Summarize only the occupation column\n\n")
print(users['occupation'].describe())


# What is the mean age of users?
print(" What is the mean age of users?\n\n")
print(users['age'].mean())


# What is the mean age per occupation
print("What is the mean age per occupation\n\n")
print(users.groupby(by='occupation')['age'].mean())

# For each occupation, calculate the minimum and maximum ages
print("For each occupation, calculate the minimum and maximum ages\n\n")
print("--- MIN ---")
print(users.groupby(by='occupation')['age'].min())

print("--- MAX ---")
print(users.groupby(by='occupation')['age'].max())


# For each combination of occupation and gender, calculate the mean age
print("For each combination of occupation and gender, calculate the mean age\n\n")
print(users.groupby(by=['occupation','gender'])['age'].mean())
