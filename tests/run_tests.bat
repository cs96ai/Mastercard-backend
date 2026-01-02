@echo off
cd /d "%~dp0.."
echo ========================================
echo Mastercard API Integration Tests
echo ========================================
echo.
echo Current directory: %CD%
echo.
echo Installing test dependencies...
pip install -r tests\requirements-test.txt
echo.
echo Running integration tests against:
echo https://mastercardapi-csutherland.azurewebsites.net
echo.
echo ========================================
python -m pytest tests\test_integration.py -v --tb=short --html=tests\test_report.html --self-contained-html
echo.
echo ========================================
echo Test report generated: tests\test_report.html
echo ========================================
pause
