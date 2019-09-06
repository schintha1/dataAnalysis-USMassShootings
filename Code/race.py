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
mass_shooting['Race'].fillna('0', inplace=True)
mass_shooting.Race.replace(['0','white', 'black', 'Some other race', 'unclear','White ','Black American or African American/Unknown','White American or European American/Some other Race','Asian American/Some other race','Native American','White American or European American','Black American or African American','Asian American','Native American or Alaska Native','Two or more races'], 
                           ['Unknown','White', 'Black', 'Other','Unknown','White','Black American or African American','White American or European American','Asian American','Native American or Alaska Native','White','Black','Asian','Natives','Other'], inplace=True)
mass_shooting['Race'].unique()
day_of_week = mass_shooting['Race'].value_counts()  
plt.figure(figsize=(15,8))  
sns.barplot(day_of_week.index, day_of_week.values, alpha=0.7, color=color[3])

plt.xlabel('Year of Shooting', fontsize=12)  # fontsize and label
plt.ylabel('Number of Attacks', fontsize=12)  # fontsize and label
plt.title('Number of Attacks per Year', fontsize=18) # fontsize and label
plt.show()
