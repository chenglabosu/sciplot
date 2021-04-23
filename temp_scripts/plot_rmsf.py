import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
import pickle

rmsf = open('RMSF_150_200ns.pkl','rb')

RMSF = pickle.load(rmsf)
print(RMSF.keys())

L = len(RMSF['ABE1'])
print(L)

x = np.linspace(1,L,L)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,RMSF['ABE1']*10,label='ABE_run1',c='navy',linestyle='-',lw=1)
ax.plot(x,RMSF['ABE2']*10,label='ABE_run2',c='blue',linestyle='-',lw=1)
ax.plot(x,RMSF['acat1A']*10,label='acat_A_run1',c='maroon',linestyle='-',lw=1)
ax.plot(x,RMSF['acat1B']*10,label='acat_B_run1',c='firebrick',linestyle='-',lw=1)
ax.plot(x,RMSF['acat2A']*10,label='acat_A_run2',c='red',linestyle='-',lw=1)
ax.plot(x,RMSF['acat2B']*10,label='acat_B_run2',c='orangered',linestyle='-',lw=1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('residue',fontsize=22,fontname='Times New Roman',fontweight='bold')
ax.set_ylabel('RMSF (A)',fontsize=22,fontname='Times New Roman',fontweight='bold')
labels = ax.get_xticklabels() + ax.get_yticklabels()

ax.tick_params(labelsize=18)
[label.set_fontname('Times New Roman') for label in labels]

font1 = fm.FontProperties(family='Times New Roman',size=12)
ax.legend(prop=font1,loc=(0.05,0.5))
plt.tight_layout()
plt.savefig('rmsf_150_200ns.eps')





