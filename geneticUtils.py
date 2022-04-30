"""
Methods for genetic agents and breeding
"""
import random as r
import struct


def bitstring_to_float(s):
    """
    converts a string of 1's & 0's to a float
    """
    return struct.unpack('!f', struct.pack('!I', int(s, 2)))[0]


def bitstring_to_twos_complement(s):
    """
    converts a string of 1's & 0's to its 2's complement
    """
    sm = 0
    sm -= int(s[0]) * (2 ** (len(s) - 1))
    for i in range(len(s)-1):
        sm += int(s[i + 1]) * (2 ** (len(s) - (i + 2)))
    return sm


def cull_int(cull_prop):
    """
    Get the denominator of a fraction, up to a 1000 (to prevent infinite loop)
    Admittedly this isn't the best way to do this
    """
    i = 1
    while i < 1000:
        if i*cull_prop%1 == 0:
            return i
        i += 1


def mutation(specimen, prob):
    """
    performs mutation on a genome with a given probability
    """
    spec = [let for let in specimen]
    for i in range(len(spec)):
        if r.random() < prob:
            spec[i] = str((int(spec[i]) + 1) % 2)
    return reduce(str.__add__, spec)


def mate(par1, par2, cr_prob, mut_prob):
    """
    process of creating a child
    """
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
def evolve(generation, fitnss_fn, mating_size=20, cr_prob=0.80, mut_prob=None, elitism_size=0, cull_prop=0.5, repl=False):
    """
     Method to evolve a poplutaion of individuals based on the fitness function
     Params:
     -generation: List of bitstrings representing the generation
     -fitnss_fn: function which gives a numerical value to bitstrings
     -mating_size: size of group randomly selected from the environment, from which best 2 individuals mate
     -cr_prob: the probability that crossover happens during mating
     -mut_prob: the probability that a bit is flipped when a child is made, this prob is applied to all bits in genome
     -elitism_size: the number of most fit individuals that go into the next generation untouched
     -cull_prop: the lower proportion not allowed to mate, as a float: i.e. lower only reproduce from top fourth
        then cull_prop=0.75 This value should be 0.5 or above. Additionally, the remaining fraction of the generation
        must divide the size of the whole generation. Eg. Numbers like (n-1)/n where n divides size of generation work
    """
    size = len(generation)
    if not mut_prob:
        mut_prob = 1/float(size)

    next_generation = []
    generation = sorted([(spec, fitnss_fn(spec)) for spec in generation], key=lambda x: x[1])
    if elitism_size > 0:
        next_generation += [spec[0] for spec in generation[-elitism_size:]]

    fitted = [spec[0] for spec in generation]
    results = [spec[1] for spec in generation]

    if cull_prop != 0:
        if (size * cull_prop) % 1 != 0 or cull_prop < 0.5:
            raise ValueError("generation size is not divisible into cull proportions")
        if repl:
            generation = generation[int(size*cull_prop):]
        else:
            generation = generation[int(size*cull_prop):] * cull_int(cull_prop)

    while len(next_generation) < size:
        if len(generation) >= mating_size:
            pool = r.sample(generation, mating_size)
        else:
            pool = generation
        pool = sorted(pool, key=lambda x: x[1])
        best = pool[-1]  # higher fitness is better
        mte = pool[-2]
        res = mate(best[0], mte[0], cr_prob, mut_prob)
        next_generation.append(res[0])
        if len(next_generation) == size:
            break
        next_generation.append(res[1])
        if not repl:
            generation.remove(best)
            generation.remove(mte)
    return next_generation, results, fitted
