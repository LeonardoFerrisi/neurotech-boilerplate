# EEG Data Collection with BrainFlow

This project provides boilerplate code for collecting EEG data using the BrainFlow Python package. It supports any device compatible with BrainFlow, and allows data collection and saving the results as a CSV file.

## Requirements

- Python 3.7+
- BrainFlow Library (https://brainflow.org/)
- Supported EEG Device (https://brainflow.readthedocs.io/en/stable/SupportedBoards.html)S

## Installation

1. Clone this repository or download the `collect_data.py` file.
2. Install the required dependencies:
   ```bash
   pip install brainflow
   ```

## Usage 

1. Set the correct serial port and board ID for your EEG device in `collect_data.py`:

```python
params.serial_port = ''  # Replace with your device's serial port
board_id = 0  # Replace with your device's board ID (check BrainFlow docs)
```

2. Run the script to start collecting EEG data:

```bash
python collect_data.py
```

3. The collected data will be saved in `eeg_data.csv` by default. You can change the file name or format in the script.

