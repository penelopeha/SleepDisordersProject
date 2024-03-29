# -*- coding: utf-8 -*-
"""Project2-SleepEDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uIg0GJ63h-6IXAXYcDMXubVP_7APL7BZ

# **Sleep Health and Lifestyle Dataset**
"""

#Load the required libraries
import pandas as pd
import numpy as np
import seaborn as sns

#Load the data
df = pd.read_csv('Sleep.csv')


#View the data
df.head()

"""## **Data Preparation**"""

# Get data types and check data counts
df.info()

df.isnull().sum()

# Remove columns that I will not use
df = df.drop(['Person ID', 'Blood Pressure'], axis=1)

# Separate categorical columns from numeric columns
cat_cols = df.select_dtypes(include=['object']).columns
num_cols = df.select_dtypes(include=np.number).columns.tolist()
print("Categorical Variables:")
print(cat_cols)
print("Numerical Variables:")
print(num_cols)

# Explore the Gender column
df['Gender'].unique()
sns.countplot(df['Gender'])

# Explore the Occupation column (11 occupations)
df['Occupation'].unique()
sns.countplot(df['Occupation'])

# Explore the BMI Category column
df['BMI Category'].unique()
sns.countplot(df['BMI Category'])

"""in this dataset, normal and normal Weight mean the same, must combine the data of these columns into a single column."""

df['BMI Category'] = df['BMI Category'].replace(['Normal', 'Normal Weight'], 'Normal Weight')
df

# Explore the BMI Category column
df['BMI Category'].unique()
sns.countplot(df['BMI Category'])

# Explore the Sleep Disorder Category column
df['Sleep Disorder'].unique()
sns.countplot(df['Sleep Disorder'])

"""# **Exploratory Data Analysis**"""

# obtain statistical information of the dataset
df.describe()

"""-The dataset contains records of 374 people from ages 27 to 59 years old. The average age of respondents is 42 years old.

-Respondents in the dataset sleep on average 7.13 hours with an average quality rating of 7.31 on a rating scale of 1 to 10 in which 1 is bad sleep and 10 is very good sleep.

-On average, respondents do 59 minutes of physical activity and walk 6,816 steps per day.

-The average stress rating of respondents is 5.38 on a rating scale from 1 to 10 in which 1 is low stress and 10 is very high stress.

# EDA Univariate Analysis
"""

import matplotlib.pyplot as plt

for col in num_cols:
    print(col)
    print('Skew :', round(df[col].skew(), 2))
    plt.figure(figsize = (15, 4))
    plt.subplot(1, 2, 1)
    df[col].hist(grid=False)
    plt.ylabel('count')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[col])
    plt.show()

"""Skewness tells us the directon of the outliers. A normal distribution has a value of 0, the closer to 0 the more normalized the data.

-If the skewness is between -0.5 and 0.5, the data are fairly symmetrical.  
-If the skewness is between -1 and – 0.5 or between 0.5 and 1, the data are moderately skewed.

-If the skewness is less than -1 or greater than 1, the data are highly skewed.

In this case, all columns, except Heart rate are fairly symetrical.

"""

sns.catplot(data=df, x="Gender", y="Quality of Sleep", hue="Gender", kind="box")
    sns.catplot(data=df, x="BMI Category", y="Quality of Sleep", hue="BMI Category", kind="box")
    sns.catplot(data=df, x="Sleep Disorder", y="Quality of Sleep", hue="Sleep Disorder", kind="box")

"""##Dataset columns
 0 -  Person ID - Identifier for each individual  

 1 -  Gender - Female / Male  

 2 - Age - Age of the person in years

 3 - Occupation - Profession of the person

 4 - Sleep Duration - Number of hours the person sleeps per day

 5 -  Quality of Sleep - Rating of the quality of sleep from 1 to 10 in which 1 is bad sleep and 10 is very good sleep

 6 -  Physical Activity Level - Number of daily minutes of pyhsical activity

 7 -  Stress Level - Rating of stress level experienced from 1 to 10, in which 1 is low stress and 10 is very high stress  

 8 -  BMI Category - BMI Category of the person

 9 -  Blood Pressure - Blood pressure of the person indicated as systolic over diastolic presure

 10 - Heart Rate - Resting heart rate of the person in beats per minute

 11 - Daily Steps - Number of steps the person takes per day  

 12 - Sleep Disorder - Presence or absence of a sleep disorder in the person

 Dataset: https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset
"""