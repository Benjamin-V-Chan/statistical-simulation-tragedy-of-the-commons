import os
import pandas as pd
from utils import simulate_tragedy_commons

def main():
    population_size = 100
    generations = 200
    initial_coop_fraction = 0.5
    initial_resource = 1000.0
    regeneration_rate = 0.1
    carrying_capacity = 1000.0
    cooperator_consumption = 1.0
    defector_consumption_multiplier = 2.0
    mutation_rate = 0.01
    replicates = 10

    os.makedirs("outputs", exist_ok=True)
    replicate_results = []
    for rep in range(replicates):
        df = simulate_tragedy_commons(population_size, generations, initial_coop_fraction, 
                                       initial_resource, regeneration_rate, carrying_capacity, 
                                       cooperator_consumption, defector_consumption_multiplier, mutation_rate)
        df["replicate"] = rep
        replicate_results.append(df)
    simulation_data = pd.concat(replicate_results, ignore_index=True)
    simulation_data.to_csv("outputs/simulation_results.csv", index=False)

if __name__ == '__main__':
    main()
