# Quantum Feature Surrogates

## Environment Setup

### Requirements

- Python 3.14.x (recommended)
- Git

### 1. Clone the repository

```powershell
git clone https://github.com/USERNAME/quantum-feature-surrogates.git
cd quantum-feature-surrogates
```

### 2. Create a virtual environment

```powershell
py -3.14 -m venv .venv
```

You can replace `3.14` with another Python version if you prefer, provided it is compatible with the project dependencies.

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Verify Python version

```powershell
python --version
```

### 5. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Run the experiment

```powershell
python -m src.experiments.run_iris_baseline
```

### Deactivate the environment

```powershell
deactivate
```