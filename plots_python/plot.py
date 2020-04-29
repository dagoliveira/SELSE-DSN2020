import pandas as pd
import matplotlib.pylab as plt
import numpy as np

df = pd.read_csv('data.csv', delimiter=';')


#red: c00000
#blue: 0070c0

# Numbers of pairs of bars you want
N = 8

# Data on X-axis

# Position of bars on x-axis
ind = np.arange(N)

# Figure size
plt.figure(figsize=(10,5))

# Width of a bar
width = 0.2

# Plotting
plt.bar(ind + 0*width, df['SDC_HIGH'], width, label='High Energy SDC', color='#c00000', edgecolor='black')
plt.bar(ind + 1*width, df['SDC_Thermal'], width, label='Thermal SDC', color='#c00000', hatch="///", edgecolor='black')
plt.bar(ind + 2*width, df['DUE_HIGH'], width, label='High Energy DUE', color='#0070c0', edgecolor='black')
plt.bar(ind + 3*width, df['DUE_Thermal'], width, label='Thermal DUE', color='#0070c0', hatch="\\\\\\", edgecolor='black')

plt.ylabel('Normalized cross section [a.u.]')
#plt.title('Here goes title of the plot')

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks((ind + 1.5*width), df['Device'])

# Finding the best position for legends and putting it
plt.legend(loc='best')
#plt.show()
plt.savefig('averages.pdf')
plt.savefig('averages.png')
