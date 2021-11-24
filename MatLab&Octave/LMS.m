%%Aplicação de um algoritmo LMS

clear()
N =  5000; %comprimento do sinal(amostras)
n = 0:1:N;

%%Sinal de referencia
f = 0.005; %Hz
theta = 0; %fase
arg = (2.*pi.*f*n - theta); % argumento da função do sinal
signal = sin(arg);


L = 15; % numero de coeficientes
wreal = randn(1,L);

%%Gerando sinal de ruído puro
anoise = randn(1,N);

%%Gerando ruído para sinal de entrada
anoise_input = conv(anoise,wreal);

%%sinal de entrada
d = (signal + anoise_input(1:1:length(signal)));

%%criação do vetor W de coeficientes do filtro
w(1,:) = zeros(1,L);
u = 0.005; %-> coeficiente mi

%% condições iniciais 0, para implementação do algoritimo
anoise = [zeros(1,L-1) anoise];

%%%%  INICIANDO O ALGORITIMO LMS  %%%%%%%%
output = zeros(1,N); %vetor para saída Y(n)
 
 for i=1:N %mover o contador para começar no sinal de entrada d(n) e
           %pular as condições iniciais
             
   j =i+L-1;
   %realiza a convolução dos coeficientes com o sinal de ruído puro para obter
   % o ruído de aprox. à entrada e subtrai para obter a saída Y(n)
   
   aux = anoise(i:1:j)';
   anoise_input(i) = w(i,:)*aux; %convolucão
   output(i) = d(i) - anoise_input(i); %sinal de saída
   w(i+1,:) = w(i,:) + u.*anoise(i:j).*output(i); %atualização de coeficientes
 endfor
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
subplot(311)
stem(1:length(d), d)
title("Sinal a ser filtrado");
axis([0,N,-10,10])

subplot(312)
stem(1:length(signal), signal)
title("Sinal Original");
axis([0,N,-1,1])

subplot(313)
stem(1:length(output), output)
title("Sinal Filtrado - LMS");
axis([0,N,-6,6])