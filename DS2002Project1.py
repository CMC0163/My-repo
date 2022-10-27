#!/usr/bin/env python
# coding: utf-8

# # DS 2002 Project 1
# ### Mianchen Cao 
# ### mc7sq

# ### Dataset:
# ##### Used the social network ads dataset downloaded from Kaggle which concludes User ID, Gender, Age, Estimated Salary, and Purchased (represented by 1s and 0s, 1 represents purchased). 
# ##### Source: https://www.kaggle.com/datasets/micheldc55/social-network-ads
# 
# ### Objectives:
# 1. Read in the local CSV file
# 2. Use Estimated Salary to get a new column with 1s and 0s representing if the user's salary is above average or not: 1 represents above average
# 3. Subset the original dataset into two datasets by if the user purchased item or not
# 4. Compare the average age, average estimated salary, and the ratio of people with above avg salary and number of users in each dataset
# 5. Write the above 6 numbers into a new dataframe
# 6. Convert the modified original CSV file, the two subset dataframes, and the result dataframe into JSON, SQL, or CVS by the will of the user
# 7. Summary the results

# In[102]:


import pandas as pd
import numpy as np
from sqlalchemy import create_engine


# In[103]:


df = pd.read_csv('/Users/CMC/Desktop/Fall 2022/DS 2002/Project1/Social_Network_Ads.csv')


# In[104]:


avg = sum(df['EstimatedSalary'])/len(df['EstimatedSalary'])


# In[105]:


df['AboveAvgSalary'] = df['EstimatedSalary'].apply(lambda x: int(1) if x >= avg else int(0))


# In[106]:


df1 = df[df['Purchased'] == 1]
df2 = df[df['Purchased'] == 0]


# In[107]:


avgAgePurchased = round(sum(df1['Age'])/len(df1['Age']),2)
avgAgeNotPurchased = round(sum(df2['Age'])/len(df2['Age']),2)
avgSalaryPurchased = round(sum(df1['EstimatedSalary'])/len(df1['EstimatedSalary']),2)
avgSalaryNotPurchased = round(sum(df2['EstimatedSalary'])/len(df2['EstimatedSalary']),2)
pctAboveSalaryPurchased = round((len(df1[df1['AboveAvgSalary'] == 1])/len(df1['Purchased']))*100,2)
pctAboveSalaryNotPurchased = round((len(df2[df2['AboveAvgSalary'] == 1])/len(df2['Purchased']))*100,2)


# In[108]:


data = [['Average Age', avgAgePurchased, avgAgeNotPurchased],['Average Salary', avgSalaryPurchased, avgSalaryNotPurchased],['Percentage of Above Avg Salary', pctAboveSalaryPurchased, pctAboveSalaryNotPurchased]]


# In[109]:


result = pd.DataFrame(data, columns = ['Variables', 'Purchased', 'Not Purchased'])


# In[113]:


df


# In[114]:


df1


# In[115]:


df2


# In[116]:


result


# In[121]:


df.info()


# In[123]:


df1.info()


# In[124]:


df2.info()


# In[122]:


result.info()


# In[118]:


mytype = input('Choose a file type for the above dataframes to be exported')


# In[120]:


mytype = mytype.lower()
if mytype == 'json':
    df.to_json(r'/Users/CMC/Desktop/Fall 2022/DS 2002/Project1/Social_Network_Ads_Modified.json')
    df1.to_json(r'/Users/CMC/Desktop/Fall 2022/DS 2002/Project1/Purchased.json')
    df2.to_json(r'/Users/CMC/Desktop/Fall 2022/DS 2002/Project1/Not_Purchased.json')
    result.to_json(r'/Users/CMC/Desktop/Fall 2022/DS 2002/Project1/Results.json')
elif mytype == 'sql':
    engine = create_engine('sqlite://', echo=False)
    df.to_sql('Social_Network_Ads_Modified', con=engine)
    df1.to_sql('Purchased', con=engine)
    df2.to_sql('Not_Purchased', con=engine)
    result.to_sql('Results', con=engine)
    print("Social_Network_Ads_Modified")
    print(engine.execute("SELECT * FROM Social_Network_Ads_Modified").fetchall())
    print('')
    print("Purchased")
    print(engine.execute("SELECT * FROM Purchased").fetchall())
    print('')
    print("Not_Purchased")
    print(engine.execute("SELECT * FROM Not_Purchased").fetchall())
    print('')
    print("Result")
    print(engine.execute("SELECT * FROM Results").fetchall())
    print('')
elif mytype == 'csv':
    df.to_csv(r'/Users/CMC/Desktop/Fall 2022/DS 2002/Project1/Social_Network_Ads_Modified.csv')
    df1.to_csv(r'/Users/CMC/Desktop/Fall 2022/DS 2002/Project1/Purchased.csv')
    df2.to_csv(r'/Users/CMC/Desktop/Fall 2022/DS 2002/Project1/Not_Purchased.csv')
    result.to_csv(r'/Users/CMC/Desktop/Fall 2022/DS 2002/Project1/Results.csv')


# ### Results:
# 1. The original dataset has 5 columns and 500 rows
# 2. The modified original dataset has 6 columns and 500 rows
# 3. The Purchased dataset has 6 columns and 143 rows
# 4. The Not Purchased dataset has 6 columns and 257 rows
# 5. The Result dataset has 3 colums and 3 rows
# 6. The average age of users who purchased is 46.39, which is higher than that of uses who didn't purchase: 32.79
# 7. The average salary of users who purchased is \\$86,272.73, which is higher than that of users who didn't purchase: \\$60,544.75
# 8. The percentage of above-avg-salary users who purchased is 67.13%, which is higher than that of users who didn't purchase: 40.86%

# In[ ]:




