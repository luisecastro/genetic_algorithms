import numpy as np
from utils import string_to_array, array_to_string, longBitsToFloat, floatToRawLongBits

class genetic_algorithm(object):
    def __init__(self, generations, population_size, fitness_function,
                 lower_limit, upper_limit, selection_probability_function, pc=1.0, pm=0.001, seed=0):
        self.generations = generations
        self.population_size = population_size
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.fitness = fitness_function
        self.selection_probability = selection_probability_function
        self.pc = pc
        self.pm = pm
        self.seed = seed
        self.fitness_log = []
        self.population_log = []
        np.random.seed(self.seed)
        
    def create_random_population(self):
        initial_population = np.random.uniform(self.lower_limit, self.upper_limit, self.population_size)
        initial_population = np.array([bin(floatToRawLongBits(chromosome))[2:] for chromosome in initial_population])
        for pop in initial_population: print(len(pop))
        return initial_population

    def mutation(self, chromosome):
        chromosome_array = string_to_array(chromosome)
        flip = np.random.uniform(size=len(chromosome)) <= self.pm
        return array_to_string(chromosome_array ^ flip)

    def crossover(self, chromosomeA, chromosomeB):
        locus = np.random.randint(1, np.min([len(chromosomeA),len(chromosomeB)]))
        if np.random.random() <= self.pc:
            chromosomeAB = ''.join([chromosomeA[:locus],chromosomeB[locus:]])
            chromosomeBA = ''.join([chromosomeB[:locus],chromosomeA[locus:]])
            return chromosomeAB, chromosomeBA
        return chromosomeA, chromosomeB

    def selection(self, population):
        population_fitness = np.array([self.fitness(longBitsToFloat(int(''.join(['0b', chromosome]),2))) for chromosome in population])
        #population_fitness = np.array([self.fitness(chromosome) for chromosome in population])
        self.fitness_log.append([np.max(population_fitness), np.mean(population_fitness), np.min(population_fitness)])
        reproduction_probability = self.selection_probability(population_fitness)
        selected_population = np.random.choice(a = [*range(self.population_size)],
                                               size=self.population_size, p=reproduction_probability)
        return selected_population

    def pairing(self, selected_chromosomes, population):
        new_population = []
        for i in range(0,len(selected_chromosomes),2):
            chromosomeAB, chromosomeBA = self.crossover(population[selected_chromosomes[i]], population[selected_chromosomes[i+1]])
            new_population.append(self.mutation(chromosomeAB))
            new_population.append(self.mutation(chromosomeBA))
        self.population_log.append(new_population)
        return np.array(new_population)

    def run(self):
        self.initial_population = self.create_random_population()
        population = self.initial_population.copy()
        countdown = self.generations
        while countdown != 0:
            selected_chromosomes = self.selection(population)
            population = self.pairing(selected_chromosomes, population)
            countdown -= 1
        self.last_population = population
