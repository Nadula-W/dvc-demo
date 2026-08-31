# DVC House Price Demo

A tiny project for demonstrating the difference between Git and DVC.

## Setup

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

## Initialize Git + DVC

```bash
git init
dvc init
git add .dvc .dvcignore .gitignore
git commit -m "Initialize Git and DVC"
```

## Track the dataset

```bash
dvc add data/houses.csv
git status
git add data/houses.csv.dvc data/.gitignore
git commit -m "Track house dataset with DVC"
```

## Train

```bash
python src/train.py
```

## Demonstrate a new dataset version

Append a new row to `data/houses.csv`, then run:

```bash
dvc add data/houses.csv
git diff data/houses.csv.dvc
git add data/houses.csv.dvc
git commit -m "Update dataset version"
```
# dvc-demo
