import numpy as np
import scipy

print 'BEGIN BPSK'
bpsk = scipy.fromfile('bpsk_out', dtype=scipy.complex64)
bpsk_sym = scipy.fromfile('bpsk_symbols_out', dtype=scipy.complex64)

length = min(len(bpsk), len(bpsk_sym))

for i in range(0, length - 1):
    print bpsk[i], bpsk_sym[i]

print 'BEGIN QPSK'
qpsk = scipy.fromfile('qpsk_out', dtype=scipy.complex64)
qpsk_sym = scipy.fromfile('qpsk_symbols_out', dtype=scipy.complex64)

length = min(len(qpsk), len(qpsk_sym))

for i in range(0, length - 1):
    print qpsk[i], qpsk_sym[i]


