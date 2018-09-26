import numpy as np

def string_to_array(string):
    return np.array([int(x) for x in string])

def array_to_string(array):
    return ''.join([str(x) for x in array])

def binary_to_decimal(binary):
    return int(binary,base=2)

def fitness(chromosome):
    chromosome_decimal = binary_to_decimal(chromosome)
    return np.abs(chromosome_decimal**2-1023*chromosome_decimal)

def selection_probability(population_fitness, minimize=True):
    reproduction_probability = population_fitness / np.mean(population_fitness)
    reproduction_probability /= np.sum(reproduction_probability)
    if minimize:
        reproduction_probability = np.ones(len(reproduction_probability)) - reproduction_probability
        reproduction_probability /= np.sum(reproduction_probability)
    return reproduction_probability
