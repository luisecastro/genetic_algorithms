import numpy as np
import struct

def string_to_array(string):
    return np.array([int(x) for x in string])

def array_to_string(array):
    return ''.join([str(x) for x in array])

def binary_to_decimal(binary):
    return int(''.join(['0b', binary]),base=2)

def fitness(chromosome):
    return np.abs(chromosome**2-1023*chromosome)

def selection_probability(population_fitness, minimize=True):
    reproduction_probability = population_fitness / np.mean(population_fitness)
    reproduction_probability /= np.sum(reproduction_probability)
    if minimize:
        reproduction_probability = np.ones(len(reproduction_probability)) - reproduction_probability
        reproduction_probability /= np.sum(reproduction_probability)
    return reproduction_probability

def floatToRawLongBits(value):
	return struct.unpack('Q', struct.pack('d', value))[0]

def longBitsToFloat(bits):
	return struct.unpack('d', struct.pack('Q', bits))[0]
