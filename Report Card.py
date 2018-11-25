
# coding: utf-8

# # Backend Assessment

# In this assessment, you will write a script to generate a text file containing the “report card” of all students in the
# database.
# You will be given an example input and an example output. Your program should be able to handle different inputs
# of various sizes. Your program 

# In[1]:


## Inputs


# In[2]:


## Import courses, students and tests csvs using pandas read_csv


# In[3]:


import pandas as pd
import numpy as np

courses = pd.read_csv("C:/Users/warin/Desktop/Data Analysis Portfolio/backend-assessment/courses.csv")

courses.head()


# In[4]:


students = pd.read_csv("C:/Users/warin/Desktop/Data Analysis Portfolio/backend-assessment/students.csv")

students.head()


# In[5]:


marks = pd.read_csv("C:/Users/warin/Desktop/Data Analysis Portfolio/backend-assessment/marks.csv")

marks.head()


# In[6]:


tests = pd.read_csv("C:/Users/warin/Desktop/Data Analysis Portfolio/backend-assessment/tests.csv")

tests.head()


# In[7]:


# Generate a report card for each student
# Merge data sets into one

df = pd.merge(tests, courses)
df2 = pd.merge(marks, df)
df2.head(100)
df3 = pd.merge(df2, students, on='id')
df3.head(100)

df3['Weighted_mark'] = df3.mark*df3.weight / 100
df3.head(100)


# In[8]:


df4 = df3.groupby(['id', 'course_id'], as_index=False).sum()


# In[15]:


df5 = df4.groupby(['id', 'course_id'], as_index=False).sum()
df5.groupby(['id'], as_index=False).mean()
df5.drop(['test_id', 'mark', 'weight'], axis=1, inplace=True)
df5 = pd.merge(df5, courses)
df5 = pd.merge(df5, students, on='id')
df5


# In[17]:


df6 = df5.groupby(['id'], as_index=False).mean()
df6.drop(['course_id'], axis=1, inplace=True)
df6 = pd.merge(df6, students, on='id')
df6


# In[36]:


j = 0
i = 0
while df6.id[j] <= 3:
    print('Student Id:', df6.id[j], ',', 'name:', df6.name[j], '\n',
          'Total Average:', df6.Weighted_mark[j],'%', '\n')
    while df5.id[i] == df6.id[j]:
        grade = 0
        grade += df5.Weighted_mark[i]
        print('     Course:', df5.name_x[i], 'Teacher:', df5.teacher[i], '\n', '     Final Grade:', grade,'%', '\n')
        i += 1
    j += 1

