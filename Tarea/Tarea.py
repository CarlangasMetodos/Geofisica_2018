import numpy as np
import matplotlib.pyplot as plt
import math


#Perfil de anomalia de Bouguer

y=[267,268,269,270,271,272,273,274,275,275.2,275.4,275.3,275,274,273,272,271,270,269,268,267,266,265,264,263,262,261]
x=[0.849,1.456,2.724,3.123,3.748,4.269,4.720,5.189,5.986,6.325,6.752,7.182,7.479,8.130,8.4,8.695,8.9,9.145,9.370,9.665,9.978,10.326,10.690,11.073,11.437,11.993,12.6]

"""
plt.figure()
plt.plot(x,y,c='red')
plt.title('Perfil de anomalia de Bouguer')
plt.xlabel('Distancia (km)')
plt.ylabel('Anomalia gravimetrica (mGals)')
plt.savefig('Perfil1.png')
plt.show()
"""

#Modelamiento/Ajuste del perfil teorico con el observado

G=6.67*10**-11
Droca=2650
Dslab=2875 #PONERLO
h=-1.140
t=1800 #PONERLO
L=9.500 #PONERLO

deltaD=Droca-Dslab
anomalias=[]
y2=[]
x2=[]


for i in range(len(x)):
	y2.append(y[i]-261)
	gz=2*G*t*10**5*deltaD*(math.atan((L-x[i])/(h))+math.atan(x[i]/(h)))
	anomalias.append(gz)

"""
print (anomalias)
print(y2)


plt.figure()
plt.plot(x,y2,c='red', label='Perfil observado')
plt.plot(x,anomalias, label='Perfil teorico')
plt.title('Perfil modelado')
plt.xlabel('Distancia (km)')
plt.ylabel('Anomalia gravimetrica (mGals)')
plt.legend()
plt.savefig('Perfil6.png')
plt.show()
"""

#Modelamiento solo de la parte sureste

ya=[275,274,273,272,271,270,269,268,267,266,265,264,263,262,261]
xa=[7.479,8.130,8.4,8.695,8.9,9.145,9.370,9.665,9.978,10.326,10.690,11.073,11.437,11.993,12.6]

ya2=[]
anomalias2=[]


for i in range(len(xa)):
	ya2.append(ya[i]-261)
	gz2=2*G*t*10**5*deltaD*(math.atan((L-xa[i])/(h))+math.atan(xa[i]/(h)))
	anomalias2.append(gz2)
"""
plt.figure()
plt.plot(xa,ya2,c='red', label='Perfil observado SE')
plt.plot(xa,anomalias2, label='Perfil teorico SE')
plt.title('Perfil modelado SE')
plt.xlabel('Distancia (km)')
plt.ylabel('Anomalia gravimetrica (mGals)')
plt.legend()
plt.savefig('Perfil6b.png')
plt.show()
"""

#Calculo de errores

Ea=[]
EaSE=[]

for i in range(len(x)):
	Ea.append(abs(y2[i]-anomalias[i]))


for i in range(len(xa)):
	EaSE.append(abs(ya2[i]-anomalias2[i]))


Eat=np.sum(Ea)
EaSEt=np.sum(EaSE)

print( Eat, EaSEt)

















