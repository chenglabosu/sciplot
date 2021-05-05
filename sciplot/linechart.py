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
'''
f = open('../data/cos.pkl','rb')
[x1,y1] = pickle.load(f)
f.close()
f = open('../data/sin.pkl','rb')
[x2,y2] = pickle.load(f)
f.close()
'''

matplotlib.rcParams['figure.dpi']=300
matplotlib.rcParams['savefig.dpi']=300


#   Plot figures
def create_subplot(xlabel='xlabel',ylabel='ylabel',rb=False,tb=False,xl=None,xh=None,yl=None,yh=None):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.spines['right'].set_visible(rb)
    ax.spines['top'].set_visible(tb)
    if xl!=None and xh!=None:
        ax.set_xlim([xl,xh])
    if yl!=None and yh!=None:
        ax.set_ylim([yl,yh])
    return fig,ax


def plot(ax,x,y,label='data1',color='steelblue'):
    ax.plot(x,y,label=label,color=color)
    return ax

def set_tick(ax,x_tick,y_tick):
    ax.set_xticks(x_tick)
    ax.set_yticks(y_tick)
    return ax

def fill_between(ax,x,y1,y2,color,alpha=0.5):
    ax.fill_between(x,y1,y2,color=color,alpha=alpha)
    return ax

def legend(ax,loc=None):
    if loc==None:
        ax.legend()
    else:
        ax.legend(loc=loc)
    return ax

def savefig(fig,name):
    fig.tight_layout()
    fig.savefig(name)
    return None
   
'''
ax.plot(x1,y1,label='data1',color='steelblue')
ax.plot(x2,y2,label='data2',color='firebrick')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
'''

#   Set the boarder of a frame
'''
ax.spines['right'].set_visible(False) 
ax.spines['top'].set_visible(False)
'''
#   Set ticks manually
#ax.set_xticks(np.linspace(0,10,100))
#ax.set_yticks(np.linspace(0,10,100))
'''
ax.legend(loc=(0.7,0.9))
plt.tight_layout()

plt.savefig('test.png')
'''
