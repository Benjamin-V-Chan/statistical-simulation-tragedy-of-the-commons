# Tragedy of the Commons: Evolutionary Statistical Simulation

### Mathematical Foundations

Let the system have:
- Total population size: `$N`  
- Generation index: `$t \in \{0, 1, \dots, T\}`  
- Fraction of cooperators at time `$t$`: `$f_t`  
- Resource pool at time `$t$`: `$R_t`  
- Cooperator consumption: `$c`  
- Defector consumption: `$c_d = k \cdot c$`, where `$k > 1`  
- Regeneration rate: `$r`  
- Carrying capacity: `$K`  

Each agent `$i$` consumes:

```
C_i(t) = {
  c         if i is a cooperator
  k * c     if i is a defector
}
```

The total planned consumption at generation `$t$` is:

`C_total(t) = c * f_t * N + k * c * (1 - f_t) * N`

If `C_total(t) > R_t`, consumption is scaled:

`scale_t = R_t / C_total(t)`, where `scale_t ∈ (0,1)`

Then the **actual payoff** `$P_i(t)$` per agent is:

`P_i(t) = C_i(t) * scale_t`

Reproduction is probabilistic and proportional to `$P_i(t)$`.

The **resource regeneration** follows logistic dynamics:

`R_{t+1} = R_t + r * R_t * (1 - R_t / K) - C_actual(t)`

After reproduction, agents can mutate with probability `$\mu$`, flipping from cooperator to defector or vice versa.

This leads to a stochastic system where:
- Cooperators may die out due to exploitation.
- Resource depletion triggers selection pressure.
- Mutation introduces dynamic equilibrium around cooperation-defection balances.

We analyze the equilibria and stability of `$f_t$` and `$R_t$` over time. In particular, we are interested in fixed points `$f^*, R^*$` such that:

`f_{t+1} = f_t` ⇒ `$f^*$` is an evolutionary stable strategy (ESS).

We observe that depending on `$k$`, `$\mu$`, and `$r$`, the system can:
- Collapse to `$f^* = 0$` (all defectors)
- Stabilize at `$f^* \in (0,1)$`
- Sustain cycles or chaotic fluctuations

## Folder Structure

```
project-root/
├── scripts/
│   ├── utils.py                     # Core simulation logic
│   ├── 01_simulation.py            # Run simulation replicates
│   ├── 02_data_analysis.py         # Analyze results and compute stats
│   ├── 03_visualization.py         # Plot time series and correlations
│   └── 04_sensitivity_analysis.py  # Run multi-param sensitivity tests
├── outputs/                        # Contains all generated CSVs and plots
└── requirements.txt                # Required Python libraries
```

## Usage

### 1. Setup the Project:

Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.

```bash
pip install -r requirements.txt
```

### 2. Run Simulation (default parameters, multiple replicates):

```bash
python scripts/01_simulation.py
```

### 3. Analyze Simulation Results:

```bash
python scripts/02_data_analysis.py
```

### 4. Generate Visualizations:

```bash
python scripts/03_visualization.py
```

### 5. Perform Sensitivity Analysis:

```bash
python scripts/04_sensitivity_analysis.py
```

## Requirements

The project requires the following Python packages:

```
numpy
pandas
matplotlib
scipy
```

These are listed in `requirements.txt`. Install them using pip:

```bash
pip install -r requirements.txt
```
