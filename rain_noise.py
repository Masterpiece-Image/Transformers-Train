import os
import argparse
import random

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc

parser = argparse.ArgumentParser()
parser.add_argument('--sig2noise_ratio', type=float, default=10, help="Rapport signal sur bruit")
parser.add_argument('--data_path', type=str, default='')
parser.add_argument('--save_path', type=str, default='')
opt = parser.parse_args()

#################################################
#                                               #
#  Generate y such that y = signal + α * noise  #
#                                               #
#             /      SNR                        #
#   with α = {  _______________                 #
#             \ 10pow(SNRdb/10)                 #
#                                               #
#################################################
def add_rain_noise(signal, SNR) :

    # create rain noise.
    # . . .

    # Evaluate signal power and noise power
    # . . . 

    # Evaluate α
    # . . .

    # y = s + α * n
    # don't forget to normalize
    # . . .

    # return y
    # . . . 
    
    pass


if __name__ == '__main__' :
    image = plt.imread('./image/260.jpg')
    # plt.imshow(image)
    # plt.show()
    print(image.shape)
    empty_noise = np.zeros(image.shape)
    print(empty_noise.shape)

    plt.imshow(empty_noise)
    plt.show()



    # entier aléatoire ==> rand.randint(start, stop+1)


