import numpy as np
import pandas as pd

def simulate_tragedy_commons(population_size=100, generations=200, 
                              initial_coop_fraction=0.5, initial_resource=1000.0,
                              regeneration_rate=0.1, carrying_capacity=1000.0,
                              cooperator_consumption=1.0, defector_consumption_multiplier=2.0,
                              mutation_rate=0.01):
    # Initialize agent strategies (1 for cooperator, 0 for defector)
    agents = np.random.choice([1, 0], size=population_size, p=[initial_coop_fraction, 1-initial_coop_fraction])
    resource = initial_resource
    results = []
    
    for gen in range(generations):
        # Determine planned consumption per agent
        consumption = np.where(agents == 1, cooperator_consumption, cooperator_consumption * defector_consumption_multiplier)
        total_demand = consumption.sum()
        # Scale consumption if demand exceeds resource
        scale = 1.0 if total_demand <= resource else resource / total_demand
        actual_consumption = consumption * scale
        payoffs = actual_consumption.copy()
        total_consumption = actual_consumption.sum()
        
        # Update resource using logistic regeneration minus consumption
        resource = resource + regeneration_rate * resource * (1 - resource / carrying_capacity) - total_consumption
        if resource < 0: resource = 0.0
        
        # Reproduction: sample new generation proportional to payoffs
        if payoffs.sum() > 0:
            probabilities = payoffs / payoffs.sum()
        else:
            probabilities = np.ones(population_size) / population_size
        new_agents = np.random.choice(agents, size=population_size, p=probabilities)
        # Mutation: flip strategy with given probability
        mutations = np.random.rand(population_size) < mutation_rate
        new_agents[mutations] = 1 - new_agents[mutations]
        agents = new_agents.copy()
        
        frac_cooperators = np.mean(agents)
        avg_payoff = np.mean(payoffs)
        results.append({"generation": gen, "resource": resource, 
                        "fraction_cooperators": frac_cooperators, "avg_payoff": avg_payoff})
    return pd.DataFrame(results)
