import pandas as pd
import matplotlib.pylab as plt
import numpy as np

df = pd.read_csv('data2.csv', delimiter=',')


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
width = 0.3

# Plotting
plt.bar(ind + 0*width, df['SDC_H_PER'], width, label='High Energy SDC', color='#c00000', edgecolor='black')
plt.bar(ind + 0*width, df['SDC_T_PER'], width, label='Thermal SDC', color='#c00000', hatch="///", edgecolor='black', bottom=df['SDC_H_PER'])
plt.bar(ind + 1*width + 0.1, df['DUE_H_PER'], width, label='High Energy DUE', color='#0070c0', edgecolor='black')
plt.bar(ind + 1*width + 0.1, df['DUE_T_PER'], width, label='Thermal DUE', color='#0070c0', hatch="\\\\\\", edgecolor='black', bottom=df['DUE_H_PER'])

plt.ylabel('Average cross section contribution [%]')
#plt.title('Here goes title of the plot')

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks((ind + 0.5*width +0.05), df['Device'])

# Finding the best position for legends and putting it
plt.legend(loc='best')
#plt.show()
plt.savefig('averages2.pdf')
plt.savefig('averages2.png')
