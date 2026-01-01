# Mastercard Fraud Analysis API

FastAPI backend for fraud case analysis using ChatGPT.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `POST /api/set-api-key` - Set OpenAI API key
- `GET /api/scenarios` - Get all fraud scenarios
- `POST /api/analyze-fraud` - Analyze a fraud case with ChatGPT

## Note

You'll need to provide your OpenAI API key through the frontend interface.
