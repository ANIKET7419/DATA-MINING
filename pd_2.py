import pandas as pd
import numpy as np
data = pd.DataFrame( {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']},index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

# Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).

print(data.loc[(data.score>=15 ) & (data.score<=20)])


# Write a Pandas program to add a column named "column1" in the sixth position of the "coalpublic2013.xlsx" excel sheet and fill it with NaN values.
data=pd.read_excel('/home/ARTHAKUR/Downloads/coalpublic2013.xlsx')
data['column1']=np.nan
data.to_excel('/home/ARTHAKUR/Downloads/coalpublic2013.xlsx')

# Write a Pandas program to import given excel data (coalpublic2013.xlsx ) into a dataframe and find details where "Mine Name" starts with "P"

print(data.loc[data['Mine_Name'].str.startswith('P',na=False)])

# Write a Pandas program to import given excel data (employee.xlsx ) into a Pandas dataframe and find a list of employees where hire_date> 01-01-07.

data=pd.read_csv('/home/ARTHAKUR/Downloads/employee.csv')
data['hire_date']=pd.to_datetime(data['hire_date'])
print(data.loc[data['hire_date']>'01-01-2007'])



#  Find the average mileage of each car making company

data=pd.read_csv('/home/ARTHAKUR/Downloads/automobile.csv')
data.drop(columns='index',inplace=True)
print(data.groupby('company').agg({'average-mileage':'mean'}))



# Find the most expensive car company name
max_=data.price.max()
print(data.loc[data.price==max_]['company'])







