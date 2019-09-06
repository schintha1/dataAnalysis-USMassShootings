import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import seaborn as sns
color = sns.color_palette()

from subprocess import check_output

# Any results you write to the current directory are saved as output.

mass_shooting = pd.read_csv("shootings.csv", encoding = "ISO-8859-1", 
                            parse_dates=["Date"])

mass_shooting['Prior signs of mental health issues'].replace(['Unknown','unknown','Unclear '],
                        ['Unclear','Unclear','Unclear'],inplace=True)
mass_shooting['Prior signs of mental health issues'].unique()
day_of_week = mass_shooting['Prior signs of mental health issues'].value_counts()  
plt.figure(figsize=(15,8))  
sns.barplot(day_of_week.index, day_of_week.values, alpha=0.7, color=color[3])

plt.xlabel('Mental State', fontsize=12)  # fontsize and label
plt.ylabel('Number of Attacks', fontsize=12)  # fontsize and label
plt.title('Number of Attacks by Mental State', fontsize=18) # fontsize and label
plt.show()

