import os
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import simulate_tragedy_commons

def main():
    population_size = 100
    generations = 200
    initial_resource = 1000.0
    regeneration_rate = 0.1
    carrying_capacity = 1000.0
    cooperator_consumption = 1.0
    replicates = 5

    # Define parameter grids
    initial_coop_fractions = [0.2, 0.5, 0.8]
    defector_multipliers = [1.5, 2.0, 3.0]
    mutation_rates = [0.0, 0.01, 0.05]

    results_list = []
    for ic, dm, mr in itertools.product(initial_coop_fractions, defector_multipliers, mutation_rates):
        final_resources = []
        final_coop_fracs = []
        final_payoffs = []
        for _ in range(replicates):
            df = simulate_tragedy_commons(population_size=population_size, generations=generations, 
                                          initial_coop_fraction=ic, initial_resource=initial_resource, 
                                          regeneration_rate=regeneration_rate, carrying_capacity=carrying_capacity, 
                                          cooperator_consumption=cooperator_consumption, 
                                          defector_consumption_multiplier=dm, mutation_rate=mr)
            final_row = df.iloc[-1]
            final_resources.append(final_row["resource"])
            final_coop_fracs.append(final_row["fraction_cooperators"])
            final_payoffs.append(final_row["avg_payoff"])
        results_list.append({
            "initial_coop_fraction": ic,
            "defector_multiplier": dm,
            "mutation_rate": mr,
            "final_resource_mean": np.mean(final_resources),
            "final_coop_fraction_mean": np.mean(final_coop_fracs),
            "final_payoff_mean": np.mean(final_payoffs)
        })
