"""
Mastercard AI Demo Application - Backend API
Author: Chris Sutherland
Email: cs96ai@hotmail.com
Phone: 416-839-9499

Azure App Service Entry Point
This file is required for Azure deployment (Azure looks for app.py)
"""

from main import app

# Azure App Service will look for 'app' variable
# The actual FastAPI application is defined in main.py

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
