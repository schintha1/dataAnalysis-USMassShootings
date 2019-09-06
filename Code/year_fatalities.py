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

tot = mass_shooting[['Year', 'Injured', 'Fatalities']].groupby('Year').sum()
tot.plot.bar(figsize=(15,8))
plt.ylabel('Number of Victims', fontsize=12)
plt.title('Fatalities vs Injuries per Year', fontsize=18)
plt.show()
