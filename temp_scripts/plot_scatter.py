import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
import pickle

pca = open('./data/PCA_unbias_250ns.pkl','rb')

PCA = pickle.load(pca)
print(PCA.keys())



matplotlib.rcParams['figure.dpi']=200
matplotlib.rcParams['savefig.dpi']=200
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(PCA['ABE_run1'][:,0]*10,PCA['ABE_run1'][:,1]*10,label='ABE_run1',marker='o',c='navy',s=10,alpha=0.6)
ax.scatter(PCA['ABE_run2'][:,0]*10,PCA['ABE_run2'][:,1]*10,label='ABE_run2',marker='o',c='mediumblue',s=10,alpha=0.6)
ax.scatter(PCA['acat_run1'][:,0]*10,PCA['acat_run1'][:,1]*10,label='acat_run1',marker='o',c='firebrick',s=10,alpha=0.6)
ax.scatter(PCA['acat_run2'][:,0]*10,PCA['acat_run2'][:,1]*10,label='acat_run2',marker='o',c='orangered',s=10,alpha=0.6)
ax.scatter(PCA['bound'][:,0]*10,PCA['bound'][:,1]*10,label='bound_state',marker='*',c='green',s=40)
'''
ax.scatter(PCA['ABE_run1'][0,0]*10,PCA['ABE_run1'][0,1]*10,marker='*',c='',edgecolor='navy',s=25,alpha=0.6)
ax.scatter(PCA['ABE_run2'][0,0]*10,PCA['ABE_run2'][0,1]*10,marker='*',c='red',s=25,alpha=0.6)
ax.scatter(PCA['acat_run1'][0,0]*10,PCA['acat_run1'][0,1]*10,marker='*',c='',edgecolor='firebrick',s=25,alpha=0.6)
ax.scatter(PCA['acat_run2'][0,0]*10,PCA['acat_run2'][0,1]*10,marker='*',c='orangered',s=25,alpha=0.6)
'''
#ax.spines['top'].set_visible(False)
#ax.spines['right'].set_visible(False)
ax.set_xlabel(r'PC1 ($\mathrm{\AA}$)',fontsize=24,fontname='Times New Roman',fontweight='bold')
ax.set_ylabel('PC2 ($\mathrm{\AA}$)',fontsize=24,fontname='Times New Roman',fontweight='bold')
labels = ax.get_xticklabels() + ax.get_yticklabels()

ax.set_xticks(np.linspace(-25,25,6))
ax.set_yticks(np.linspace(-25,25,6))
ax.tick_params(labelsize=22)
[label.set_fontname('Times New Roman') for label in labels]

font1 = fm.FontProperties(family='Times New Roman',size=16)
ax.legend(prop=font1,loc=(0.62,0.55))
plt.tight_layout()
plt.savefig('PCA_250ns_unbiased.png')

print(PCA['bound'])



