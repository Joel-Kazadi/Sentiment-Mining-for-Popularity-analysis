# Thesis Pipeline README

## Overview

This repository contains a comprehensive pipeline for predicting DRC 2018 election results based on Twitter data. The pipeline includes web scraping, data preprocessing, exploratory data analysis (EDA), sentiment analysis, popularity index construction, time series predictions, and accuracy comparisons. Each step is encapsulated in separate Python notebooks or scripts for clarity and modularity.

## Pipeline Structure

The pipeline consists of the following components, each connected sequentially:

1. **Web Scraping**
   - **Filename**: `WebScraping.py`
   - **Description**: This script scrapes Twitter data based on specified parameters in the thesis. It outputs the raw data as an XLSX file named `scraped_data.xlsx`.

2. **Data Preprocessing**
   - **Filename**: `1 DataPreprocessing.ipynb`
   - **Description**: This notebook loads the raw data from `scraped_data.xlsx`, performs various NLP operations for data cleaning and preprocessing, and outputs the results to `preprocessed_data.csv`.

3. **Exploratory Data Analysis (EDA)**
   - **Filename**: `2 EDA.ipynb`
   - **Description**: This notebook retrieves the preprocessed data from `preprocessed_data.csv` to conduct data exploration, including statistical tables and graphical visualizations. Note that no output CSV file is generated from this step.

4. **Sentiment Analysis**
   - **Filename**: `3 SentimentAnalysis.ipynb`
   - **Description**: This notebook uses the preprocessed data from `preprocessed_data.csv` to perform sentiment analysis using French-VADER and CamemBERT techniques. The resulting data is saved in `sentiment_data.csv`.

5. **Indices Construction**
   - **Filename**: `4 IndicesConstruction.ipynb`
   - **Description**: This notebook processes the sentiment analysis data from `sentiment_data.csv` to construct defined popularity indices (TSSW, WG, YHRM) in both baseline and penalized versions, along with visualizations of the indices over the campaign period. The output is saved as `popularity_data.csv`.

6. **Time Series Prediction**
   - **Filename**: `5 TimeSeriesPrediction.ipynb`
   - **Description**: This notebook utilizes the popularity data from `popularity_data.csv` to make predictions using ARIMA and LSTM methods. It conducts backtesting (expanding window + rolling window) to evaluate the forecasting performance. The predictions are saved in `predictions_data.csv`.

7. **Accuracy Comparison**
   - **Filename**: `6 AccuracyComparison.ipynb`
   - **Description**: This final notebook retrieves the predictions from `predictions_data.csv` to calculate and compare the accuracy of each popularity index, focusing on the penalized versions to determine the relevance of subjectivity for predicting election outcomes. The results are saved in `accuracy_data.csv`.

## Requirements

To replicate the entire pipeline, please ensure you have the necessary Python packages installed. You can install them using the provided `requirements.txt` file. 

### Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository

2. Install the required packages:
   ```bash
   pip install -r requirements.txt

### Usage Instructions

- Execute `WebScraping.py` to start the pipeline.
- Proceed to run each notebook in the order listed above (1 to 6) in a Jupyter Notebook environment.
- Ensure that each output file is available for the subsequent steps.
- Recommended environment: Python 3.11.13.

### Note

Ensure you have appropriate permissions and comply with Twitter’s terms of service when scraping data. This pipeline is designed for research purposes and should be used responsibly.

### Contributions

Feel free to fork the repository, make improvements, and suggest changes via pull requests!
