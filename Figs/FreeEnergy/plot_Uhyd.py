import numpy as np
import matplotlib.pyplot as plt


class RHN:
    def __init__(self):
        fp=open("Uhyd.out")
        ndat=int(fp.readline())
        print(fp.readline())

        nH2O=np.zeros(ndat) # hydrated water mole number
        hz=np.zeros(ndat)   # basal spacing [nm]
        RH=np.zeros(ndat)   # relative humidity [-]
        mu_var=np.zeros(ndat) # logarithmic part of chemical potential [kJ/mol]
        mu_sat=np.zeros(ndat) # chemical potential for saturated H2O vapor [kJ/mol]
        G_var=np.zeros(ndat) # nonlinear part of interlayer-water Hydration energy [kJ/mol]
        G_sat=np.zeros(ndat) # linear part of interlayer-water Hydration energy [kJ/mol]
        k=0
        for row in fp:
            data=row.strip().split(",");
            nH2O[k]=float(data[0])
            hz[k]=float(data[1])
            RH[k]=float(data[2]);
            mu_var[k]=float(data[3])
            mu_sat[k]=float(data[4]);
            G_var[k]=float(data[5])
            G_sat[k]=float(data[6])
            k+=1
        self.nH2O=nH2O
        self.hz=hz
        self.RH=RH
        self.mu_var=mu_var
        self.mu_sat=mu_sat
        self.G_var=G_var
        self.G_sat=G_sat
        self.ndat=ndat

    def plot_hz(self,ax,lw=2,styl="-k"):
        ax.plot(self.nH2O,self.hz*10,styl,linewidth=lw)
        ax.grid(True)
        #ax.set_xlabel("$n(H_2O)$")
        ax.set_ylabel("basal spacing [$\AA$]")

    def plot_RH(self,ax,lw=2,styl="-k"):
        ax.plot(self.nH2O,self.RH*100,styl,linewidth=lw)
        ax.grid(True)
        ax.set_xlabel("$n(H_2O)$")
        ax.set_ylabel("R.H.[%]")

    def plot_mu(self,ax,lw=2,styl="-k"):
        ax.plot(self.nH2O,self.mu_var+self.mu_sat,styl,linewidth=lw)
        ax.grid(True)
        #ax.set_xlabel("$n(H_2O)$")
        ax.set_ylabel("$\delta \mu $[kJ/mol]")
        ax.set_ylim([-50,-44])

    def plot_G(self,ax,lw=2,styl="-k"):
        #ax.plot(self.nH2O,self.G_var+self.G_sat)
        ax.plot(self.nH2O,self.G_var,styl,linewidth=lw)
        ax.grid(True)
        ax.set_xlabel("$n(H_2O)$")
        ax.set_ylabel("$\delta G_{hyd}$[kJ/mol]")
        ax.legend()
    def plot_hz_XRD(self,ax,lw=2,styl="-k"):
        ax.plot(self.RH*100,self.hz*10,styl,linewidth=lw)
        ax.grid(True)
        ax.set_xlabel("R.H.[%]")
        ax.set_ylabel("basal spacing [$\AA$]")
    def plot_hz_MD(self,ax,lw=2,styl="-k"):
        ax.plot(self.nH2O,self.hz*10,styl,linewidth=lw)
        ax.grid(True)
        ax.set_xlabel("n($H_2O$)")
        ax.set_ylabel("basal spacing [$\AA$]")
        ax.set_xlim([0,self.nH2O[-1]])


if __name__=="__main__":

    plt.rcParams["font.size"]=14


    rhn_data=RHN()

    #  hz vs. n(H2O) 
    #rhn_data.plot_hz(ax1)   
    #  R.H. vs. n(H2O) 
    fig1=plt.figure()
    ax1=fig1.add_subplot(111)
    rhn_data.plot_RH(ax1)
    fig1.savefig("RH_nH2O.png",bbox_inches="tight")


    #  mu_var vs. n(H2O) 
    fig2=plt.figure()
    bx1=fig2.add_subplot(111)
    rhn_data.plot_mu(bx1)
    fig2.savefig("Muvar_nH2O.png",bbox_inches="tight")

    #  G_var vs. n(H2O) 
    fig3=plt.figure()
    cx1=fig3.add_subplot(111)
    rhn_data.plot_G(cx1)
    fig3.savefig("Gvar_nH2O.png",bbox_inches="tight")

    # XRD Swelling Curve
    fig4=plt.figure()
    ax=fig4.add_subplot(111)
    rhn_data.plot_hz_XRD(ax,lw=3)
    ax.set_xlim([0,100])
    ax.set_ylim([9,16])
    fig4.savefig("XRD_swelling.png",bbox_inches="tight")

    # XRD Swelling Curve
    fig5=plt.figure()
    bx=fig5.add_subplot(111)
    rhn_data.plot_hz_MD(bx,lw=3)
    bx.set_ylim([9,16])
    fig5.savefig("MD_swelling.png",bbox_inches="tight")


    plt.show()


