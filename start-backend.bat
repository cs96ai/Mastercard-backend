@echo off
echo Starting Mastercard Fraud Analysis Backend...
echo.
cd backend
echo Installing dependencies...
set PIP_TRUSTED_HOST=pypi.org files.pythonhosted.org pypi.python.org
set PIP_NO_VERIFY_CERTS=1
set PYTHONHTTPSVERIFY=0
set REQUESTS_CA_BUNDLE=
set CURL_CA_BUNDLE=
python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org --no-cache-dir -r requirements.txt
echo.
echo Starting FastAPI server on http://localhost:8000
echo.
python -m uvicorn main:app --reload --port 8000
