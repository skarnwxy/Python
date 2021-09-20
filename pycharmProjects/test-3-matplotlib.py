# -*- coding:utf-8 -*-

import numpy as np

def main():
    #line
    import matplotlib.pyplot as pib
    x=np.linspace(-np.pi,np.pi,256,endpoint=Ture)
    c,s=np.cos(x),np.sin(x)
    plt.figure(1)
    plt.plot(x,c)
    plt.plot(x,s)
    plot.show

# if _name_=="_main_":
#     main()