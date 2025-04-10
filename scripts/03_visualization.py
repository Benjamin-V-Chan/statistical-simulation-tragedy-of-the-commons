import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    data_file = "outputs/simulation_results.csv"
    if not os.path.exists(data_file):
        print("Simulation data not found. Run 01_simulation.py first.")
        return
    df = pd.read_csv(data_file)
    
    os.makedirs("outputs", exist_ok=True)
    
    # Time series: average resource and fraction_cooperators over generations
    ts = df.groupby("generation").agg({
        "resource": "mean",
        "fraction_cooperators": "mean"
    }).reset_index()
    
    plt.figure()
    plt.plot(ts["generation"], ts["resource"])
    plt.xlabel("Generation")
    plt.ylabel("Average Resource")
    plt.title("Time Series: Average Resource over Generations")
    plt.savefig("outputs/avg_resource_timeseries.png")
    plt.close()
    
    plt.figure()
    plt.plot(ts["generation"], ts["fraction_cooperators"])
    plt.xlabel("Generation")
    plt.ylabel("Average Fraction of Cooperators")
    plt.title("Time Series: Average Cooperation over Generations")
    plt.savefig("outputs/avg_cooperation_timeseries.png")
    plt.close()
    
    # Scatter plot for final generation: resource vs. fraction_cooperators for each replicate
    final_df = df[df["generation"] == df.groupby("replicate")["generation"].transform('max')]
    plt.figure()
    plt.scatter(final_df["fraction_cooperators"], final_df["resource"])
    plt.xlabel("Fraction of Cooperators")
    plt.ylabel("Final Resource")
    plt.title("Final Generation: Resource vs. Fraction of Cooperators")
    plt.savefig("outputs/final_scatter.png")
    plt.close()

if __name__ == '__main__':
    main()
