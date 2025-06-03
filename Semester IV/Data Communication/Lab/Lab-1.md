# Matlab Code & Output 
# Continuous sine wave

```matlab
clc;
close all;
clear all;
a = 5;
f = 3;
t = 0:0.001:1
x = a*sin(2*pi*f*t);
plot(t,x,'blue');
xlabel('<- Time ->');
ylabel('<- Amplitude ->');
title('Continuous Sine wave / Nikash Lamsal / 39');
grid on;
```

---

### ✅ Continuous Sine wave output:

![Sine Wave](./Output%20Store/cont%20sine%20wave.svg)

# Discrete sine wave

```matlab
clc;
close all;
clear all;
a = 5;
f = 3;
t = 0:0.01:1
x = a*sin(2*pi*f*t);
stem(t,x,'Blue');
xlabel('<- Time ->');
ylabel('<- Amplitude ->');
title('Discrete Sine wave / Nikash Lamsal / 39');
grid on;

```

---

### ✅ Discrete Sine wave output:

![Sine Wave](./Output%20Store/dic%20sine%20wave.svg)

# Continuous Cosine wave

```matlab
clc;
close all;
clear all;
a = 5;
f = 3;
t = 0:0.001:1
x = a*cos(2*pi*f*t);
plot(t,x,'blue');
xlabel('<- Time ->');
ylabel('<- Amplitude ->');
title('Continuous Cosine wave / Nikash Lamsal / 39');
grid on;

```

---

### ✅ Continuous Cosine wave output:

![cosine Wave](./Output%20Store/cont..%20cosine%20wave.svg)


# Discrete Cosine wave

```matlab
clc;
close all;
clear all;
a = 5;
f = 3;
t = 0:0.01:1
x = a*cos(2*pi*f*t);
stem(t,x,'Blue');
xlabel('<- Time ->');
ylabel('<- Amplitude ->');
title('Discrete Cosine wave / Nikash Lamsal / 39');
grid on;

```

---

### ✅ Discrete Cosine wave output:

![cosine Wave](./Output%20Store/disc..cosine%20wave.svg)



# Combine wave

```matlab
clc;
clear;
close all;

a = 5;
f = 3;
t = 0:0.01:1;

x = a * sin(2 * pi * f * t);
y = a * cos(2 * pi * f * t);

subplot(2,2,1);
stem(t, x, 'b');
xlabel('Time');
ylabel('Amplitude');
title('Discrete Sine / Nikash / 39');
grid on;

subplot(2,2,2);
plot(t, x, 'r');
xlabel('Time');
ylabel('Amplitude');
title('Continuous Sine / Nikash / 39');
grid on;

subplot(2,2,3);
stem(t, y, 'g');
xlabel('Time');
ylabel('Amplitude');
title('Discrete Cosine / Nikash / 39');
grid on;

subplot(2,2,4);
plot(t, y, 'm');
xlabel('Time');
ylabel('Amplitude');
title('Continuous Cosine / Nikash / 39');
grid on;


```

### ✅ Combine wave output:

![Combine Wave](./Output%20Store/all.svg)
