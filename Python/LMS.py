import numpy as np
import matplotlib.pylab as plt
#Toolbox para simplificar as tarefas de processamento de sinais adaptáveis
#​​dentro do Python (filtragem, predição, reconstrução, classificação).
import padasip as pa 

# gerando informações
N = 1000
signal = np.random.normal(0, 1, (N, 10)) # matriz de entrada
noise_in = np.random.normal(0, 0.1, N) # ruído
d = 2*signal[:,0] + 0.1*signal[:,1] - 4*signal[:,2] + 0.5*signal[:,3] + noise_in # sinal desejado
# identificação
f = pa.filters.FilterLMS(n=10, mu = 0.1, w = "random")
y, e, w = f.run(d, signal)

# resultados
plt.figure(figsize=(15,9))
plt.subplot(211);plt.title("Adaptation");plt.xlabel("Amostras - k")
plt.plot(d,"b", label="d - Sinal desejado")
plt.plot(y,"g", label="y - Saída");plt.legend()
plt.subplot(212);plt.title("Erro");plt.xlabel("Amostras - k")
plt.plot(10*np.log10(e**2),"r", label="e - erro [dB]");plt.legend()
plt.tight_layout()
plt.show()