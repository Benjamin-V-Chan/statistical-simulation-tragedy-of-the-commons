# statistical-simulation-tragedy-of-the-commons

## Project Overview

This project models the **Tragedy of the Commons** through an **evolutionary game-theoretic simulation**, incorporating elements from population dynamics, agent-based modeling, and nonlinear differential equations. The simulation involves agents that act as either **cooperators** or **defectors**, each consuming a shared, regenerating resource. Evolutionary pressure drives agents to adapt strategies over time based on fitness (payoff), introducing emergent behaviors and dynamic equilibria.

### Mathematical Foundations

Let the system be defined as follows:

- Total population size: $N$
- Generation index: $t \in \{0, 1, \dots, T\}$
- Fraction of cooperators at generation $t$: $f_t$
- Resource pool at generation $t$: $R_t$
- Cooperator consumption: $c$
- Defector consumption: $c_d = k \cdot c$ where $k > 1$
- Regeneration rate of the resource: $r$
- Carrying capacity of the resource pool: $K$
- Mutation probability: $\mu$

#### Consumption and Payoff

Each agent $i$ has a consumption at generation $t$ defined by:

$$C_i(t) = \begin{cases}
  c & \text{if agent } i \text{ is a cooperator} \\
  k \cdot c & \text{if agent } i \text{ is a defector}
\end{cases}$$

Total planned consumption:

$$C_{\text{total}}(t) = N [c \cdot f_t + k \cdot c \cdot (1 - f_t)]$$

If $C_{\text{total}}(t) > R_t$, each agent's consumption is scaled by a factor:

$$\alpha_t = \frac{R_t}{C_{\text{total}}(t)}$$

Actual consumption becomes $\alpha_t C_i(t)$ and the payoff $P_i(t)$ is equal to actual consumption.

#### Resource Regeneration

The resource evolves following a **logistic growth model** with harvesting:

$$R_{t+1} = R_t + r R_t \left(1 - \frac{R_t}{K}\right) - C_{\text{actual}}(t)$$

Where:
- $r R_t (1 - R_t/K)$ is the natural logistic growth
- $C_{\text{actual}}(t)$ is total actual consumption of the population

#### Evolutionary Dynamics

A new generation is formed via stochastic reproduction proportional to agent payoff:

- Probability of selection for agent $i$: $p_i = \frac{P_i(t)}{\sum_j P_j(t)}$
- With probability $\mu$, an agent's strategy mutates (cooperator ↔ defector)

Over time, this results in evolutionary pressures shifting the population distribution of cooperators vs. defectors depending on environmental feedback.

---

## Folder Structure

```
project-root/
├── scripts/
│   ├── utils.py                   # Core simulation function
│   ├── 01_simulation.py          # Run simulation and save results
│   ├── 02_data_analysis.py       # Analyze final outcomes across replicates
│   ├── 03_visualization.py       # Visualize trends and outcome distributions
│   └── 04_sensitivity_analysis.py# Run parameter sweep and sensitivity analysis
├── outputs/
│   ├── simulation_results.csv    # Main simulation data output
│   ├── analysis_summary.csv      # Summary statistics
│   ├── analysis_correlation.csv  # Correlation results
│   ├── avg_resource_timeseries.png
│   ├── avg_cooperation_timeseries.png
│   └── sensitivity_ic_*.png      # Sensitivity plots
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## Usage

### 1. Setup the Project:

Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.

```bash
pip install -r requirements.txt
```

### 2. Run the Main Simulation:

```bash
python scripts/01_simulation.py
```
This will run multiple replicates of the simulation and save the results to `outputs/simulation_results.csv`.

### 3. Analyze the Simulation Results:

```bash
python scripts/02_data_analysis.py
```
This script generates summary statistics and correlation results for final population metrics.

### 4. Generate Visualizations:

```bash
python scripts/03_visualization.py
```
This will create time series plots and a scatterplot of resource vs. cooperation in the final generation.

### 5. Perform Sensitivity Analysis:

```bash
python scripts/04_sensitivity_analysis.py
```
This performs a grid search over initial cooperation, defector greed, and mutation rate, then saves both CSV data and plots for result interpretation.

---

## Requirements

Install all required libraries via:
```bash
pip install -r requirements.txt
```

**requirements.txt** should include:
```
numpy
pandas
matplotlib
scipy
```
