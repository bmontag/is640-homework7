import random
import statistics
from collections import Counter

RANDOM_SEED = 2020
NUMBER_COUNT = 20
RANGE_MIN = 100
RANGE_MAX = 120

DISPLAY_MEDIAN = "Median is: {:g}"
DISPLAY_MODE = "Mode is: {}"
DISPLAY_MODES = "Modes are: {}"

random.seed(RANDOM_SEED)

def get_median(nbrs):
    return statistics.median(nbrs)
    
def get_mode(nbrs):

    occurences = Counter(nbrs).items()
    sorted_occurences = dict(sorted(occurences, key=lambda x: x[1], reverse=True))
    
    if len(sorted_occurences) == 0:
        return []

    top_occurence_count = list(sorted_occurences.values())[0]
    top_occurence_values = []
    
    for (occurence_value, count) in sorted_occurences.items():
        if count != top_occurence_count:
            break
        top_occurence_values.append(occurence_value)

    return sorted(top_occurence_values)

def generate_random_nbrs(k):

    nbrs = []
    
    for _ in range(0, k):
        nbr = random.randint(RANGE_MIN, RANGE_MAX)
        nbrs.append(nbr)

    return nbrs

def task1():

    random_nbrs = generate_random_nbrs(NUMBER_COUNT)
    print(random_nbrs)

    median = get_median(random_nbrs)
    print(DISPLAY_MEDIAN.format(median))
    
    mode_array = get_mode(random_nbrs)
    if len(mode_array) == 1:
        print(DISPLAY_MODE.format(mode_array[0]))
    else:
        modes = ", ".join(map(str, mode_array))
        print(DISPLAY_MODES.format(modes))

task1()
