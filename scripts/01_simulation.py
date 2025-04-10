# =====================================
#
# Import packages and the simulate_tragedy_commons function from utils.
# Define the main function:
#   - Set simulation parameters (population_size, generations, etc.).
#   - Specify the number of replicates to run.
#   - Create the outputs folder if it does not exist.
#   - For each replicate:
#         * Run the simulation.
#         * Add a 'replicate' column to the DataFrame.
#         * Append the DataFrame to a list.
#   - Concatenate all replicate DataFrames.
#   - Save the combined results as a CSV file in outputs/simulation_results.csv.
# Run the main function.
