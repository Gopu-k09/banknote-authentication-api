# 🚀 Quick Start Guide - Deployment Team

## What You're Getting

A **production-ready Machine Learning API** that classifies bank notes as genuine or forged.

```
Model Accuracy: 98.55% ✅
Size: 1.2 KB (lightweight)
API: FastAPI (modern, fast, documented)
```

---

## ⚡ Quick Deployment (5 minutes)

### **The Fastest Way: Docker**

```bash
# 1. Navigate to project folder
cd mlmodel

# 2. Build Docker image
docker build -t banknote-api .

# 3. Run container
docker run -p 8000:8000 banknote-api

# 4. Test the API
curl http://localhost:8000/

# 5. Visit API docs
Open: http://localhost:8000/docs
```

**Done!** API is running. 🎉

---

## 📦 Files in This Package

| File | Purpose |
|------|---------|
| `main.py` | FastAPI application |
| `model.pkl` | Trained ML model |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Docker setup |
| `docker-compose.yml` | Docker Compose config |
| `DEPLOYMENT_GUIDE.md` | Full deployment guide |
| `train_model.py` | Model training script |

---

## 🔌 API Endpoints

### Check Status
```bash
GET /
# Response: {"message": "Bank Note Authentication API is running!"}
```

### Make Prediction
```bash
POST /predict
# Body: {
#   "variance": 3.6216,
#   "skewness": 8.6661,
#   "curtosis": -2.8073,
#   "entropy": -0.44699
# }
# Response: {"prediction": 0}
# 0 = Genuine, 1 = Forged
```

### API Documentation
```
http://localhost:8000/docs  (Swagger UI)
http://localhost:8000/redoc (ReDoc)
```

---

## 🛠️ Installation Options

### **Option A: Docker (Recommended)**
```bash
docker build -t banknote-api .
docker run -p 8000:8000 banknote-api
```

### **Option B: Python Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate (Windows)
pip install -r requirements.txt
uvicorn main:app --reload
```

### **Option C: Docker Compose**
```bash
docker-compose up -d
```

### **Option D: Kubernetes**
```bash
kubectl create deployment banknote-api --image=banknote-api:latest
kubectl expose deployment banknote-api --type=LoadBalancer --port=8000
```

---

## 🧪 Test the API

### Using Swagger UI (Easiest)
1. Open browser: `http://localhost:8000/docs`
2. Click on `/predict`
3. Click "Try it out"
4. Fill in values:
   - variance: 3.6216
   - skewness: 8.6661
   - curtosis: -2.8073
   - entropy: -0.44699
5. Click "Execute"
6. See result: `{"prediction": 0}`

### Using cURL
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"variance":3.6216,"skewness":8.6661,"curtosis":-2.8073,"entropy":-0.44699}'
```

### Using Python
```python
import requests
r = requests.post("http://localhost:8000/predict", 
                  json={"variance":3.6216,"skewness":8.6661,"curtosis":-2.8073,"entropy":-0.44699})
print(r.json())  # {"prediction": 0}
```

---

## 🚨 Troubleshooting

### Port 8000 Already in Use
```bash
# Use different port
uvicorn main:app --port 8001
```

### Model Not Found
```
Error: FileNotFoundError: model.pkl
```
**Solution**: Ensure `model.pkl` is in the same directory as `main.py`

### Dependencies Missing
```bash
pip install -r requirements.txt
```

---

## 📊 Model Performance

```
Test Accuracy:       98.55% ✅
Training Accuracy:   99.18% ✅
Precision:           0.99
Recall:              0.98
F1-Score:            0.99

Confusion Matrix:
                    Predicted Genuine  Predicted Forged
Actual Genuine             146                2
Actual Forged              2               125
```

---

## 🔧 Environment Variables (Optional)

Create `.env` file:
```
API_TITLE=Bank Note Authentication API
API_VERSION=1.0
DEBUG=False
HOST=0.0.0.0
PORT=8000
```

---

## 📈 Scaling & Production

### Multiple Workers (Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

### Behind Load Balancer
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
# Or use nginx/haproxy in front
```

### Database Integration (Optional)
```python
# Add to main.py if needed
from sqlalchemy import create_engine
# log predictions to database
```

---

## 📚 Full Documentation

See `DEPLOYMENT_GUIDE.md` for:
- ✅ Azure deployment
- ✅ AWS Lambda deployment
- ✅ Heroku deployment
- ✅ Security recommendations
- ✅ Monitoring setup
- ✅ Advanced configuration

---

## 🎯 Next Steps

1. **Choose deployment method** (Docker recommended)
2. **Run the application**
3. **Test with sample data**
4. **Configure for your environment**
5. **Set up monitoring**
6. **Deploy to production**

---

## 💬 Questions?

Check `DEPLOYMENT_GUIDE.md` or contact the data science team.

---

**Version**: 1.0  
**Status**: ✅ Production Ready  
**Last Updated**: 2026-04-08
