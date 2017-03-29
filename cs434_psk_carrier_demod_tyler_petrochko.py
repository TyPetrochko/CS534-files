import numpy as np
import sys
import math

def bpsk():
    bpsk = np.fromfile('bpsk_out', dtype=float)
    bpsk_sym = np.fromfile('bpsk_symbols_out', dtype=complex)

    length = min(len(bpsk), len(bpsk_sym))

    i = 0 # absolute index
    block_i = 0 # index into block
    block_total = 0 # block sum
    block_index = 0

    while(i < length):
        block_total += bpsk[i].real * math.cos(2 * math.pi * (block_i / 4))
        
        if(block_i == 63):
            print 'Compare ', block_total, ' vs ', bpsk_sym[block_index].real
            i += 1
            block_i = 0
            block_total = 0
            block_index += 1
        else:
            i += 1
            block_i += 1

def qpsk():
    print 'TODO'

# TODO actually use filename param
if(len(sys.argv) != 3):
    print 'Usage: [bpsk | qpsk] <filename>'
    exit()
if(sys.argv[1] == 'bpsk'):
    print 'Analyzing bpsk'
    bpsk()
elif(sys.argv[1] == 'qpsk'):
    print 'Analyzing qpsk'
    qpsk()
else:
    print 'Usage: [bpsk | qpsk] <filename>'
    exit()


