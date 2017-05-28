#coding:utf8
import scipy
import scipy.signal as ss
from matplotlib import pyplot as pp
import numpy as np
import scipy.signal
from pylab import *

N = 255
fc = 1000.
fc2 = 3000.
Fs = 44100.

#%% LPF
h = ss.firwin(numtaps=N, cutoff=fc/(Fs/2.), window='blackman', pass_zero=True)

#%% HPF
f = ss.firwin(numtaps=N, cutoff=fc/(Fs/2.), window='blackman', pass_zero=False)

#%% BPF
e = ss.firwin(numtaps=N, cutoff=scipy.array([fc/(Fs/2.), fc2/(Fs/2.)]), window='blackman', pass_zero=False)

#%% BEF
h = ss.firwin(numtaps=N, cutoff=scipy.array([fc/(Fs/2.), fc2/(Fs/2.)]), window='blackman', pass_zero=True)

#%% 表示
f = scipy.array(range(0, N)) * Fs / scipy.double(N)
tf = scipy.fft(h)
mag = scipy.absolute(tf)
phase = scipy.unwrap(scipy.angle(tf)) * 180. / scipy.pi

figure(1)
subplot(3,1,1)
pp.plot(h)
grid('on', 'both')
subplot(3,1,2)
pp.semilogx(f, mag)
xlim([20, 20000])
ylim([0, 1.2])
grid('on', 'both')
subplot(3,1,3)
pp.plot(f, phase)
xlim([0, 20000])
grid('on', 'both')

figure(2)
subplot(3,1,1)
pp.plot(f)
grid('on', 'both')
subplot(3,1,2)
pp.semilogx(f, mag)
xlim([20, 20000])
ylim([0, 1.2])
grid('on', 'both')
subplot(3,1,3)
pp.plot(f, phase)
xlim([0, 20000])
grid('on', 'both')

figure(3)
subplot(3,1,1)
pp.plot(e)
grid('on', 'both')
subplot(3,1,2)
pp.semilogx(f, mag)
xlim([20, 20000])
ylim([0, 1.2])
grid('on', 'both')
subplot(3,1,3)
pp.plot(f, phase)
xlim([0, 20000])
grid('on', 'both')

plt.show()