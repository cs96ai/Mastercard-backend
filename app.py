"""
Mastercard AI Demo Application - Backend API
Author: Chris Sutherland
Email: cs96ai@hotmail.com
Phone: 416-839-9499

Azure App Service Entry Point
This file is required for Azure deployment (Azure looks for app.py)

Updated: 2024-12-31 - Simplified deployment
Deployment triggered: latest update
"""

from fastapi import FastAPI, HTTPException
from datetime import datetime
import traceback
import sys

app = FastAPI(title="Mastercard Fraud Analysis API", debug=True)

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler to show detailed error information"""
    error_detail = {
        "error": str(exc),
        "error_type": type(exc).__name__,
        "traceback": traceback.format_exc(),
        "url": str(request.url),
        "method": request.method
    }

    # Log the error
    print(f"ERROR: {error_detail}", file=sys.stderr)

    # Return detailed error in development
    return {
        "status": "error",
        "message": "Internal Server Error",
        "details": error_detail
    }

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
