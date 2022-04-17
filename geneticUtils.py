"""
Methods for genetic agents and breeding
"""
import random as r
import struct
from bitstring import *


# converts a string of 1's & 0's to a float
def bitstring_to_float(s):
    return BitArray(bin=s).float


# converts a string of 1's & 0's to its 2's complement
def bitstring_to_twos_complement(s):
    sum = 0
    sum -= int(s[0]) * (2**(len(s)-1))
    for i in range(len(s)-1):
        sum += int(s[i+1]) * (2**(len(s)-(i+2)))
    return sum


# performs mutation on a genome
def mutation(specimen, prob):
    spec = [let for let in specimen]
    for i in range(len(spec)):
        if r.random() < prob:
            spec[i] = str((int(spec[i]) + 1) % 2)
    return reduce(str.__add__, spec)


# process of creating a child
def mate(par1, par2, cr_prob, mut_prob):
    childa = ''
    childb = ''
    if r.random() < cr_prob:
        mirr_pnt = r.randint(0, len(par1))
        childa += par1[:mirr_pnt]
        childa += par2[mirr_pnt:]
        childb += par2[:mirr_pnt]
        childb += par1[mirr_pnt:]
    else:
        childa = par1
        childb = par2
    return mutation(childa, mut_prob), mutation(childb, mut_prob)


# take a generation of individuals, use fitness to rank, and then mate based on fitness
def evolve(generation, fitness_fn, mating_size, cr_prob, mut_prob):
    # take all of the parents
    # uniformly select n of them w/o replacement
    # pick highest fitness
    # let them "choose" best mate
    # mate them, and repeat with others
    next_generation = []
    results = []
    generation = sorted([(spec, fitness_fn(spec)) for spec in generation], key=lambda x: x[1])
    generation = generation[3*len(generation)/4:] * 4
    while generation:
        if len(generation) >= mating_size:
            pool = r.sample(generation, mating_size)
        else:
            pool = generation
        pool = sorted(pool, key=lambda x: x[1])
        best = pool[-1]  # higher fitness is better
        mte = pool[-2]
        res = mate(best[0], mte[0], cr_prob, mut_prob)
        next_generation.append(res[0])
        next_generation.append(res[1])
        results.append(best[1])
        results.append(mte[1])
        generation.remove(best)
        generation.remove(mte)
    return next_generation, results
