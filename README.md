# Intelligent Taxi Trip Duration Prediction

## Project Overview

This project develops a machine learning system to predict the duration of a taxi trip using trip-related, geographic, and temporal information.

Accurate trip-duration prediction can support better passenger experience, estimated arrival times, fleet planning, and urban mobility analysis.

## Problem Statement

Predict the duration of a taxi trip based on factors such as pickup and drop-off locations, trip time, date, and other available trip attributes.

This is a supervised machine learning regression problem because the target variable, trip duration, is a continuous numerical value.

## Dataset

The project uses the NYC Taxi Trip Duration dataset.

**Dataset source:** Kaggle — NYC Taxi Trip Duration

The dataset will be added to the `data/raw/` directory after the dataset source and usage requirements are verified.

## Technologies

- Python 3.11
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook
- Flask
- Git
- GitHub
- Conda

## Environment Setup

### 1. Create the Conda environment

```bash
conda env create -f environment.yml
```

### 2. Activate the environment

```bash
conda activate taxi-ml
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify the Python environment

```bash
python --version
```

The project currently uses Python 3.11.

## Project Structure

```text
intelligent-taxi-trip-duration/
│
├── data/
│   └── raw/
│
├── notebooks/
│
├── src/
│   ├── __init__.py
│   ├── logger.py
│   ├── exception.py
│   │
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   └── pipeline/
│       ├── train_pipeline.py
│       └── predict_pipeline.py
│
├── artifacts/
├── logs/
│
├── requirements.txt
├── environment.yml
├── README.md
└── .gitignore
```

## Development Workflow

The project follows a structured machine learning development workflow:

```text
Environment Setup
        ↓
Data Collection
        ↓
Data Validation
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Data Transformation
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Hyperparameter Tuning
        ↓
Prediction Pipeline
        ↓
Deployment
```

## Project Progress

### Unit 1 — Environment & Project Setup

- [x] Python 3.11 environment created
- [x] Project structure created
- [x] Required libraries installed
- [x] Requirements file created
- [x] Conda environment specification created
- [x] Git repository initialized
- [x] GitHub repository connected
- [x] Initial project pushed to GitHub

### Unit 2 — Logging, Exception Handling & Git

- [ ] Logging
- [ ] Custom exception handling
- [ ] Data ingestion
- [ ] Feature branch and Pull Request

### Machine Learning

- [ ] Data analysis
- [ ] Feature engineering
- [ ] Data transformation
- [ ] Model training
- [ ] Model evaluation
- [ ] Hyperparameter tuning
- [ ] Model explainability

### Deployment

- [ ] Prediction pipeline
- [ ] API
- [ ] Deployment

## Current Status

Unit 1 — Environment and project setup completed.

Unit 2 — Logging, exception handling, data ingestion, and Git workflow are currently in progress.

## Development Workflow

The project follows a structured machine learning development workflow:

```text
Environment Setup
        ↓
Data Collection
        ↓
Data Validation
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Data Transformation
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Hyperparameter Tuning
        ↓
Prediction Pipeline
        ↓
Deployment