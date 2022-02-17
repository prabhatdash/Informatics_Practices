
#Aim:Create a data frame based on ecommerce data and generate descriptive statistics (mean, median,mode, quartile, and variance)

#Code:

import pandas as pd
import numpy as np

df=pd.read_csv("0_ecom_data.csv")
mean_price=df['Sale Price'].mean()
median_price=df['Sale Price'].median()
mode_price=df['Sale Price'].mode()
print("Mean of Price:",mean_price)
print("Median of Price:",median_price)
print("Mode of Price:","\n",mode_price)
