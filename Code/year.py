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

mass_shooting['Year'] = mass_shooting['Date'].dt.year     # seperates years from date 
year = mass_shooting['Year'].value_counts()           # counts values according to specific year
plt.figure(figsize=(12,6))                                # decides size of plot
sns.barplot(year.index, year.values, alpha=0.7, color=color[3])
"""
Color
0 Blue
1 Orange
2 Green
3 Red
"""
plt.xticks(rotation='vertical')  # makes x axis values vrertical
plt.xlabel('Year of Shooting', fontsize=12)  # fontsize and label
plt.ylabel('Number of Attacks', fontsize=12)  # fontsize and label
plt.title('Number of Attacks per Year', fontsize=18) # fontsize and label
plt.show()

