import numpy as np                 #biblioteka zawierajaca funkcje matematyczne
import matplotlib.pyplot as plt    #biblioteka do tworzenia wykresow


#b) y(t) = Be^(at),  B > 0 , 3 różne a (na jednym wykresie) 

#deklarujemy niezbedne wartosci
B = float(3.0)
a1 = float(-2.0)
a2 = float(0.5)
a3 = float(2.0) 

def y(t,a):
    return B*np.e**(t*a)

t = np.arange(float(-10.0), float(10.0) , 0.001)


plt.plot(t, y(t,a1), label = 'y(t) = 3e^(t*(-2))', color = 'red')
plt.plot(t, y(t,a2), label = 'y(t) = 3e^(t*0.5)', color = 'green')
plt.plot(t, y(t,a3), label = 'y(t) = 3e^(t*2)', color = 'blue')

plt.grid()
plt.axis([-5,5,0,20])
plt.title('Wykresy trzech sygnalow o wzorze y(t) = Be^(at)')
plt.legend()
plt.tight_layout()

plt.show()

