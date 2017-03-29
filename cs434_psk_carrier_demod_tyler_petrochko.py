import numpy as np
import scipy
import sys
import math

def compl_to_idx(comp):
    if(comp.real > 0 and comp.imag > 0):
        return 11
    elif(comp.real < 0 and comp.imag > 0):
        return 10
    elif(comp.real < 0 and comp.imag < 0):
        return 0
    elif(comp.real > 0 and comp.imag < 0):
        return 1

def bpsk(out_file, symbols_file):
    correct = 0
    incorrect = 0
    bpsk = scipy.fromfile(out_file, dtype=scipy.complex64)
    bpsk_sym = scipy.fromfile(symbols_file, dtype=scipy.complex64)

    length = min(len(bpsk), len(bpsk_sym))

    i = 0 # absolute index
    block_i = 0 # index into block
    block_total = 0 # block sum
    block_index = 0

    while(i < length):
        block_total += bpsk[i].real * math.cos(2 * math.pi * (block_i / 4))
        
        if(block_i == 63):
            expected = block_total
            actual = bpsk_sym[block_index].real
            print 'actual: ', actual, ' expected: ', expected
            if((expected > 0 and actual > 0) or (expected < 0 and actual < 0)):
                correct += 1
            else:
                incorrect += 1
            i += 1
            block_i = 0
            block_total = 0
            block_index += 1
        else:
            i += 1
            block_i += 1
    print 'Incorrect: ', incorrect
    print 'Correct: ', correct
    print 'Error rate for bpsk is ', float(incorrect) / (incorrect + correct)

def qpsk(out_file, symbols_file):
    correct = 0
    incorrect = 0
    qpsk = scipy.fromfile(out_file, dtype=scipy.complex64)
    qpsk_sym = scipy.fromfile(symbols_file, dtype=scipy.complex64)

    length = min(len(qpsk), len(qpsk_sym))

    i = 0 # absolute index
    block_i = 0 # index into block
    block_index = 0

    block_total00 = 0 # block sums!
    block_total01 = 0
    block_total10 = 0
    block_total11 = 0

    while(i < length):
        block_total11 += qpsk[i].real * math.cos(2 * math.pi * (float(block_i) / 4) + ((math.pi * 1)/4))
        block_total10 += qpsk[i].real * math.cos(2 * math.pi * (float(block_i) / 4) + ((math.pi * 3)/4))
        block_total00 += qpsk[i].real * math.cos(2 * math.pi * (float(block_i) / 4) + ((math.pi * 5)/4))
        block_total01 += qpsk[i].real * math.cos(2 * math.pi * (float(block_i) / 4) + ((math.pi * 7)/4))

        best = max(block_total00, block_total01, block_total10, block_total11)

        if(best == block_total00 and compl_to_idx(qpsk_sym[block_index]) == 0):
            correct += 1
        elif(best == block_total01 and compl_to_idx(qpsk_sym[block_index]) == 1):
            correct += 1
        elif(best == block_total10 and compl_to_idx(qpsk_sym[block_index]) == 10):
            correct += 1
        elif(best == block_total11 and compl_to_idx(qpsk_sym[block_index]) == 11):
            correct += 1
        else:
            incorrect += 1

        if(block_i == 63):
            i += 1
            block_i = 0
            block_total = 0
            block_index += 1
        else:
            i += 1
            block_i += 1
    print 'Error rate for qpsk is ', float(incorrect) / (incorrect + correct)

# TODO actually use filename param
if(len(sys.argv) != 4):
    print 'Usage: cs434_psk_carrier_demod_tyler_petrochko [bpsk | qpsk] <output_file> <symbols_file>'
    exit()
if(sys.argv[1] == 'bpsk'):
    print 'Analyzing bpsk'
    bpsk(sys.argv[2], sys.argv[3])
elif(sys.argv[1] == 'qpsk'):
    print 'Analyzing qpsk'
    qpsk(sys.argv[2], sys.argv[3])
else:
    print 'Usage: cs434_psk_carrier_demod_tyler_petrochko [bpsk | qpsk] <output_file> <symbols_file>'
    exit()



