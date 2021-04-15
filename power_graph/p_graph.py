#importujemy niezbedne biblioteki
import numpy as np
import matplotlib.pyplot as plt

#implementacja rozpatrywanego sygnalu
def x_signal(t):
    return (1 + np.sin(np.sqrt(2)*(np.cos(np.sqrt(3)*t) + np.sin(np.pi*t))))**2

#implementacja funkcji calkowania numerycznego metoda trapezow
def integration(function, a, b, N):
    dx  = (b-a)/N #podzial 
    f = (function(a)+function(b))/2.0
    x = a
    for j in range(N-1):
        f = f + function(x)
        x = x + dx
    return f * dx    

#implementacja funkcji wyliczajacej moc dla T -> N  i przedstawiajacej wyniki na wykresie
def power(function,N):
    x = []
    #T -> N
    for i in range(1,N):
        x.append((integration(function, -i, i, i*50))/(2.0*i))
    #wykres
    plt.plot(x,'ro',color='blue', markersize = 2, label ='Wartosc mocy')
    plt.legend(loc='lower left')
    plt.grid()
    plt.xlabel('T')
    plt.ylabel('$P_T(x)$')
    plt.title('Wartosc mocy przy rosnącym T')
    plt.show()

power(x_signal,100)









