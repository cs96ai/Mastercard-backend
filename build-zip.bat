@echo off
REM Backend ZIP Build Script for Windows
REM Author: Chris Sutherland (cs96ai@hotmail.com)
REM Creates a deployment ZIP for Azure App Service (Linux)

echo ========================================
echo Building Backend ZIP for Azure Deployment
echo ========================================
echo.

REM Clean up old dist folder if it exists
if exist dist (
    echo Cleaning old dist folder...
    rmdir /s /q dist
)

REM Create dist folder
echo Creating dist folder...
mkdir dist

REM Copy all Python files
echo Copying Python files...
copy *.py dist\
copy requirements.txt dist\

REM Create ZIP file
echo.
echo Creating backend-deploy.zip...
cd dist
powershell -Command "Compress-Archive -Path * -DestinationPath ..\backend-deploy.zip -Force"
cd ..

echo.
echo ========================================
echo Build Complete!
echo ========================================
echo.
echo ZIP file created: backend-deploy.zip
echo.
echo To deploy to Azure:
echo 1. Go to https://portal.azure.com
echo 2. Navigate to: mastercard-backend-csutherland
echo 3. Go to: Development Tools ^> Advanced Tools ^> Go
echo 4. In Kudu, go to: Tools ^> Zip Push Deploy
echo 5. Drag and drop: backend-deploy.zip
echo.
echo Target: https://mastercard-backend-csutherland.azurewebsites.net
echo.

pause
