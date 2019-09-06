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
mass_shooting['City'] = mass_shooting['Location'].str.rpartition(',')[0]
mass_shooting['State'] = mass_shooting['Location'].str.rpartition(', ')[2]
g = mass_shooting['State'].unique()
"""mass_shooting['State'].replace(['','NV','CA','PA','WA','D.C.','LA'],
                        ['Unknown','Nevada','California','Pennysylvania','Washington','Washington D.C.','Louisiana'],inplace=True)
mass_shooting['State'].unique()"""

f=['Maryland','AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY',]
g = np.append(g,f)
mass_shooting['State'].value_counts('')
g = np.delete(g,10)
ll = mass_shooting['State']
day_of_week = ll.value_counts()  
plt.figure(figsize=(15,8))  
sns.barplot(day_of_week.index[1:], day_of_week.values[1:], alpha=0.7, color=color[3])

plt.xticks(rotation='vertical')  # makes x axis values vrertical
plt.xlabel('State', fontsize=12)  # fontsize and label
plt.ylabel('Number of Attacks', fontsize=12)  # fontsize and label
plt.title('Number of Attacks by State', fontsize=18) # fontsize and label
plt.show()
