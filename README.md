# Land Use and Land Cover Classification with CNNs

## Setup Instructions

  1. **Create a virtual environment with Python 3.10**:
      ```bash
        # Install Python 3.10 if needed
        brew install python@3.10
        
        # Create and activate virtual environment
        python3.10 -m venv venv
        source venv/bin/activate
      ```

  2. **Install dependencies**:
      ```bash
        pip install -r requirements.txt
      ```
  3. **Download the dataset**:
      * Download from https://zenodo.org/records/7711810
      * Extract the files to the data/ directory
      * Ensure you have both RGB and multispectral (MS) data