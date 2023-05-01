from scipy.io import wavfile
from matplotlib import pyplot as plt
from numpy import fft, abs, arange, abs, log10, convolve, pi
from filter import filter
from play import play

fc = 3000 # frequência de corte
bt = 1500 # banda de transição (intervalo onde o filtro transita de 1, banda de passagem, para 0, banda de rejeição)

fs, data = wavfile.read('audio.wav') # abre arquivo de audio
play(fs, data) # executa arquivo de audio

wc = 2 * pi * fc / fs
wt = 2 * pi * bt / fs 

# os.remove("./audio_sem_ruido.wav")
plt.figure(1)
plt.plot(data)
plt.ylim([-2,2])
plt.xlabel('Tempo (amostras)')
plt.ylabel('Amplitude')
plt.grid()

lp, w, n, N = filter(fs, wc, wt)

# Plotar a resposta em frequência do filtro
f = arange(0, fs / 2, fs / (2 * N))
H = fft.fft(lp, 2 * N)
H_db = 20 * log10(abs(H[:N]))
plt.figure(2)
plt.plot(f,H_db)
plt.xlim([0, fs / 2])
plt.ylim([-80, 5])
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid()

# Plotar a janela de Hamming
plt.figure(3)
plt.plot(n, w)
plt.xlabel('Amostra')
plt.ylabel('Amplitude')
plt.title('Janela de Hamming')

# Plotar a resposta ao impulso do filtro
plt.figure(4)
plt.stem(n, lp)
plt.xlabel('Amostra')
plt.ylabel('Amplitude')
plt.title('Resposta ao impulso do filtro')

# Calcula a transformada de Fourier do sinal
fft_data = fft.fft(data)

# Calcula o espectro de frequências
freqs = fft.fftfreq(len(data), 1/fs)
spectrum = abs(fft_data)

# Plota o espectro de frequências
plt.figure(5)
plt.plot(freqs, spectrum)
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')

# Aplica o filtro no sinal
signal_filtered =  convolve(lp, data)

# Plota o sinal filtrado no tempo
plt.figure(6)
plt.plot(signal_filtered)
plt.ylim([-1.5,1.5])
plt.xlabel('Tempo (amostras)')
plt.ylabel('Amplitude')

# Calcula o espectro de frequências do sinal filtrado
fft_filtered_data = fft.fft(signal_filtered)
freqs = fft.fftfreq(len(signal_filtered), 1/fs)
spectrum_filtered = abs(fft_filtered_data)

# Plota o espectro de frequências do sinal filtrado
plt.figure(7)
plt.plot(freqs, spectrum_filtered)
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')


# Reproduz o sinal filtrado
play(fs, signal_filtered)
plt.show()

wavfile.write("./audio_sem_ruido.wav", fs, signal_filtered)
