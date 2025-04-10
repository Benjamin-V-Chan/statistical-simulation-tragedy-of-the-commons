# =====================================
#
# Import pandas, numpy, and scipy.stats.
# Define the main function:
#   - Load the simulation CSV file from outputs/simulation_results.csv.
#   - For each replicate, extract the final generation’s metrics.
#   - Compute summary statistics across replicates:
#         * Mean, median, and standard deviation for final resource, fraction_cooperators, and avg_payoff.
#   - Optionally perform Pearson correlation between final resource and fraction_cooperators.
#   - Save the summary statistics and correlations to outputs/analysis_summary.csv.
#   - Print the summary results.
# Run the main function.
