"""
Mastercard AI Demo Application - Backend API
Author: Chris Sutherland
Email: cs96ai@hotmail.com
Phone: 416-839-9499

Azure App Service Entry Point
This file is required for Azure deployment (Azure looks for app.py)
"""

from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Mastercard Fraud Analysis API")

@app.get("/")
async def root():
    return {
        "message": "Mastercard API",
        "status": "running",
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
