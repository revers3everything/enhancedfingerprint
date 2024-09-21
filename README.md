# Enhanced Fingerprint

**Enhanced Fingerprint** is a Python-based tool for fingerprint image enhancement, based on the Fingerprint-Enhancement-Python repository by [Utkarsh-Deshmukh](https://github.com/Utkarsh-Deshmukh/Fingerprint-Enhancement-Python). This version adds the functionality to save the final enhanced fingerprint image to a file.

## Features
- **Fingerprint Enhancement**: Uses Gabor filter techniques to enhance low-quality fingerprint images.
- **Save Enhanced Image**: After processing, the enhanced fingerprint image can now be saved to a file for further analysis or record-keeping.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/enhancedfingerprint.git
   ```

2. Navigate to the project directory:
   ```bash
   cd enhancedfingerprint
   ```

3. Install the required dependencies:
   ```bash
   pip install fingerprint_enhancer
   ```

## Usage

To run the program:

1. Place your fingerprint image in the same directory as the script or provide the path in the script.
2. Execute the Python script:
   ```bash
   python3 fingerprint.py
   ```

### Sample Output

The program will display the original and enhanced fingerprint images, and it will also save the enhanced image to the file path specified by the `--output` option.

## Requirements

- Python 3.x
- `fingerprint_enhancer` library (installed with `pip`)

## Acknowledgments

- The original codebase was developed by [Utkarsh Deshmukh](https://github.com/Utkarsh-Deshmukh) and can be found [here](https://github.com/Utkarsh-Deshmukh/Fingerprint-Enhancement-Python).
- This fork adds the functionality to save enhanced images.