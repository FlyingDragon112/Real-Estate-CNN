# CDC Project

This project predicts prices using image features and geospatial data, leveraging a Convolutional Neural Network (CNN) and static map images.

## Project Structure

```
.
├── data_fetcher.py           # Downloads static map images for test and train data
├── model_training.ipynb      # Model training notebook
├── preprocessing.ipynb       # Data preprocessing notebook
└── README.md                 # Project documentation
```

## Setup

1. **Clone the repository** and set up a Python virtual environment (Python 3.8+ recommended).
2. **Install dependencies** (see your notebook cells for required packages, e.g., `pandas`, `requests`, `torch`, etc.).
3. **Download static map images**:
   - Ensure Docker is installed.
   - Start the static maps server:
     ```sh
     docker run -d -p 3000:3000 staticmaps
     ```
   - Run the image fetcher:
     ```sh
     python data_fetcher.py
     ```
   - This will populate the `images` and `test_images` directories.

## Notebooks

- **preprocessing.ipynb**: Data cleaning and preprocessing.
- **model_training.ipynb**: Model definition, training, and evaluation.

## Model

- The model uses satellite images and tabular data to predict prices.
- Trained weights are saved in `price_prediction_cnn.pth`.


## Static Maps Server

- The project uses docker-staticmaps to generate satellite images for each data point.
- See `docker-staticmaps/README.md` for more details.

## Usage

1. Fetch images using `data_fetcher.py`.
2. Run the notebooks in order: data exploration, preprocessing, then model training.
3. Use the trained model for predictions.

## License

See `docker-staticmaps/LICENSE` for third-party component licensing.

---