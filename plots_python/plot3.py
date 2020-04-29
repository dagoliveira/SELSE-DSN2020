import pandas as pd
import matplotlib.pylab as plt
import numpy as np

df = pd.read_csv('data3.csv', delimiter=',')


#red: c00000
#blue: 0070c0

# Numbers of pairs of bars you want
N = 8

# Data on X-axis

# Position of bars on x-axis
ind = np.arange(N)

# Figure size
plt.figure(figsize=(10,5))
plt.rcParams.update({'font.size': 12})

# Width of a bar
width = 0.3

# Plotting
plt.bar(ind + 0*width, df['SDC_R'], width, label='SDC', color='#c00000', edgecolor='black')
plt.bar(ind + 1*width + 0.1, df['DUE_R'], width, label='DUE', color='#0070c0', edgecolor='black')
plt.text(ind[-1] + 0.25 , 0.1, 'NA')

plt.ylabel('Cross section ratio [ High energy / Thermal ]')
#plt.title('Here goes title of the plot')

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks((ind + width - 0.1), df['Device'])

# Finding the best position for legends and putting it
plt.legend(loc='best')
#plt.show()
plt.savefig('ratio.pdf')
plt.savefig('ratio.png')
