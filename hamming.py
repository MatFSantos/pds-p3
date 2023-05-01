from numpy import arange, cos, pi

# M -> comprimento do filtro passa-baixas
def hamming(M):

    # vetor com valores igualmente espassados, de 0 até M-1
    n = arange(M)

    # função da janela de hamming, caculada com base no comprimento passada
    w = 0.54 - 0.46 * cos(2 * pi * n / (M - 1))
    return w, n