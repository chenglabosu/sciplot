import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
import pickle

dist = open('./data/rmsd_bound_ABD.pkl','rb')

rmsd = pickle.load(dist)
print(rmsd.keys())


rmsd11 = rmsd['pull1']*10
rmsd12 = rmsd['pull2']*10
rmsd13 = rmsd['pull3']*10
rmsd14 = rmsd['pull4']*10


rmsd21 = rmsd['prod1']*10
rmsd22 = rmsd['prod2']*10
rmsd23 = rmsd['prod3']*10
rmsd24 = rmsd['prod4']*10


rmsd31 = rmsd['acat1_150_300']*10
rmsd32 = rmsd['acat2_150_300']*10


L = len(rmsd11)

'''
x = np.linspace(0,250,L)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,rmsd11,label='ABE_run1',c='navy')
ax.plot(x,rmsd12,label='ABE_run2',c='blue')
ax.plot(x,rmsd21,label='acat_run1',c='firebrick')
ax.plot(x,rmsd22,label='acat_run2',c='red')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('time (ns)',fontsize=24,fontname='Times New Roman',fontweight='bold')
ax.set_ylabel('RMSD (A)',fontsize=24,fontname='Times New Roman',fontweight='bold')

ax.set_xticks(np.linspace(0,250,6))
ax.set_yticks(np.linspace(0,30,7))
labels = ax.get_xticklabels() + ax.get_yticklabels()


ax.tick_params(labelsize=22)
[label.set_fontname('Times New Roman') for label in labels]

font1 = fm.FontProperties(family='Times New Roman',size=18)
ax.legend(prop=font1,loc=(0.6,0.1))
plt.tight_layout()
plt.savefig('rmsd_unbiased.eps')
'''

rmsd_pull = np.concatenate((rmsd11,rmsd12,rmsd13,rmsd14))
rmsd_prod = np.concatenate((rmsd21,rmsd22,rmsd23,rmsd24))
rmsd_acat = np.concatenate((rmsd31,rmsd32))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(rmsd_pull,label='pull',bins=100,alpha=0.6,color='green')
ax.hist(rmsd_prod,label='unbiased',bins=100,alpha=0.6,color='blue')
ax.hist(rmsd_acat,label='Acat',bins=100,alpha=0.6,color='red')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel(r'RMSD ($\mathrm{\AA}$)',fontsize=22,fontname='Times New Roman',fontweight='bold')
ax.set_ylabel('frequency',fontsize=24,fontname='Times New Roman',fontweight='bold')
ax.set_xticks(np.linspace(2.5,4,7))
ax.set_yticks(np.linspace(0,300,7))

labels = ax.get_xticklabels() + ax.get_yticklabels()

ax.tick_params(labelsize=22)
[label.set_fontname('Times New Roman') for label in labels]

font1 = fm.FontProperties(family='Times New Roman',size=18)
ax.legend(prop=font1,loc=(0.65,0.65))
plt.tight_layout()
plt.savefig('rmsd_hist.png')



