import os
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

def main():
    data_file = "outputs/simulation_results.csv"
    if not os.path.exists(data_file):
        print("Simulation data not found. Run 01_simulation.py first.")
        return
    df = pd.read_csv(data_file)
    # Get final generation data for each replicate
    final_df = df[df["generation"] == df.groupby("replicate")["generation"].transform('max')]
    summary = final_df.agg({
        "resource": ["mean", "median", "std"],
        "fraction_cooperators": ["mean", "median", "std"],
        "avg_payoff": ["mean", "median", "std"]
    }).transpose().reset_index().rename(columns={'index':'metric'})
    
    # Correlation analysis between final resource and fraction_cooperators
    corr, p_value = pearsonr(final_df["resource"], final_df["fraction_cooperators"])
    corr_stats = pd.DataFrame([{"resource_vs_fraction_cooperators_corr": corr, "p_value": p_value}])
    
    os.makedirs("outputs", exist_ok=True)
    summary.to_csv("outputs/analysis_summary.csv", index=False)
    corr_stats.to_csv("outputs/analysis_correlation.csv", index=False)
    
    print("Summary Statistics:")
    print(summary)
    print("\nCorrelation (resource vs fraction_cooperators):")
    print(corr_stats)

if __name__ == '__main__':
    main()
