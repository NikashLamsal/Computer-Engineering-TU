# Matlab Code & Output 
### 1. Generate a sine wave of amplitude 5 and frequency 3 Hz over the time interval 0 to 1 second with a sampling interval of 0.001 seconds also Generate random noise and add it to the sine wave .

```matlab
clc;
close all;
clear all;

a = 5;          % Amplitude
f = 3;          % Frequency in Hz
t = 0:0.001:1;  % Time vector
x = a * sin(2 * pi * f * t);  % Sine wave

subplot(3,1,1);
plot(t, x, 'b');  
xlabel("Time (s)");
ylabel("Amplitude");
title("Sine Wave / Nikash / 39");
grid on;

noise = rand(1, length(t)); 
subplot(3,1,2);
plot(t, noise, 'r'); 
xlabel("Time (s)");
ylabel("Amplitude");
title("Noise / Nikash / 39");
grid on;

y = x + noise;
subplot(3,1,3);
xlabel("Time (s)");
ylabel("Amplitude");
title("Sine Wave with Noise / Nikash / 39");
grid on;

```
### Output : 
![output](./Output%20Store/lab21.png)

### 2 . Write a MATLAB program to generate and plot both a continuous-time and discrete-time impulse signal .

```matlab

clc;
clear all;
i = 1;
for t = -2:0.001:2;
if (t == 0)
x(i) = 1;
else 
x(i) = 0;
end;
i = i+1;
end;

t = -2:0.001:2;
subplot(2,1,1);
plot(t,x);
xlabel("Time");
ylabel("Amplitude");
title("CT Impulse / Nikash Lamsal / 39");
grid on;
i = 1;
for t = -2:0.001:2;
if (t == 0 )
x(i) = 1;
else 
x(i) = 0;
end;
i = i+1;
end;
t = -2:0.001:2;
subplot(2,1,2);
stem(t,x);
xlabel("Time");
ylabel("Amplitude");
title("DT / Nikash / 39");
grid on;

```
### Output : 
![output](./Output%20Store/lab22.png)

### 3 . Write a MATLAB program to generate and plot the Continuous-Time and Discrete-Time Unit Step signals using the time range -2 to 2 seconds.

```matlab
clc;
clear all;
i=1;
for t=-2:0.001:2
    if(t>=0)
        x(i)=1;
    else
        x(i)=0;
    end
 i=i+1;
end
t=-2:0.001:2;
subplot(2,1,1);
plot(t,x);
xlabel('time');
ylabel('amp');
title('CT unit step/ Nikash / 39');
grid on;
i=1;
for t=-2:0.001:2
    if (t>=0)
        x(i)=1;
    else
        x(i)=0;
    end
i=i+1;
end
t = -2:0.001:2;
subplot(2,1,2);
stem(t,x);
xlabel('time');
ylabel('amp');
title('DT unit step / Nikash / 39');
grid on;

```
### Output :
![output](./Output%20Store/lab23.png)


### 4 . Write a MATLAB program to generate and plot both Continuous-Time and Discrete-Time ramp signals for the time range from -2 to 2 seconds.

```matlab

clc;
clear all;
i=1;
for t=-2:0.001:2
    if(t>=0)
        x(i)=t;
    else
        x(i)=0;
    end
 i=i+1;
end
t=-2:0.001:2;
subplot(2,1,1);
plot(t,x);
xlabel('Time');
ylabel('Amplitude');
title('CT Ramp / Nikash / 39');
grid on;
i=1;
for t=-2:0.001:2
    if (t>=0)
        x(i)=t;
    else
        x(i)=0;
    end
i=i+1;
end
t = -2:0.001:2;
subplot(2,1,2);
stem(t,x);
xlabel('Time');
ylabel('Amplitude');
title('DT Ramp / Nikash / 39');
grid on;

```
![output](./Output%20Store/lab24.png)


### 5 . Write a MATLAB program to generate and plot a rectangular pulse signal which is 1 for time between -1 and 1 and 0 elsewhere.

```matlab

clc;
clear all;
i=1;
for t=-2:0.001:2
    if(t<=-1||t>=1)
        x(i)=0;
    else
        x(i)=1;
    end
 i=i+1;
end
t=-2:0.001:2;
subplot(2,1,1);
plot(t,x);
xlabel('Time');
ylabel('Amplitude');
title('Continuous-Time Pulse/ Nikash / 39');
grid on;
i=1;
for t=-2:0.001:2
    if(t<=-1||t>=1)
        x(i)=0;
    else
        x(i)=1;
    end
 i=i+1;
end
t=-2:0.001:2;
subplot(2,1,2);
stem(t,x);
xlabel('Time');
ylabel('Amplitude');
title('Discrete-Time Pulse/ Nikash / 39');
grid on;


```
![output](./Output%20Store/lab25.png)


### 6 . Write a MATLAB program to generate and plot the sinc function for time ranging from -5 to 5.

```matlab

x=linspace(-5,5)
y=sinc(x);
plot(x,y)
xlabel('Time');
ylabel('Amplitude');
title('sinc Function / Nikash / 39');
grid on;

```
![output](./Output%20Store/lab26.png)


### 7 . Write a MATLAB program to generate square waves of 30%, 50%, and 90% duty cycles and plot them.

```matlab
clc;
close all;
clear;

a = 4;                   
f = 10/200;                
t = 0:0.01:100;         

x = a * square(2*pi*f*t, 30);   
y = a * square(2*pi*f*t, 50);   
z = a * square(2*pi*f*t, 90);  

subplot(3,1,1);
plot(t, x, 'b');
xlabel('Time');
ylabel('Amplitude');
grid on;

subplot(3,1,2);
plot(t, y, 'g');
xlabel('Time');
ylabel('Amplitude');
grid on;

subplot(3,1,3);
plot(t, z, 'r');
xlabel('Time');
ylabel('Amplitude');
grid on;


```
![output](./Output%20Store/lab27.jpg)
