# statistical-simulation-tragedy-of-the-commons

## Project Overview

This project simulates the evolutionary dynamics of cooperative and defecting agents in a shared-resource environment, illustrating the phenomenon known as the **Tragedy of the Commons**. The simulation is agent-based and runs over multiple generations. Each agent consumes resources depending on whether they are a **cooperator** or **defector**, and reproduction is determined by a payoff function based on resource consumption.

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

```text
numpy
pandas
matplotlib
scipy
```

These are listed in `requirements.txt`. Install them using pip:

```bash
pip install -r requirements.txt
```