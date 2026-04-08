# Bank Note Authentication ML API - Deployment Guide

## 📋 Project Overview

This is a production-ready **Machine Learning API** that classifies bank notes as genuine or forged using a trained Logistic Regression model.

### Model Performance
- **Test Accuracy**: 98.55%
- **Training Accuracy**: 99.18%
- **Precision**: 0.99
- **Recall**: 0.98
- **F1-Score**: 0.99

---

## 📦 Project Contents

```
mlmodel/
├── main.py                          # FastAPI application
├── model.pkl                        # Trained ML model (1.2 KB)
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker containerization
├── docker-compose.yml               # Docker Compose setup
├── deployment-guide.md              # This file
├── train_model.py                   # Model training script
├── mlmodel1.ipynb                   # Jupyter notebook (analysis)
└── BankNote_Authentication.csv      # Training dataset
```

---

## 🚀 Deployment Options

### **Option 1: Docker (Recommended for Production)**

#### Build Docker Image
```bash
docker build -t banknote-api:latest .
```

#### Run Docker Container
```bash
docker run -p 8000:8000 banknote-api:latest
```

#### With Docker Compose
```bash
docker-compose up -d
```

API will be available at: `http://localhost:8000`

---

### **Option 2: Direct Installation (Local/VPS)**

#### Prerequisites
- Python 3.10+
- pip or conda

#### Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

### **Option 3: Azure App Service**

#### Prerequisites
- Azure CLI installed
- Azure subscription

#### Deployment Steps
```bash
# Login to Azure
az login

# Create resource group
az group create --name myResourceGroup --location eastus

# Create App Service Plan
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku B1 --is-linux

# Create Web App
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name banknote-api --runtime "PYTHON:3.11"

# Deploy from local git
az webapp up --name banknote-api --resource-group myResourceGroup --runtime "python:3.11"
```

---

### **Option 4: AWS Lambda + API Gateway**

#### Deployment with Zappa
```bash
# Install Zappa
pip install zappa

# Initialize Zappa
zappa init

# Deploy
zappa deploy production

# Update deployment
zappa update production
```

---

### **Option 5: Heroku**

#### Deployment Steps
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create banknote-api

# Add Procfile
echo "web: uvicorn main:app --host 0.0.0.0 --port $PORT" > Procfile

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

---

## 🔧 Configuration

### Environment Variables (Optional)
```bash
# .env file
API_TITLE=Bank Note Authentication API
API_VERSION=1.0
DEBUG=False
HOST=0.0.0.0
PORT=8000
```

### Production Settings
```python
# For production deployment, update main.py:
app = FastAPI(
    title="Bank Note Authentication API",
    version="1.0",
    description="ML API for bank note classification",
    docs_url="/docs",
    redoc_url="/redoc",
)
```

---

## 📡 API Endpoints

### **Root Endpoint**
```
GET /
```
Returns API status.

**Response:**
```json
{"message": "Bank Note Authentication API is running!"}
```

---

### **Prediction Endpoint**
```
POST /predict
```

**Request Body:**
```json
{
  "variance": 3.6216,
  "skewness": 8.6661,
  "curtosis": -2.8073,
  "entropy": -0.44699
}
```

**Response:**
```json
{
  "prediction": 0
}
```

**Prediction Values:**
- `0`: Genuine Bank Note ✅
- `1`: Forged Bank Note ⚠️

---

## 📖 API Documentation

### Swagger UI
```
http://your-domain/docs
```

### ReDoc (Alternative)
```
http://your-domain/redoc
```

---

## 🧪 Testing the API

### Using cURL
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "variance": 3.6216,
    "skewness": 8.6661,
    "curtosis": -2.8073,
    "entropy": -0.44699
  }'
```

### Using Python
```python
import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={
        "variance": 3.6216,
        "skewness": 8.6661,
        "curtosis": -2.8073,
        "entropy": -0.44699
    }
)
print(response.json())
# Output: {"prediction": 0}
```

### Using JavaScript/Fetch
```javascript
fetch('http://localhost:8000/predict', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    variance: 3.6216,
    skewness: 8.6661,
    curtosis: -2.8073,
    entropy: -0.44699
  })
})
.then(r => r.json())
.then(data => console.log(data))
// Output: {prediction: 0}
```

---

## 📊 Model Information

### Features
- **variance**: Variance of the image
- **skewness**: Skewness of the image
- **curtosis**: Curtosis of the image
- **entropy**: Entropy of the image

### Algorithm
- **Type**: Logistic Regression
- **Library**: scikit-learn
- **Training Samples**: 1,097
- **Test Samples**: 275

### Model File
- **Name**: model.pkl
- **Size**: 1.2 KB
- **Format**: Joblib pickle
- **Compatibility**: Python 3.7+

---

## 🔒 Security Recommendations

### For Production Deployment

1. **Enable HTTPS**
   ```bash
   # Use SSL certificates
   uvicorn main:app --ssl-keyfile key.pem --ssl-certfile cert.pem
   ```

2. **Add Authentication**
   ```python
   from fastapi import Depends, HTTPException
   from fastapi.security import HTTPBearer
   
   security = HTTPBearer()
   
   @app.post("/predict")
   def predict(note: BankNote, credentials = Depends(security)):
       # Verify credentials
       return prediction
   ```

3. **Rate Limiting**
   ```bash
   pip install slowapi
   ```

4. **CORS Configuration**
   ```python
   from fastapi.middleware.cors import CORSMiddleware
   
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["https://yourdomain.com"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

5. **Logging & Monitoring**
   ```python
   import logging
   
   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)
   ```

---

## 📈 Performance Optimization

### Caching Predictions
```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def cached_predict(variance, skewness, curtosis, entropy):
    # Returns cached result if same input seen before
    pass
```

### Load Balancing
```bash
# Use Gunicorn with multiple workers
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

---

## 🆘 Troubleshooting

### Issue: Model file not found
```
FileNotFoundError: [Errno 2] No such file or directory: 'model.pkl'
```
**Solution**: Ensure `model.pkl` is in the same directory as `main.py`

### Issue: Port already in use
```
OSError: [Errno 48] Address already in use
```
**Solution**: Use a different port:
```bash
uvicorn main:app --port 8001
```

### Issue: Module not found
```
ModuleNotFoundError: No module named 'fastapi'
```
**Solution**: Install requirements:
```bash
pip install -r requirements.txt
```

---

## 📞 Support & Maintenance

### Retraining the Model
```bash
python train_model.py
```
This will:
1. Load the dataset
2. Train a new model
3. Evaluate performance
4. Save updated `model.pkl`

### Monitoring
- Check server logs regularly
- Monitor prediction accuracy
- Track API response times
- Alert on failures

---

## 📝 Deployment Checklist

- [ ] Model file (model.pkl) is present
- [ ] requirements.txt is accurate
- [ ] Dockerfile builds successfully
- [ ] API starts without errors
- [ ] Health check endpoint responds
- [ ] Prediction endpoint works
- [ ] API documentation is accessible
- [ ] HTTPS/SSL configured
- [ ] Authentication enabled (if needed)
- [ ] Monitoring & logging configured
- [ ] Backup strategy in place
- [ ] Disaster recovery plan ready

---

## 📞 Contact & Support

**Technical Support**: deployment-team@company.com  
**Project Lead**: data-science@company.com  
**Repository**: https://github.com/company/banknote-api

---

**Version**: 1.0  
**Last Updated**: 2026-04-08  
**Status**: ✅ Production Ready
