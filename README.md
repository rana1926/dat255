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
        ```bash
        mkdir -p data
        # Extract EuroSAT_RGB and EuroSAT_MS folders to data/
        ```
      * Ensure you have both RGB and multispectral (MS) data
  4. **Run the Jupyter notebook**:
      ```bash
      jupyter notebook imgClassification.ipynb
      ```
## Training the Model
  1. **Run through the jupyter notebook to train the model**
  2. **Make sure the model is saved as SatCoverClassifier.keras in the correct folder:**:
      ```bash
      # The model should be in models/SatCoverClassifier.keras
      mkdir -p models
      ```
##  Running the Flask App with Docker
build and run the docker container
```bash
  docker-compose up --build
  # access the app on http://localhost:7860
  # or Update your docker-compose.yml to use a different port
```
to stop
```bash
  # Press Ctrl+C in the terminal or run:
  docker-compose down
```