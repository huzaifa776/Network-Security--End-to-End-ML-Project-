# Network Security - Phishing Detection ML Project

An end-to-end machine learning project for detecting phishing attacks using network security data. This project implements a complete MLOps pipeline from data ingestion to model deployment with FastAPI and Docker support.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Architecture](#project-architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Docker Deployment](#docker-deployment)
- [MLOps Pipeline](#mlops-pipeline)
- [Contributing](#contributing)

## 🎯 Overview

This project is an end-to-end machine learning solution designed to detect phishing attacks using network security data. It includes data ingestion from MongoDB, data validation, transformation, model training, and deployment through a FastAPI web service.

The system processes phishing data, trains a machine learning model, and provides REST API endpoints for training and prediction. It's built with production-ready features including logging, exception handling, artifact versioning, and cloud storage integration.

## ✨ Features

- **Complete ML Pipeline**: Data ingestion, validation, transformation, and model training
- **MongoDB Integration**: Seamless data storage and retrieval
- **REST API**: FastAPI-based web service for training and predictions
- **Batch Prediction**: Support for bulk predictions via CSV upload
- **Model Versioning**: Automatic artifact management and versioning
- **Cloud Storage**: S3 bucket integration for model storage
- **MLflow Integration**: Experiment tracking and model registry
- **Docker Support**: Containerized deployment
- **Comprehensive Logging**: Detailed logging for debugging and monitoring
- **Custom Exception Handling**: Robust error management system
- **Data Drift Detection**: Automatic data validation and drift reporting

## 🏗️ Project Architecture

```
Network Security ML Pipeline
├── Data Ingestion (MongoDB)
├── Data Validation (Schema & Drift Detection)
├── Data Transformation (Preprocessing)
├── Model Training (ML Model)
├── Model Evaluation
└── Deployment (FastAPI + Docker)
```

## 🛠️ Tech Stack

- **Programming Language**: Python 3.12
- **Web Framework**: FastAPI
- **Database**: MongoDB
- **ML Libraries**: scikit-learn, pandas, numpy
- **Experiment Tracking**: MLflow, DagHub
- **Serialization**: Dill
- **Cloud Storage**: AWS S3
- **Containerization**: Docker
- **Environment Management**: python-dotenv

## 📦 Installation

### Prerequisites
- Python 3.12 or higher
- MongoDB Atlas account or local MongoDB instance
- AWS account (for S3 storage, optional)
- Docker (for containerized deployment, optional)

### Local Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd "Network Security (End to End ML Project)"
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install the package in editable mode**
```bash
pip install -e .
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-url>/<database>?retryWrites=true&w=majority
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=your_aws_region
MLFLOW_TRACKING_URI=your_mlflow_uri
DAGSHUB_TOKEN=your_dagshub_token
```

### Data Schema

The data schema is defined in `data_schema/schema.yaml`. Ensure your data conforms to this schema for proper validation.

## 🚀 Usage

### 1. Push Data to MongoDB

Upload your phishing data to MongoDB:

```bash
python push_data.py
```

This script reads data from `network_data/phishingData.csv` and pushes it to MongoDB.

### 2. Train the Model

#### Option A: Using main.py (Complete Pipeline)
```bash
python main.py
```

#### Option B: Using the API
```bash
python app.py
```
Then access: `http://localhost:8000/train`

### 3. Make Predictions

Start the FastAPI server:
```bash
python app.py
```

Access the API documentation at: `http://localhost:8000/docs`

Upload a CSV file for batch predictions at the `/predict` endpoint.

### 4. Test MongoDB Connection

```bash
python test_mongodb.py
```

## 📁 Project Structure

```
Network Security (End to End ML Project)/
│
├── app.py                          # FastAPI application
├── main.py                         # Training pipeline execution
├── push_data.py                    # Data upload to MongoDB
├── test_mongodb.py                 # MongoDB connection test
├── requirements.txt                # Project dependencies
├── setup.py                        # Package setup file
├── Dockerfile                      # Docker configuration
├── readme.md                       # Project documentation
│
├── networksecurity/                # Main package
│   ├── __init__.py
│   ├── components/                 # Pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── entity/                     # Data classes
│   │   ├── config_entity.py        # Configuration entities
│   │   └── artifact_entity.py      # Artifact entities
│   │
│   ├── pipeline/                   # ML pipelines
│   │   ├── training_pipeline.py
│   │   └── batch_prediction.py
│   │
│   ├── exception/                  # Custom exceptions
│   │   └── exception.py
│   │
│   ├── logging/                    # Logging configuration
│   │   └── logger.py
│   │
│   ├── utils/                      # Utility functions
│   │   ├── main_utils/
│   │   │   └── utils.py
│   │   └── ml_utils/
│   │       ├── metric/
│   │       │   └── classification_metric.py
│   │       └── model/
│   │           └── estimator.py
│   │
│   ├── cloud/                      # Cloud storage utilities
│   │   └── s3_syncer.py
│   │
│   └── constant/                   # Constants
│       └── training_pipeline/
│           └── __init__.py
│
├── Artifacts/                      # Training artifacts
├── final_model/                    # Trained models
├── logs/                           # Application logs
├── network_data/                   # Raw data
│   └── phishingData.csv
├── data_schema/                    # Data schema definitions
│   └── schema.yaml
├── prediction_output/              # Prediction results
│   └── output.csv
├── templates/                      # HTML templates
│   └── table.html
└── notebooks/                      # Jupyter notebooks for exploration
```

## 🔌 API Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: GET
- **Description**: Redirects to API documentation

### 2. Train Model
- **URL**: `/train`
- **Method**: GET
- **Description**: Triggers the complete training pipeline
- **Response**: Training success message

### 3. Batch Prediction
- **URL**: `/predict`
- **Method**: POST
- **Description**: Upload a CSV file for batch predictions
- **Request**: Multipart form data with CSV file
- **Response**: HTML table with predictions

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t network-security-app .
```

### Run Docker Container

```bash
docker run -p 8000:8000 --env-file .env network-security-app
```

Access the application at `http://localhost:8000`

## 🔄 MLOps Pipeline

### 1. Data Ingestion
- Connects to MongoDB
- Fetches data from the specified collection
- Splits data into training and testing sets
- Stores data in the feature store

### 2. Data Validation
- Validates data against the schema
- Checks for missing values and data types
- Generates data drift reports
- Separates valid and invalid data

### 3. Data Transformation
- Handles missing values
- Encodes categorical features
- Scales numerical features
- Creates preprocessing pipelines

### 4. Model Training
- Trains multiple ML models
- Performs hyperparameter tuning
- Evaluates model performance
- Saves the best model

### 5. Model Deployment
- Loads trained models
- Serves predictions via REST API
- Supports batch predictions

## 📊 Model Artifacts

All training artifacts are stored in the `Artifacts/` directory with timestamp-based versioning:
- Feature store data
- Validated/Invalid data
- Transformed data
- Trained models
- Data drift reports
- Preprocessing pipelines

Final production models are stored in `final_model/`:
- `model.pkl`: Trained ML model
- `preprocessor.pkl`: Data preprocessing pipeline

## 🔍 Logging and Monitoring

- Comprehensive logging throughout the pipeline
- Logs stored in the `logs/` directory
- Custom exception handling with detailed error messages
- MLflow integration for experiment tracking

## 📝 Data Format

### Input Data
The input CSV should contain network security features with a `Result` column indicating phishing (1) or legitimate (0/-1).

### Output Format
Predictions are saved in `prediction_output/output.csv` with an additional `predicted_column` showing the model's predictions.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Huzaifa Mahmood**

## 🙏 Acknowledgments

- MongoDB for database services
- FastAPI for the web framework
- MLflow and DagHub for experiment tracking
- scikit-learn for machine learning tools

---

**Note**: Make sure to configure all environment variables and MongoDB connection before running the application. For production deployment, ensure proper security measures are in place for API endpoints and database connections.