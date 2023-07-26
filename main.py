from main import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_json('inf.json')
df.head()
sns.boxplot(x='floor_max', y='name', data=df[:5], hue='min')
plt.savefig('plots/plot_11.png')





def draw_plots():
   pass
print(draw_plots())