import numpy
from hamming import hamming
from lowpass import lowpass

# fs -> frequência do sinal de entrada (Hz)
# fc -> frequência de corte (Hz)
# bt -> largura da banda de transição (Hz)
def filter(fs, fc, bt):

    # atenuação mínima, em decibéis (dB), que o filtro deve proporcionar na banda de rejeição especificada.
    # é utilizado o valor de 0.01 como referência para a atenuação mínima desejada, o que corresponde a uma atenuação de -20 dB.
    # valor comum para filtros digitais que exigem uma boa atenuação na banda de rejeição.
    # A = -20 * numpy.log10(0.3)

    # ordem do filtro, utilizando a função ceil para arredondar e somando 1 para compensar a ordem ser arredondada para cima
    # a constante 2.285 é um fator de escala que ajuda a ajustar a banda de transição e a largura de banda do filtro.
    # M = numpy.ceil((A - 8) / (2.285 * bt / fs)) + 1

    M = numpy.ceil(3.3 * 2 * numpy.pi / bt)

    # janela de hamming
    w, n = hamming(M)

    # resposta ao impulso ideal do passa-baixas
    lp_ideal = lowpass(fs, fc, M, n)
    
    # multiplicação da resposta ao impulso ideal pela janela de Hamming, resultando na resposta ao impulso do filtro passa-baixas com
    # janela de Hamming
    lp = lp_ideal * w
    
    M = int(M)

    return lp, w, n, M