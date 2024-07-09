# Transportation Mode Selection Tool

This tool helps in selecting the most suitable mode of transportation based on cost, time, and emissions for a given distance and weight of cargo.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Transportation Mode Selection Tool is a web application that allows users to input the distance and weight of their shipment and receive recommendations on the best transportation mode to use. The recommendations are based on minimizing total cost, total time, and total emissions.

## Features

- Calculate total cost, time, and emissions for different transportation modes.
- Sort and display recommendations based on cost, time, and emissions.
- Simple web interface for easy input and output.

## Installation

To install and run the Transportation Mode Selection Tool locally, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/nkusharoraa/transportation_mode_selection_tool.git
    cd transportation_mode_selection_tool
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install flask flask_sqlalchemy pandas
    ```

4. Ensure the `transport_modes.csv` file is present in the root directory of the project. This file contains the initial data for different transportation modes.

## Usage

1. Initialize the database and start the application:

    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter the distance and weight of your shipment and click "Get Recommendation".

4. View the recommendations for the most suitable transportation mode.

## Data

The initial data for transportation modes is stored in a CSV file named `transport_modes.csv`. This file should have the following format:

```csv
mode,cost_per_mile,time_per_mile,emissions_per_mile
Road,0.5,0.1,0.02
Rail,0.3,0.08,0.01
Air,1.5,0.02,0.05
Sea,0.2,0.05,0.01
```

## Previews

![image](https://github.com/nkusharoraa/transportation_tool/assets/59050030/8081a772-d6a6-46b4-ab36-ce9f56f3cbdb)


![image](https://github.com/nkusharoraa/transportation_tool/assets/59050030/803bacca-b006-4fde-868e-9f0e1fb5e902)

![image](https://github.com/nkusharoraa/transportation_tool/assets/59050030/7b630b66-dbfd-448a-8576-2cb81680b722)
