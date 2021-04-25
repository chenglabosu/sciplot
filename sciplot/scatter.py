import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
import pickle

'''
color names

details see https://matplotlib.org/stable/gallery/color/named_colors.html

Frequently used:
Red:    pink, lightcoral, salmon, red, brown, firebrick, maroon, darkred
Yellow: yellow, gold, orange, darkorange
Blue:   cyan, skyblue, deepskyblue, steelblue, blue, mediumblue, navy
Purple: violet, purple, magenta

'''


SIZE1 = 24
SIZE2 = 20
SIZE3 = 16

plt.rc('font',family='serif')
plt.rc('axes',titlesize=SIZE1)
plt.rc('axes',titleweight='bold')
plt.rc('axes',labelsize=SIZE2)

plt.rc('xtick',labelsize=SIZE2)
plt.rc('ytick',labelsize=SIZE2)

plt.rc('legend',fontsize=SIZE3)
#plt.rc('legend',markerscale=1)
plt.rc('legend',borderpad=0.1)

#   Load Data
f = open('../data/rand_xy.pkl','rb')
[x,y] = pickle.load(f)
f.close()

matplotlib.rcParams['figure.dpi']=300
matplotlib.rcParams['savefig.dpi']=300


#   Plot figures
fig = plt.figure()
ax = fig.add_subplot(111)

ax.scatter(x,y,label='data1')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')


#   Set the boarder of a frame
ax.spines['right'].set_visible(False) 
ax.spines['top'].set_visible(False)

#   Set ticks manually
#ax.set_xticks(np.linspace(0,10,100))
#ax.set_yticks(np.linspace(0,10,100))

ax.legend(loc=(0.7,0.9))
plt.tight_layout()

plt.savefig('test.png')
