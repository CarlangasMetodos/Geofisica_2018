import numpy as np
import matplotlib.pyplot as plt

#Punto 1
rhow=1
phi=np.linspace(0,1,100)
m=[1.2,1.5,1.8,2.1,2.4,2.5]
A=[]

def Archie(phi,m):
    rho=rhow*phi**-m
    log=np.log(rho)
    return log

plt.plot(np.log(phi),Archie(phi,m[0]), label='m=1.2')
plt.plot(np.log(phi),Archie(phi,m[1]), label='m=1.5')
plt.plot(np.log(phi),Archie(phi,m[2]), label='m=1.8')
plt.plot(np.log(phi),Archie(phi,m[3]), label='m=2.1')
plt.plot(np.log(phi),Archie(phi,m[4]), label='m=2.4')
plt.plot(np.log(phi),Archie(phi,m[5]), label='m=2.5')
plt.legend()
plt.title('Ley de Archie para  rocas totalmente saturadas')
plt.xlabel('Log (Porosidad)')
plt.ylabel('Log (Resistividad (ohm*m))')
plt.savefig('Archie.png')
plt.show()


#PARTE A Circuito en Serie

L=np.linspace(0,1,100)
def funcion(L):
    rho=L+1000*(1-L)
    log=np.log(rho)
    return log

#PARTE B Circuito en Paralelo
def funcion2(L):
    rho=1000/(1000*L+1-L)
    log=np.log(rho)
    return log

#PARTE C Para resistividad usando Archie, con Pw=1, phi entre 0 y 1, m=1 y m=2

phi=L
def funcion3(phi,m):
    rho=phi**-m
    log=np.log(rho)
    return log

plt.plot(L,funcion(L), label='Serie')
plt.plot(L,funcion2(L), label='Paralelo')
plt.plot(L,funcion3(phi,2),label='Archie, m=2')
plt.plot(L,funcion3(phi,1),label='Arche,m=1')
plt.ylabel('Log (Resistividad (Ohm m))')
plt.xlabel('Longitud (m)')
plt.legend()
plt.savefig('Punto 2.png')
plt.show()




