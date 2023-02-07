import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = (df["weight"]/ (df["height"] / 100) ** 2).apply(lambda v:1 if v > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.cholesterol = [0 if x == 1 else 1 for x in df.cholesterol]

df.gluc = [0 if x == 1 else 1 for x in df.gluc]

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars="cardio", value_vars=["cholesterol", "overweight", "gluc", "alco", "active", "smoke"])
    df_cat["total"] = 1

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index=False).count()

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot( x="variable",  y="total", col="cardio", hue="value",  kind="bar", data=df_cat )

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():

    # Clean the data
    df_heat = df[ (df['ap_lo'] <= df['ap_hi']) &
                  (df['weight'] >= df['weight'].quantile(0.025)) &
                  (df['weight'] <= df['weight'].quantile(0.975)) &
                  (df['height'] >= df['height'].quantile(0.025)) &
                  (df['height'] <= df['height'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(
        corr,
        mask = mask,
        square= True,
        annot = True,
        linewidths = 0.5,
        fmt = '.1f',
        center = 0,
        vmin = -0.1,
        vmax = 0.25,
        cbar_kws={
            'shrink': .45,
            'format': '%.2f'
        })

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig