import sounddevice as sd

# fs -> frequência de amostragem do sinal de entrada
# data -> conteudo do sinal de entrada
def play(fs, data):
    sd.play(data, fs)
    sd.wait()