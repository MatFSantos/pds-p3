import numpy

# fs -> frequência de amostragem do sinal de entrada
# fc -> frequência de corte
# N -> ordem do filtro passa-baixas
# n -> # vetor com valores igualmente espassados, de 0 até N-1
def lowpass(fs, fc, N, n):

    # frequencia de corte normalizada pela frequencia de amostragem do sinal de entrada
    # fc_norm = fc / fs
    
    # é gerada uma resposta ao impulso ideal do passa-baixas, que nada mais é que uma sinc multiplicada pela 
    # frequencia de corte normalizada "fc_norm"
    ideal =  numpy.sin(fc * (n - (N - 1) / 2))/ (numpy.pi * ( n - (N - 1) / 2))
    return ideal