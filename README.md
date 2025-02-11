# Driver-Proximity-and-Lane-Changing-Prediction
## Overview

This project develops a machine learning model to predict lane-changing behavior based on the proximity of vehicles in adjacent lanes. It's based on research into understanding human driver behavior and its impact on traffic flow.

## Motivation

Understanding and predicting lane-changing behavior can contribute to:

*   Advanced Driver-Assistance Systems (ADAS)
*   Autonomous vehicle navigation
*   Traffic management and optimization

## Key Features

*   Machine learning model for lane-change prediction
*   Analysis of vehicle proximity data
*   Sample dataset for demonstration
*   Clear code structure and documentation

## Technologies Used

*   Python
*   pandas
*   scikit-learn

## Installation

1.  Clone the repository:

    ```
    git clone https://github.com/<your_username>/DriverProximityLaneChange.git
    cd DriverProximityLaneChange
    ```

2.  Create a virtual environment (recommended):

    ```
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1.  **Explore the data** using the `data_exploration.ipynb` notebook in the `/notebooks` folder.
2.  **Train the model** by running the `train_model.py` script:

    ```
    python scripts/train_model.py
    ```
   3.  **Predict lane change** by running the `predict_lane_change.py` script:
    ```
    python scripts/predict_lane_change.py --proximity <proximity_value> --speed <speed_value>
    ```

## Data Dictionary

*   **Distance_Main_Next_Lane:** The distance (in meters) from the main vehicle to the vehicle in the adjacent lane.
*   **Relative_Speed:** The speed difference (in km/h) between the main vehicle and the vehicle in the adjacent lane.
*   **Lane_Change:** A binary variable (0 or 1) indicating whether the driver initiated a lane change (1) or not (0).

## Data Source

This study's data was generated for research purposes and to show a demonstration.
