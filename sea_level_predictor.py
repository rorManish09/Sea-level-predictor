import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    # Create scatter plot
    fig,ax = plt.subplots(figsize = (10,6))

    plt.scatter(x,y)
    # Create first line of best fit
    res_line1 = linregress(x,y)

    lineX = np.arange(1880,2051,1)

    lineY =  res_line1.slope*lineX + res_line1.intercept

    plt.plot(lineX,lineY)

    # Create second line of best fit

    year_2000 = df[df['Year']>=2000]

    x2 = year_2000['Year']
    y2 = year_2000['CSIRO Adjusted Sea Level']

    res_line2 = linregress(x2,y2)

    lineX2 =np.arange(2000,2051,1)

    lineY2 = res_line2.slope*lineX2 + res_line2.intercept

    plt.plot(lineX2,lineY2)

    # Add labels and title

    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()