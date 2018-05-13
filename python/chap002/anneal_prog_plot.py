import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def prog03(x):
    if x < 0:
        return 0
    elif ( x >= 0 ) and ( x < 5 ):
        return 250./5. * x
    elif ( x >= 5 ) and ( x < 35 ):
        return 250
    elif ( x >=35 ) and ( x <= 40 ):
        return -50. * x + 2000.
    else:
        return 0

def prog06(x):
    if x < 0:
        return 0
    elif ( x >= 0 ) and ( x < 5 ):
        return 600./5. * x
    elif ( x >= 5 ) and ( x < 20 ):
        return 600.
    elif ( x >= 20 ) and ( x <= 25 ):
        return -600./5. * x + 3000.
    else:
        return 0

if __name__=="__main__":
    #print plt.style.available
    t = np.linspace(0, 40, 1000)   
    y = [prog03(tt) for tt in t]

    t2 = np.linspace(0, 25, 1000)
    y2 = [prog06(tt2) for tt2 in t2]

    plt.clf()
    plt.style.use('classic')
    plt.xlabel(r'Time (min)', fontsize=16)
    plt.ylabel(r'Temperature $(^\circ$C)', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.ylim(0,300)
    plt.axvline( x = 5, ymax=0.833, color='k', linestyle='--')
    plt.axvline( x = 35, ymax=0.833, color='k', linestyle='--')
    plt.plot(t, y, linewidth=2)
    plt.tight_layout()
    plt.savefig('annealed_program03_plot.pdf')

    plt.clf()
    plt.style.use('classic')
    plt.xlabel(r'Time (min)', fontsize=16)
    plt.ylabel(r'Temperature $(^\circ$C)' , fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.ylim(0,700)
    plt.axvline( x = 5, ymax=0.8571, color='k', linestyle='--')
    plt.axvline( x = 7, ymax=0.8571, color='k', linestyle='--')
    plt.axvline( x = 20, ymax=0.8571, color='k', linestyle='--')
    plt.plot(t2, y2, linewidth=2)
    plt.tight_layout()
    plt.savefig('annealed_program06_plot.pdf')
