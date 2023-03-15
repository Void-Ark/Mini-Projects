import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
  plt.figure(figsize = (10, 6))

    # Create first line of best fit
  X = df['Year']
  Y = df['CSIRO Adjusted Sea Level']
  plt.scatter(X, Y)
  slope, intercept, _, _, _ = linregress(X, Y)
  X_pred = range(1880, 2051)
  Y_pred = (slope * X_pred) + intercept
  plt.plot(X_pred, Y_pred)

    # Create second line of best fit
  X_new = df[df['Year'] >= 2000]['Year']
  Y_new = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
  slope_n, intercept_n, _, _, _ = linregress(X_new, Y_new)
  Xn_pred = range(2000, 2051)
  Yn_pred = (slope_n * Xn_pred) + intercept_n
  plt.plot(Xn_pred, Yn_pred)

    # Add labels and title

  plt.xlabel('Year')
  plt.xticks(range(1850, 2076, 25))
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()

