# Analog Modulation
---
### Amplitude Modulation

```
Modulaton (m) = c(t) * m(t)
        where c(t) = Carrier
              m(t) = Message
 ```
### Why Modulation ?
#### 1. Practical Length of Antenna
  -  20 kh - Lemda = c/f
  - h = c/f = 3*10^8 m/s / 20 * 10^3  = 15 Km
#### 2. Narrow Banding of Signal 
  - AM - Band
#### 3. Multiplexing 
  - Many into one 
  - eg TV Signal 

### 1 . Construct Amplitude modulation , & plot signal for over modulation , Undermodulation & 100% modulation
```matlab
clc;
close all;
clear all;

fm = input ("Enter message Frequency");
am = input ('Enter message amplitude');
fc = input('Enter Carrier frequency ');
ac = input ('Enter Carrier amplitude');

t = 0:0.001:1;

m = am * sin(2*pi*fm*t);
c = ac * sin(2*pi*fc*t);
x = m.*c;
mod = x + (ac.*c);
subplot(3,1,1);
plot(t,m);
xlabel({'Time (sec) '; 'Fig 1:a'});
ylabel('Amplitude(v)');
title('Message Signal / Nikash / 39 ');
legend('msg');
subplot(3,1,2);
plot(t,c);
xlabel({'Time (sec) '; 'Fig 1:b'});
ylabel('AMP (V) ');
title('Carrier Signal / Nikash / 39 ');
legend('Carrier');
Subplot(3,1,3);
plot(t,mod);
xlabel({'Time (sec)'; 'Fig 1: C'});
ylabel('Amplitude (v)');
title('Amplitude Modulation / Nikash / 39');
legend('AM');

```
```
Input Values :

Over = 10 , 10 , 100 , 5 
100% = 10 , 5 , 100 , 10 
Under = 10 , 3 , 100 , 10 

```

### 2 . Construct frequency Modulation , & plot signals 

```matlab
clc;
close all;
clear all;

fm = input ("Enter message Frequency");
am = input ('Enter message amplitude');
fc = input('Enter Carrier frequency ');
ac = input ('Enter Carrier amplitude');
kf = input('Enter Frequency Sensitivity ');


t = 0:0.001:1;

x = am * cos(2*pi*fm*t);
c = ac * cos(2*pi*fc*t);
b = (kf * am)/fm;

A = ac .* cos(2*pi*fc*t + (b.*sin(2*pi*fm*t)));
subplot(3,1,1);
plot(t,x);
xlabel({'Time (sec) '; 'Fig 2:a'});
ylabel('Amplitude(v)');
title('Message Signal / Nikash / 39 ');
legend('msg');
subplot(3,1,2);
plot(t,c);
xlabel({'Time (sec) '; 'Fig 2:b'});
ylabel('AMP (V) ');
title('Carrier Signal / Nikash / 39 ');
legend('Carrier');
Subplot(3,1,3);
plot(t,A);
xlabel({'Time (sec)'; 'Fig 2: C'});
ylabel('Amplitude (v)');
title('Amplitude Modulation / Nikash / 39');
legend('FM');
```
```
Input Values :
fm = 25 
am = 10
fc = 400
ac = 10 
kf = 10 
```


### 3 . Construct Phase Modulation , & plot signals

```matlab
clc;
close all;
clear all;

fm = input ("Enter message Frequency");
am = input ('Enter message amplitude');
fc = input('Enter Carrier frequency ');
ac = input ('Enter Carrier amplitude');
b = input('enter modulation index');


t = 0:0.001:1;

x = am * sin(2*pi*fm*t);
c = ac * sin(2*pi*fc*t);

A = ac.*cos(2*pi*fc*t + (b.*sin(2*pi*fm*t)));
subplot(3,1,1);
plot(t,x);
xlabel({'Time (sec) '; 'Fig 2:a'});
ylabel('Amplitude(v)');
title('Message Signal / Nikash / 39 ');
legend('msg');
subplot(3,1,2);
plot(t,c);
xlabel({'Time (sec) '; 'Fig 2:b'});
ylabel('AMP (V) ');
title('Carrier Signal / Nikash / 39 ');
legend('Carrier');
subplot(3,1,3);
plot(t,A);
xlabel({'Time (sec)'; 'Fig 2: C'});
ylabel('Amplitude (v)');
title('Amplitude Modulation / Nikash / 39');
legend('FM');
```
```
Input Values :
fm = 10 
am = 10
fc = 100
ac = 10
b = 4
```