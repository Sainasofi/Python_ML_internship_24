import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import os

auto = pd.read_csv("titanic.csv")
plt.figure(figsize=(10,6))
sns.barplot(x="pclass", y="survived", hue="sex", data=auto)
plt.title("Survival Rate by Class and Sex")
plt.xlabel("Passengerclass")
plt.ylabel("survival; rate")
print(plt.show())

sns.set(rc={"axes.facecolor":"#FFFFFF", "axes.grid":False, "xtick.labelsize":10, "ytick.labelsize":10})
plt.figure(figsize=(20,8))
plt.title("Fare vs Age")
plt.xlabel("Age")
plt.ylabel("Fare")
sns.lineplot(x=auto["age"], y=auto["fare"], color='r')
print(plt.show())

plt.figure(figsize=(20,8))
sns.lineplot(x=auto["age"], y=auto["survived"], linewidth=1.5, color='r', marker='o')
plt.title("Survival Rate by Age")
plt.xlabel("Age")
plt.ylabel("Survival Rate")
plt.show()

plt.figure(figsize=(20,8))
sns.lineplot(data=auto["age"],linewidth=1.5,label="Age")
sns.lineplot(data=auto["fare"],linewidth=1.5,label="fare")
plt.title("Fare by Age")
plt.ylabel("Age")
plt.xlabel("fare")
plt.show()

neww = pd.DataFrame({
    'Category': ['Average Age', 'Average Fare'],
    'Value': [auto['age'].mean(), auto['fare'].mean()]
})
sns.set(style="whitegrid")
plt.figure(figsize=(20,8))
sns.barplot(x='Category', y='Value', data=neww)
plt.title("Average Age and Fare")
plt.ylabel("Value")
plt.xlabel("Category")
plt.show()

