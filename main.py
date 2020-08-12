import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns


## Load and clean dataset 
df = pd.read_csv('/kaggle/input/fortune-500-women-as-ceo-since-1970/women_in_fortune_500_as_ceo.csv', sep=';')
df.dropna(inplace=True)
df.drop(columns=['%Women'],inplace=True)
df=df.astype({'Year': 'int32','#Women': 'int32'})
df.columns = ['Year', 'Number_of_women']
df['Proportion_of_women']=df['Number_of_women']/500

## Plot figure
plt.figure(figsize=(15,4))
ax = plt.axes()
ax.set_facecolor("#001c3e")

plt.plot(df['Year'],df['Number_of_women'],color='#fcfcfc',linestyle=' ',marker='.')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()plt.figure(figsize=(15,4))
ax = plt.axes()
ax.set_facecolor("#001c3e")

plt.plot(df['Year'],df['Number_of_women'],color='#fcfcfc',linestyle=' ',marker='.')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()
