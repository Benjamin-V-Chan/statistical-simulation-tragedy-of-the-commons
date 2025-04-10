# =====================================
#
# Import necessary packages (numpy, pandas, itertools) and simulate_tragedy_commons from utils.
# Define the main function:
#   - Establish parameter grids for:
#         * initial_coop_fraction (e.g., 0.2, 0.5, 0.8)
#         * defector_consumption_multiplier (e.g., 1.5, 2.0, 3.0)
#         * mutation_rate (e.g., 0.0, 0.01, 0.05)
#   - Set fixed simulation parameters (population_size, generations, etc.).
#   - For every combination of parameter values, run several replicate simulations:
#         * For each replicate, record the final generation metrics (resource, fraction_cooperators, avg_payoff).
#         * Compute average final metrics for that parameter combination.
#         * Append these results along with the parameter values.
#   - Assemble all results into a Pandas DataFrame.
#   - Save the sensitivity analysis results to outputs/sensitivity_analysis.csv.
#   - Generate a plot (e.g., scatter plot) to show how final resource depends on defector multiplier
#     for different mutation rates and initial cooperation levels. Save each plot to PNG.
# Run the main function.
