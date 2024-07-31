# Sentiment_Analysis


## Project Overview

This project demonstrates an end-to-end solution for sentiment analysis of Amazon reviews. It involves building a classifier to predict review sentiment as positive, neutral, or negative. The solution includes extensive textual analysis, model development, API creation, and a web application for user interaction.

## Key Components

### 1. Textual Analysis

- **Data Exploration and Preprocessing:** 
  - Analyzed Amazon reviews dataset to understand rating and feedback distribution.
  - Performed preprocessing tasks including tokenization, stemming, and stop word removal.

- **Feature Extraction:**
  - Applied Count Vectorization to convert text data into numerical features.

### 2. Model Development

- **Classifier Models:**
  - Implemented and evaluated multiple classification algorithms including Random Forest, XGBoost, and Decision Tree.

- **Model Tuning:**
  - Optimized models through hyperparameter tuning and cross-validation.

- **Model Evaluation:**
  - Assessed model performance using accuracy scores and confusion matrices.

### 3. API Development

- **Flask API:**
  - Developed a Flask-based API to provide sentiment analysis services.
  - Created endpoints for bulk predictions from CSV files and single text predictions.

### 4. Web Application

- **Streamlit Interface:**
  - Built a Streamlit application for users to input text or upload CSV files for sentiment analysis.
  - Integrated with the Flask API to fetch and display predictions.

## Getting Started

### Prerequisites

- Python 3.6+
- Required Python libraries: `Flask`, `flask-cors`, `pandas`, `nltk`, `scikit-learn`, `xgboost`, `streamlit`

### Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Install Dependencies:**
Create a requirements.txt file with the following content:
```bash
Flask
flask-cors
pandas
nltk
scikit-learn
xgboost
streamlit
```
Then, install the dependencies using:
```bash
pip install -r requirements.txt
```
### Running the Application
**Run the Flask API:**
Start the Flask API server by running:

```bash

flask --app api.py run --port=5000
```
**Run the Streamlit Application:**
Start the Streamlit web application by running:

```bash
streamlit run main.py
```
