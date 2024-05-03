import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data =pd.read_csv("C://Users/LENOVO/Documents/dataset/Country Wise Airport.csv")
data

subset_data = data.head(5)
colors = ["#6495ED", "#1E90FF", "#00BFFF", "#87CEFA", "#B0E0E6"]
sns.barplot(x="Country", y="2014_Chennai_(Airport)", palette=colors, data = subset_data)
plt.show()

subset_data = data.head(8)
colors = ['blue', 'green', 'red', 'orange']
labels=['Canada', 'USA', 'Argentina','Brazil','Mexico', 'Austria', 'Belgium', 'Denmark']
plt.pie(subset_data, labels=labels, autopct='%1.1f%%', colors = colors)
plt.title("pie chart")
plt.show()

sub_data=data.head(8)
x=sub_data['country']
y1=sub_data['2014_Delhi_(Airport)']
y2=sub_data['2014_Mumbai_(Airport)']
y3=sub_data['2014_Chennai_(Airport)']
sns.lineplot(x=x, y=y1, color='blue', marker='o', label='Delhi')
sns.lineplot(x=x, y=y2, color='green', marker='o', markersize=8, label='Mumbai', )
sns.lineplot(x=x, y=y3, color='red', marker='o', label='Chennai')
plt.title('Line plot')
plt.xlabel('Country')
plt.ylabel('Average')
plt.show()

hist_data = data.loc [1:30, ['2020_Chennai_(Airport)']]
sns.histplot(hist_data, bins=20, kde=True, color='skyblue')
plt.xlabel('2020_Chennai_(Airport)')
plt.ylabel('Tourist (Average)')
plt.title('Tourist visited chennai (Average) 2020')
plt.show()

