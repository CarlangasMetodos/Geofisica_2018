import numpy as np
import matplotlib.pyplot as plt
import math


G=6.67*10**-11
denE=3000
denT=2600
K0=10**-4
U0=4*np.pi*10**-7 #Constante de permeabilidad magnetica
K=0.1
x=np.linspace(-8000,8000,16000)
z=2000
rE=1000
M=K-K0

#Anomalias de la esfera

def gravimetria_esfera():
    y= ((4/3)*np.pi*G*rE**3*(denE-denT))*(z/(x**2+z**2)**(3/2))
    return y/np.abs(y.max()) #Devuelve el valor normalizado

def magnetometria_esfera():
    y=((1/3)*U0*rE**3*M)*((2*z**2-x**2)/(z**2+x**2)**(5/2))
    return y/np.abs(y.max()) #Devuelve el valor normalizado

def segunda_derg():
    y=np.diff(np.diff(gravimetria_esfera()))
    return y/np.abs(y.min())


plt.figure()
plt.plot(x,gravimetria_esfera(), label='Gravimetria esfera')
plt.plot(x,magnetometria_esfera(),label='Magnetometria esfera')
plt.plot(x[1:-1],segunda_derg(),label='Segunda Derivada gravimetria esfera')
plt.plot(x,np.linspace(0,0,16000), label='Linea de cero')
plt.legend()
plt.savefig('Anomalias_esfera.png')
plt.show()


#Anomalias del cilindro

rC=1000
denC=3000

def gravimetria_cilindro():
    y= (2.0*np.pi*G*rC**2*(denC-denT))*(1.0/(z*(1.0+(x/z)**2)))
    return y/np.abs(y.max()) #Devuelve el valor normalizado cilindro

def magnetometria_cilindro():
    y=(1/2)*U0*rC**2*M*(z**2-x**2)/(z**2+x**2)**2

    return y/np.abs(y.max()) #Devuelve el valor normalizado

def segunda_dergc():
    y=np.diff(np.diff(gravimetria_cilindro()))
    return y/np.abs(y.min())

plt.figure()
plt.plot(x,gravimetria_cilindro(), label='Gravimetria cilindro')
plt.plot(x,magnetometria_cilindro(),label='Magnetometria cilindro')
plt.plot(x[1:-1],segunda_dergc(),label='Segunda Derivada gravimetria cilindro')
plt.plot(x,np.linspace(0,0,16000), label='Linea de cero')
plt.legend()
plt.savefig('Anomalia_cilindro.png')
plt.show()
 
