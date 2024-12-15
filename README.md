# PII Redactor Service

This project implements a system to identify and redact Personally Identifiable Information (PII) from text. It includes a training pipeline for a spaCy NER model, a REST API using Flask for predictions, and a containerized deployment using Docker and Docker Compose.

---

## Table of Contents

1. [Features](#features)  
2. [Folder Structure](#folder-structure)  
3. [Prerequisites](#prerequisites)  
4. [Setup Instructions](#setup-instructions)  
5. [API Endpoints](#api-endpoints)  
6. [How It Works](#how-it-works)  
7. [Testing](#testing)  

---

## Features

1. **Training Pipeline**:  
   - Trains a Named Entity Recognition (NER) model using spaCy.  
   - Saves the trained model to be used for predictions.

2. **Flask REST API**:  
   - Provides an endpoint `/api/redact` to process text and redact PII entities.  
   - Redacts the following categories:  
     - `NAME`  
     - `EMAIL`  
     - `PHONE_NUMBER`  
     - `ORGANIZATION`  
     - `ADDRESS`  

3. **Dockerized Deployment**:  
   - Uses Docker Compose to orchestrate the **training** and **Flask API** services.  
   - Ensures the Flask API starts only after model training completes.  

---

## Folder Structure

```plaintext
new/
├── training/                   # Training pipeline
│   ├── __init__.py
│   ├── main.py                 # Entry point for training
│   ├── factory.py              # Model initialization
│   ├── data_utils.py           # Preprocess and handle training data
│   ├── corpus_creator.py       # Converts data into spaCy format
│   ├── constants.py            # Constants for paths and settings
│   ├── config.cfg              # spaCy configuration file
│   └── pii_data.json           # Training dataset
├── service/                    # Flask REST API
│   ├── __init__.py
│   ├── app.py                  # Flask application factory
│   ├── api.py                  # API routes
│   ├── factory.py              # Model loader for predictions
│   ├── validators.py           # Input validation logic
│   ├── config.py               # Configuration for Flask
│   └── logger.py               # Application logging
├── Dockerfile                  # Docker configuration for the image
├── docker-compose.yml          # Orchestration file for services
├── requirements.txt            # Python dependencies
├── .dockerignore               # Files to ignore in Docker build
├── .gitignore                  # Files to ignore in git
└── README.md                   # Project documentation
```
---
## Prerequisites

- **Python**: Version 3.12  
- **Docker**: Version 20.x or higher  
- **Docker Compose**: Version 3.x or higher  

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd new
   ```
2. **Build Docker Images:**:
   ```bash
   docker-compose build
    ```

3. **Start Services:**:
   ```bash
   docker-compose up
    ```
4. **Access the API:**:
   ```bash
   http://localhost:5000
    ```
---
## API Endpoints

### 1. Redact PII

**Endpoint**: `/api/redact`  
**Method**: `POST`  

**Request Body**:
```json
{
  "text": "John Doe lives at 123 Baker Street. You can contact him at john.doe@example.com or 555-123-4567."
}
```
**Response**:
```json
{
  
  "redacted_text": "[NAME] lives at [ADDRESS]. You can contact him at [EMAIL] or [PHONE_NUMBER]."

}
```
---

## How It Works

### Training:
- The `training/main.py` script trains a spaCy NER model using the `pii_data.json` dataset.
- The trained model is saved under the `model/` directory.
- A flag file (`training_complete.flag`) is created to indicate that training has completed successfully.

### Flask API:
- The Flask API loads the trained model using `service/factory.py`.
- The `/api/redact` endpoint processes the input text and replaces detected PII entities with their respective categories.

### Docker Compose:
- The **training service** runs the training pipeline and saves the model.
- The **flask-service** starts only after the model training completes successfully.
  - This ensures that the model is available before the Flask API starts serving requests.

---
## Testing

### Unit Tests
Run unit tests for the training pipeline and the Flask API using pytest:
```bash
   pytest training\tests
   pytest service\tests
```
  
---


 
