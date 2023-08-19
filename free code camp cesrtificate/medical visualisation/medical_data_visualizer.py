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
  df_cat =pd.melt(df, id_vars='cardio', value_vars=x, var_name='feature')

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  df_cat = df_cat.groupby(['cardio', 'feature', 'value']).size().reset_index(name='count')

  # Draw the catplot with 'sns.catplot()'
  sns.set(style='whitegrid')
  sns.catplot(
    data=df_cat,
    x='feature',
    y='count',
    hue='value',
    col='cardio',
    kind='bar',
    height=5,
    aspect=0.8
)

  # Get the figure for the output
  fig = plt.show()

  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig



# Draw Heat Map
def draw_heat_map():
  # Clean the data
  # Clean the data
    height_percentile_2_5 = df['height'].quantile(0.025)
    height_percentile_97_5 = df['height'].quantile(0.975)

    weight_percentile_2_5 = df['weight'].quantile(0.025)
    weight_percentile_97_5 = df['weight'].quantile(0.975)

    condition_ap = df['ap_lo'] <= df['ap_hi']
    condition_height = (df['height'] >= height_percentile_2_5) & (df['height'] <= height_percentile_97_5)
    condition_weight = (df['weight'] >= weight_percentile_2_5) & (df['weight'] <= weight_percentile_97_5)

    df_heat = df[condition_ap & condition_height & condition_weight]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, cmap='coolwarm', annot=True, fmt=".2f", mask=mask, ax=ax)
    ax.set_title('Correlation Matrix')
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    plt.show()
    return fig



