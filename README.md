# Robot Soccer SSL Tactical Prediction

This project models the temporal movement of a swarm (a team of robots) in the Robot Soccer Small Size League (SSL) to predict their tactical behavior. We use Deep Learning (PyTorch) to process time-series telemetry data (x, y, orientation).

## Tech Stack
- Python 3.10+
- PyTorch
- Pandas & NumPy
- Protobuf
- scikit-learn

## Directory Structure
- `data/`: Contains raw and processed dataset files.
- `src/`: Core pipeline code.
  - `data/`: Scripts to parse Robot Soccer SSL Protobuf log files.
  - `features/`: Scripts to create sliding windows and PyTorch Datasets.
  - `models/`: PyTorch model definitions (e.g., LSTM).
  - `training/`: Training loops.

## Setup and Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Pipeline

1. **Parse Data**: Extract telemetry from `.log` files.
   ```bash
   python src/data/make_dataset.py
   ```

2. **Train Model**: Run the training pipeline.
   ```bash
   python src/training/train.py
   ```
