# Integration Tests for Mastercard API

This directory contains integration tests that call the actual deployed API at:
**https://mastercardapi-csutherland.azurewebsites.net**

## Test Structure

- `test_integration.py` - Main integration test suite
- `requirements-test.txt` - Test-specific dependencies
- `run_tests.bat` - Windows batch script to run tests
- `test_report.html` - Generated HTML test report (after running tests)

## Running Tests

### Windows
```bash
cd c:\code\MasterCard\Mastercard-backend
tests\run_tests.bat
```

### Manual (any OS)
```bash
# Install test dependencies
pip install -r tests/requirements-test.txt

# Run tests
pytest tests/test_integration.py -v

# Run with HTML report
pytest tests/test_integration.py -v --html=tests/test_report.html --self-contained-html
```

## Test Coverage

### Health Endpoints
- ✓ Root endpoint (`/`)
- ✓ Heartbeat endpoint (`/api/heartbeat`)

### Fraud Scenarios API
- ✓ Get all scenarios
- ✓ Validate scenario structure
- ✓ Analyze fraud (Risk Analyst audience)
- ✓ Analyze fraud (Executive Summary audience)
- ✓ Analyze fraud (Customer-friendly audience)
- ✓ Invalid scenario ID handling

### Merchant API
- ✓ Get merchant list
- ✓ Get merchant details
- ✓ Generate merchant narrative
- ✓ Merchant not found handling

### Customer API
- ✓ Get customer list
- ✓ Get customer details
- ✓ Analyze customer upgrade (Executive mode)
- ✓ Analyze customer upgrade (JSON format)

### Dispute API
- ✓ Get dispute cases
- ✓ Get dispute details
- ✓ Analyze dispute (forensic analysis)
- ✓ Dispute not found handling

### Error Handling
- ✓ Missing required fields
- ✓ Invalid JSON
- ✓ Non-existent endpoints

## Test Data

All tests use real data from the deployed API. No mocking is performed - these are true integration tests that verify:
1. API endpoints are accessible
2. Response structures are correct
3. Data validation works properly
4. Error handling is appropriate
5. AI analysis endpoints function correctly

## Notes

- Tests require internet connectivity to reach the Azure deployment
- Some tests call OpenAI API endpoints and may take longer to complete
- Test failures may indicate API downtime or configuration issues
