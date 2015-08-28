'''Common formatting and print commands

'''

# author: Thomas Haslwanter, date: June-2015

# Import standard packages
import matplotlib.pyplot as plt
import os

# additional packages
import matplotlib as mlb

def despine(axis='right'):
    '''Despine the plot'''
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.yaxis.set_ticks_position('left')

def set(fs=18):
    '''Set my favorite defaulte fonts'''
    font = {'family' : 'sans-serif',
            'weight' : 'normal',
            'size'   : fs}

    xtick = {'direction': 'out',
             'major.size': 6,
             'labelsize': fs-2}
    
    ytick = {'direction': 'out',
             'major.size': 6,
             'labelsize': fs-2}
    
    axes = {'labelsize': fs,
            'titlesize': fs}
    
    legend = {'fontsize': fs}
    
    figure = {'autolayout': True}
    
    mlb.rc('font', **font)
    mlb.rc('xtick', **xtick)
    mlb.rc('ytick', **ytick)
    mlb.rc('axes', **axes)
    mlb.rc('legend', **legend)
    mlb.rc( 'figure', **figure)
    
def printout(outFile, xlabel = '', ylabel='', title='', outDir = '..\Images'):
    '''Save the current figure to a file, and then display it'''
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    plt.tight_layout
    
    xlim = plt.gca().get_xlim()
    plt.hlines(0, xlim[0], xlim[1], linestyles='--', colors='#999999')
    plt.gca().set_xlim(xlim)
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    
    plt.show()
    plt.close()

def printout_plain(outFile, outDir = '..\Images'):
    '''Save a figure with subplots to a file, and then display it'''
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    
    plt.show()
    plt.close()


if __name__ == '__main__':
    set()
