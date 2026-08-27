# Intelligent Taxi Trip Duration Prediction

## Project Overview

This project develops a machine learning system to predict the duration of a taxi trip using trip-related, geographic, and temporal information.

Accurate trip-duration prediction can support better passenger experience, estimated arrival times, fleet planning, and urban mobility analysis.

## Problem Statement

Predict the duration of a taxi trip based on factors such as pickup and drop-off locations, trip time, date, and other available trip attributes.

This is a supervised machine learning regression problem because the target variable, trip duration, is a continuous numerical value.

## Dataset

The project uses the NYC Taxi Trip Duration dataset.

Dataset source:
Kaggle — NYC Taxi Trip Duration

The dataset will be added to the `data/raw/` directory after the dataset source and usage requirements are verified.

## Project Structure

```text
intelligent-taxi-trip-duration/
├── data/
│   └── raw/
├── notebooks/
│   └── 01_eda.ipynb
├── src/
│   ├── __init__.py
│   ├── logger.py
│   ├── exception.py
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   └── pipeline/
│       ├── train_pipeline.py
│       └── predict_pipeline.py
├── artifacts/
├── logs/
├── requirements.txt
├── README.md
└── .gitignore