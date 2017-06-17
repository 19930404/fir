#coding:utf8
import scipy
import scipy.signal as ss
from matplotlib import pyplot as pp
import numpy as np
import scipy.signal
from pylab import *

N = 255
N2 = 501
N3 = 751
fc = 1000.
fc2 = 3000.
Fs = 44100.

#%% LPF
h = ss.firwin(numtaps=N, cutoff=fc/(Fs/2.),  window='boxcar', pass_zero=True)
h2 = ss.firwin(numtaps=N2, cutoff=fc/(Fs/2.),  window='boxcar', pass_zero=True)
h3 = ss.firwin(numtaps=N3, cutoff=fc/(Fs/2.),  window='boxcar', pass_zero=True)
'''
boxcar, triang, blackman, hamming, hann, bartlett, flattop, parzen, bohman, blackmanharris, nuttall, barthann, kaiser (needs beta), gaussian (needs std), general_gaussian (needs power, width), slepian (needs width), chebwin (needs attenuation)
'''
#%% HPF
#f = ss.firwin(numtaps=N, cutoff=fc/(Fs/2.), window='blackman', pass_zero=False)

#%% BPF
#e = ss.firwin(numtaps=N, cutoff=scipy.array([fc/(Fs/2.), fc2/(Fs/2.)]), window='blackman', pass_zero=False)

#%% BEF
#h = ss.firwin(numtaps=N, cutoff=scipy.array([fc/(Fs/2.), fc2/(Fs/2.)]), window='blackman', pass_zero=True)

#%% 表示
f = scipy.array(range(0, N)) * Fs / scipy.double(N)
tf = scipy.fft(h)
mag = scipy.absolute(tf)
phase = scipy.unwrap(scipy.angle(tf)) * 180. / scipy.pi

f2 = scipy.array(range(0, N2)) * Fs / scipy.double(N2)
tf2 = scipy.fft(h2)
mag2 = scipy.absolute(tf2)
phase2 = scipy.unwrap(scipy.angle(tf2)) * 180. / scipy.pi

f3 = scipy.array(range(0, N3)) * Fs / scipy.double(N3)
tf3 = scipy.fft(h3)
mag3 = scipy.absolute(tf3)
phase3 = scipy.unwrap(scipy.angle(tf3)) * 180. / scipy.pi

figure(1)
pp.plot(h)
pp.plot(h2)
pp.plot(h3)
grid('on', 'both')
figure(2)
pp.semilogx(f, mag)
pp.semilogx(f2, mag2)
pp.semilogx(f3, mag3)
xlim([20, 20000])
ylim([-0.05, 1.2])
grid('on', 'both')
figure(3)
pp.plot(f, phase)
xlim([0, 20000])
grid('on', 'both')
'''
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
'''
plt.show()