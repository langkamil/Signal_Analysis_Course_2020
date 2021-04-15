import numpy as np                 #biblioteka zawierajaca funkcje matematyczne
import matplotlib.pyplot as plt    #biblioteka do tworzenia wykresow


#c) z(t) = A sin(2πf t)e^(at)    dla  trzech roznych (A, f, a) 

#deklarujemy niezbedne wartosci

#ampilituda 
A1 = float(1.0)  
A2 = float(3.0)
A3 = float(4.0)

#czestotliwosci
f1 = float(2.0) 
f2 = float(1.3)
f3 = float(10)

a1 = float(-2.0)
a2 = float(1.0)
a3 = float(2.0) 

def z(t,A,f,a):
    return A * np.sin(float(2)*np.pi*f * t )*np.e**(t*a)

t = np.arange(-200.0, 200.0, 0.001)


#CZERWONY
plt.subplot(221)
plt.plot(t, z(t,A1,f1,a1), label = 'z(t) = 1sin(2π*2 * t)*e^(-2*t)', color = 'red')
plt.grid()
plt.axis([-2.5,1,-80,120])
plt.title('Wykresy funkcji z(t) = 1sin(2π*2 * t)*e^(-2*t)')
plt.tight_layout()

#ZIELONY
plt.subplot(222)
plt.plot(t, z(t,A2,f2,a2), label = 'z(t) = 3sin(2π*0.1 * t)*e^(0.5*t)', color = 'green')
plt.grid()
plt.axis([-2,3.49,-60,85])
plt.title('Wykres funkcji z(t) = 3sin(2π*1.3 * t)*e^(1*t)')
plt.tight_layout()

#NIEBIESKI
plt.subplot(223)
plt.plot(t, z(t,A3,f3,a3), label = 'z(t) = 4sin(2π*2 * t)*e^(-2*t)', color = 'blue')
plt.grid()
plt.axis([-1,1,-30,30])
plt.title('Wykres funkcji z(t) = 4sin(2π*10 * t)*e^(2*t)')
plt.tight_layout()

plt.show()
