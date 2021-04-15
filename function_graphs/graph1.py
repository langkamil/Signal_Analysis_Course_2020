import numpy as np                 #biblioteka zawierajaca funkcje matematyczne
import matplotlib.pyplot as plt    #biblioteka do tworzenia wykresow

    
#a) x(t) = A sin(2πf * t + ϕ)    dla  0 < A ∈ R,      ϕ ∈ (0, 2π)  i 3 roznych f ∈ R (na jednym wykresie)

#deklarujemy niezbedne wartosci
A = float(2.0)  #ampilituda 
phi = np.pi/2   #faza poczatkowa 
#czestotliwosci
f1 = float(0.5) 
f2 = float(1.0)
f3 = float(2.0)


def x(t,f):
     return A * np.sin(float(2)*np.pi*f * t + phi)

t = np.arange(-2.0*np.pi, 2.0*np.pi, 0.001)

plt.plot(t, x(t,f1), label = 'x(t) = 2sin(2π*0.5 * t + π/2 )', color = 'red')
plt.plot(t, x(t,f2), label = 'x(t) = 2sin(2π*1 * t + π/2 )', color = 'green')
plt.plot(t, x(t,f3), label = 'x(t) = 2sin(2π*2 * t + π/2 )', color = 'blue')

plt.grid()
plt.xlabel('t')
plt.ylabel('x(t) = A sin(2πf * t + ϕ)')
plt.axis([-2,2,-2.1,2.1])
plt.title('Wykresy trzech sygnalow sinusoidalnych')
plt.legend(loc = 'lower left')
plt.tight_layout()

plt.show()
