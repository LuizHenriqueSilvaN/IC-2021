import numpy as np
import matplotlib.pyplot as plt

def returnFunction(x, v):
    d = 2*x[:, 0] + v  # target
    return d

def LMS_Filter(d, x):

    N = len(x)
    
    if not len(d) == N:
        raise ValueError('The length of vector d and matrix x must agree.')
    
    n = len(x[0])

    try:
        x = np.array(x)
        d = np.array(d) 

    except:
        raise ValueError('Impossible to convert x or d to a numpy array')

    # create empty arrays
    y = np.zeros(N)
    e = np.zeros(N)
    
    W_history = np.zeros((N, n)) # coeficientes de W
    
    #Wcoef = np.random.normal(0, 0.5, n) 
    Wcoef = np.zeros(n) 
    
    # adaptation loop
    for k in range(N):

        W_history[k,:] = Wcoef
        y[k] = np.dot(Wcoef, x[k])
        e[k] = d[k] - y[k]
        dw = mi * e[k] * x[k]
        Wcoef += dw

    return y, e, W_history

# Dados de entrada
N = 1000
mi = 0.05  # Coeficiente mi
x = np.sin(np.sin(np.random.normal(0, 1, (N, 4)))) # matriz de entrada
v = np.sin(np.random.normal(0, 0.1, N)) # ruido
d = returnFunction(x, v)

yout, erro, w = LMS_Filter(d, x)

plt.figure(figsize = (15,9))
plt.subplot(311)
plt.plot(d,'black', linewidth=(1.5), label = "d - Sinal desejado")
plt.plot(yout, '--y',label = "y - Saída");plt.legend();
plt.xlabel("Amostras - k")

plt.subplot(312)
plt.plot(10*np.log10(erro**2), 'r', label = "e - erro[dB]");plt.legend()
plt.xlabel("Amostras - k");plt.ylabel("dB")

plt.subplot(313)
plt.title("W - Peso dos coeficientes")
plt.plot(w,'teal', linewidth=(1.5));
plt.xlabel("Amostras - k")


plt.tight_layout()
plt.show()

