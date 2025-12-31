# Quantum Machine Learning Tutorial

## Quick start

1) Create the conda env (Python 3.8):

```bash
conda env create -f environment.yml
conda activate qml
```

1) Install wheels (skips building qiskit-aer from source):

```bash
pip install --upgrade pip
pip install --only-binary=:all: "qiskit-aer==0.15.1"
pip install -r requirements.txt --no-build-isolation --only-binary=qiskit-aer
```

1) Build the docs:

```bash
make html
```

1) Explore the notebooks:

```bash
jupyter lab
```

## Troubleshooting

- If `myst_nb` is missing, re-check that `conda activate qml` was run before `make html`.
- If `qiskit-aer` tries to compile, ensure the `--only-binary` install step above ran without errors.
