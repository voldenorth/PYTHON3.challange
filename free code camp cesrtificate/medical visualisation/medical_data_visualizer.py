import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
def bmi_result():
  bmi=(df['weight']/((df['height']/100)**2))
  result=[]
  for i in bmi:
    if i > 25:
      result.append(1)
    else:
      result.append(0)
  return result


df['overweight']=bmi_result()

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def Normalize(*args):
    normalized_values = []
    for i in args:
        if i <= 1:
            normalized_values.append(0)
        else:
            normalized_values.append(1)
    return normalized_values
a=df['cholesterol']
df['cholesterol']=Normalize(*a)
b=df['gluc']
df['gluc']=Normalize(*b)





# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  x=['cholesterol','gluc','smoke','alco','active','overweight']
  df_cat =pd.melt(df,id_vars='cardio',value_vars=x)

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  df_cat = df_cat.groupby('cardio')[x].size().reset_index(name='count')

  # Draw the catplot with 'sns.catplot()'
  a=sns.catplot(data=df_cat,x='cardio',y='count',hue=x)

  # Get the figure for the output
  fig = plt.show()

  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig



# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df = df[df['ap_lo'] <= df['ap_hi']]
  height_percentile_2_5 = df['height'].quantile(0.025)
  height_percentile_97_5 = df['height'].quantile(0.975)
  df = df[(df['height'] >= height_percentile_2_5) & (df['height'] <= height_percentile_97_5)]
  weight_percentile_2_5 = df['weight'].quantile(0.025)
  weight_percentile_97_5 = df['weight'].quantile(0.975)
  df = df[(df['weight'] >= weight_percentile_2_5) & (df['weight'] <= weight_percentile_97_5)]
  df_heat=df
  # Calculate the correlation matrix
  corr = df_heat.corr()

  # Generate a mask for the upper triangle
  mask = np.triu(np.ones_like(df_heat), k=0)

  # Set up the matplotlib figure
  fig, ax = plt.subplot(figsize=(11,9))

  cmap = sns.diverging_palette(230, 20, as_cmap=True)

  # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(corr, mask=mask, cmap=cmap,vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig
