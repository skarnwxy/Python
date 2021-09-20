# -*- coding:utf-8 -*-
import numpy as np
def main():
    import matplotlib.pyplot as plt
    x=np.linspace(-np.pi,np.pi,256,endpoint=Ture)
    c,s=np.cos(x),np.sin(x)
    plt.figure(1)
    plt.plot(x,c,color="blue",linewidth=1.0,linestyle="-",label="COS",alpha=0.5)
    plt.plot(x,s,"r*",label="SIN")
    plt.title("COS&SIN")
    ax=plt.gce()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data",0))
    ax.spines["bottom"].set_position(("data",0))
    ax.xaixs.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$,r'$-\pi/2$,r'$0$,r'$+\pi/2$,r'$+\pi$'])
plt.yticks(np.linspace(-1,1,5,endpoint=Ture))
for lable in ax.get_xtickelables()+ax.get_yticklable():
    lable.set_fontsize(16)
    lable.set_bbox(dict(facecolor="white",edgecolor="None",alpha=0.2))
 plt.legend(loc="upper left")
 plt.grid()
 plt.fill_between(x,np.abs(x)<0.5,c,c>0.5,color="green",alpha=0.25)
 t=1
 plt.plot([t,t],[0,np.cos(t)],"y",linewidth=3,linestyle='--')
 plt.annotate("cos(1)",xy=(t,np.cos(1),xycoords="data",xytext=(+10,+30),textcoords="offset points",arrowprpos=(arrowstyle="->",connectionstule="arc3,rad=.2")
    plt.show()
if __name__=="__main__":