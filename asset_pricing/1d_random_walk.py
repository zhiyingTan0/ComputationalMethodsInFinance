import datetime
import tracemalloc
import numpy as np
from memory_profiler import memory_usage
import psutil


""" Simulate a 1D random walk and calculate the probability of returning to the origin after N steps simulations."""
""" S_t = S_t-1 + epsilon where epsilon a bernoulli r.v. """

N = 10 # N steps of random walk
p = 0.52 # probability of move +1
num_trials = 1000000 #number of experiments

"""Method 1 : for loop"""
def simulate_random_walk(N, p):
    """walk for N steps"""
    pos=5
    for _ in range(N):
        pos+=np.random.choice([1, -1], p=[p, 1 - p])
        if pos <=0 :
            return pos
    return pos

def calculate_probability(N, p, num_trials):
    return_to_origin = 0
    for _ in range(num_trials):
        final_pos = simulate_random_walk(N, p)
        if final_pos <= 0:
            return_to_origin += 1
    return return_to_origin/num_trials


"""Method 2: Numpy"""
def simulate_random_walk_numpy(N, p, num_trials):
    pos=5
    samples = np.random.binomial(n=1, p=p, size=num_trials*N).reshape(num_trials,N)*2-1
    estimate_prob = np.sum((np.cumsum(samples, axis=1)+pos <= 0).any(axis=0) ) / num_trials
    return estimate_prob



if __name__ == "__main__":
    """
    Measuring peak memory usage 
    """
    print("Measuring Method 1 (Python loops)...")
    mem_usage_method1 = memory_usage((calculate_probability, (N, p, num_trials)))

    print("Measuring Method 2 (NumPy)...")
    mem_usage_method2 = memory_usage((simulate_random_walk_numpy, (N, p, num_trials)))

    print(f"Peak memory usage - Method 1: {max(mem_usage_method1):.2f} MB")
    print(f"Peak memory usage - Method 2: {max(mem_usage_method2):.2f} MB")


    """ 
    Measuring runtime and memory block size/count 
    """
    print("Measuring Method 1 (Python loops)...")
    tracemalloc.start()
    curr = datetime.datetime.now()
    print(f"Method 1 - Probability of return to origin after {N} step Ramdom walk is "
          f"{calculate_probability(N,p,num_trials): .5f} with runtime={datetime.datetime.now()-curr}")
    snapshot_method1 = tracemalloc.take_snapshot()
    tracemalloc.stop()

    print("Measuring Method 2 (NumPy)...")
    tracemalloc.start()
    curr= datetime.datetime.now()
    print(f"Method 2 - Probability of return to origin after {N} step Ramdom walk is "
          f"{simulate_random_walk_numpy(N,p,num_trials): .5f} with runtime={datetime.datetime.now()-curr}")
    snapshot_method2 = tracemalloc.take_snapshot()
    tracemalloc.stop()

    print("Top memory blocks for Method 1:")
    for stat in snapshot_method1.statistics("lineno")[:5]:
        print(stat)

    print("\nTop memory blocks for Method 2:")
    for stat in snapshot_method2.statistics("lineno")[:5]:
        print(stat)

