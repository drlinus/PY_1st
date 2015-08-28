''' Different continuous distribution functions.
- T-distribution
- F-distribution
- Chi2-distribution
- Exponential

'''

# author: Thomas Haslwanter, date: Nov-2014


# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import os

# additional packages
from matplotlib.mlab import frange

sns.set(context='poster', style='ticks', palette='bright', font_scale=1.5)

#----------------------------------------------------------------------
def showT():
    '''Utility function to show T distributions'''
    
    t = frange(-5, 5, 0.05)
    TVals = [1,5]
    
    normal = stats.norm.pdf(t)
    t1 = stats.t.pdf(t,1)
    t5 = stats.t.pdf(t,5)
    
    plt.plot(t,normal, '--',  label='normal')
    plt.plot(t, t1, label='df=1')
    plt.plot(t, t5, label='df=5')
    plt.legend()
        
    plt.xlim(-5,5)
    plt.xlabel('X')
    plt.ylabel('pdf(X)')
    plt.axis('tight')
    
    outDir = r'..\Images'
    outFile = 'dist_t.png'
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    plt.show()
    plt.close()
    
#----------------------------------------------------------------------
def showChi2():
    '''Utility function to show Chi2 distributions'''
    
    t = frange(0, 8, 0.05)
    Chi2Vals = [1,2,3,5]
    
    for chi2 in Chi2Vals:
        plt.plot(t, stats.chi2.pdf(t, chi2), label='k={0}'.format(chi2))
    plt.legend()
        
    plt.xlim(0,8)
    plt.xlabel('X')
    plt.ylabel('pdf(X)')
    plt.axis('tight')
    
    outDir = r'..\Images'
    outFile = 'dist_chi2.png'
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    plt.show()
    plt.close()
    
#----------------------------------------------------------------------
def showF():
    '''Utility function to show F distributions'''
    
    t = frange(0, 3, 0.01)
    d1s = [1,2,5,100]
    d2s = [1,1,2,100]
    
    for (d1,d2) in zip(d1s,d2s):
        plot(t, stats.f.pdf(t, d1, d2), label='F({0}/{1})'.format(d1,d2))
    plt.legend()
        
    plt.xlim(0,3)
    plt.xlabel('X')
    plt.ylabel('pdf(X)')
    plt.axis('tight')
    plt.legend()
        
    outDir = r'..\Images'
    outFile = 'dist_f.png'
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    plt.show()
    plt.close()
    

#----------------------------------------------------------------------
def showExp():
    '''Utility function to show exponential distributions'''
    
    t = frange(0, 3, 0.01)
    lambdas = [0.5, 1, 1.5]
    
    for par in lambdas:
        plt.plot(t, stats.expon.pdf(t, 0, par), label='$\lambda={0:3.1f}$'.format(par))
    plt.legend()
        
    plt.xlim(0,3)
    plt.xlabel('X')
    plt.ylabel('pdf(X)')
    plt.axis('tight')
    plt.legend()
        
    outDir = r'..\Images'
    outFile = 'dist_exp.png'
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    plt.show()
    plt.close()
    
    
#----------------------------------------------------------------------
if __name__ == '__main__':
    showT()
    showChi2()
    showF()
    showExp()
