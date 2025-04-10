# =====================================
#
# Import necessary packages (numpy, pandas).
#
# Define function simulate_tragedy_commons with parameters:
#   - population_size, generations, initial_coop_fraction, initial_resource,
#     regeneration_rate, carrying_capacity, cooperator_consumption,
#     defector_consumption_multiplier, and mutation_rate.
#
# In simulate_tragedy_commons:
#   - Initialize agents as a binary numpy array (1 for cooperator, 0 for defector)
#     based on initial_coop_fraction.
#   - Initialize the resource level.
#   - Create an empty list for results.
#
#   For each generation:
#     - Compute each agent’s planned consumption:
#         * Cooperators consume cooperator_consumption.
#         * Defectors consume cooperator_consumption multiplied by defector_consumption_multiplier.
#     - Calculate total consumption demand.
#     - Determine scaling factor if demand exceeds available resource.
#     - Compute actual consumption and agent payoffs.
#     - Update the resource level using a logistic regeneration function:
#           resource = resource + regeneration_rate * resource * (1 - resource/carrying_capacity) - total_consumption
#     - Perform reproduction:
#         * Sample new generation of agents with probabilities proportional to payoffs.
#         * Apply mutation with probability mutation_rate to flip the agent’s strategy.
#     - Record generation, resource level, fraction of cooperators, and average payoff.
#
#   Return results as a Pandas DataFrame.
#
# (Include any helper functions as needed.)
