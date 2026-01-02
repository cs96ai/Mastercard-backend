"""
Integration tests for Mastercard API
Tests the actual deployed API at https://mastercardapi-csutherland.azurewebsites.net/
"""

import requests
import pytest
from typing import Dict, Any

BASE_URL = "https://mastercardapi-csutherland.azurewebsites.net"


class TestHealthEndpoints:
    """Test basic health and connectivity endpoints"""
    
    def test_root_endpoint(self):
        """Test the root endpoint returns status"""
        response = requests.get(f"{BASE_URL}/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "status" in data
        assert data["status"] == "running"
    
    def test_heartbeat_endpoint(self):
        """Test the heartbeat endpoint"""
        response = requests.get(f"{BASE_URL}/api/heartbeat")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "running"
        assert "timestamp" in data
        assert "message" in data


class TestFraudScenariosAPI:
    """Test fraud scenario endpoints"""
    
    def test_get_scenarios(self):
        """Test retrieving fraud scenarios"""
        response = requests.get(f"{BASE_URL}/api/scenarios")
        assert response.status_code == 200
        data = response.json()
        
        assert "scenarios" in data
        assert "total" in data
        assert isinstance(data["scenarios"], list)
        assert data["total"] > 0
        assert len(data["scenarios"]) == data["total"]
    
    def test_scenarios_structure(self):
        """Test that scenarios have the correct structure"""
        response = requests.get(f"{BASE_URL}/api/scenarios")
        data = response.json()
        
        scenario = data["scenarios"][0]
        
        assert "id" in scenario
        assert "case_name" in scenario
        assert "account" in scenario
        assert "flagged_transaction" in scenario
        assert "fraud_indicators" in scenario
        assert "historical_transactions" in scenario
        
        assert "account_number" in scenario["account"]
        assert "cardholder_name" in scenario["account"]
        
        assert "amount" in scenario["flagged_transaction"]
        assert "merchant" in scenario["flagged_transaction"]
        assert "location" in scenario["flagged_transaction"]
    
    def test_analyze_fraud_risk_analyst(self):
        """Test fraud analysis with Risk Analyst audience"""
        payload = {
            "scenario_id": 0,
            "audience": "Risk Analyst"
        }
        
        response = requests.post(f"{BASE_URL}/api/analyze-fraud", json=payload)
        assert response.status_code == 200
        data = response.json()
        
        assert "analysis" in data
        assert "scenario" in data
        assert "audience" in data
        assert data["audience"] == "Risk Analyst"
        assert len(data["analysis"]) > 0
    
    def test_analyze_fraud_executive(self):
        """Test fraud analysis with Executive Summary audience"""
        payload = {
            "scenario_id": 0,
            "audience": "Executive Summary"
        }
        
        response = requests.post(f"{BASE_URL}/api/analyze-fraud", json=payload)
        assert response.status_code == 200
        data = response.json()
        
        assert data["audience"] == "Executive Summary"
        assert len(data["analysis"]) > 0
    
    def test_analyze_fraud_customer_friendly(self):
        """Test fraud analysis with Customer-friendly audience"""
        payload = {
            "scenario_id": 0,
            "audience": "Customer-friendly"
        }
        
        response = requests.post(f"{BASE_URL}/api/analyze-fraud", json=payload)
        assert response.status_code == 200
        data = response.json()
        
        assert data["audience"] == "Customer-friendly"
        assert len(data["analysis"]) > 0
    
    def test_analyze_fraud_invalid_scenario(self):
        """Test fraud analysis with invalid scenario ID"""
        payload = {
            "scenario_id": 9999,
            "audience": "Risk Analyst"
        }
        
        response = requests.post(f"{BASE_URL}/api/analyze-fraud", json=payload)
        assert response.status_code == 404


class TestMerchantAPI:
    """Test merchant endpoints"""
    
    def test_get_merchants(self):
        """Test retrieving merchant list"""
        response = requests.get(f"{BASE_URL}/api/merchants")
        assert response.status_code == 200
        data = response.json()
        
        assert "merchants" in data
        assert isinstance(data["merchants"], list)
        assert len(data["merchants"]) > 0
        
        merchant = data["merchants"][0]
        assert "id" in merchant
        assert "name" in merchant
        assert "business_type" in merchant
    
    def test_get_merchant_detail(self):
        """Test retrieving specific merchant data"""
        merchants_response = requests.get(f"{BASE_URL}/api/merchants")
        merchants = merchants_response.json()["merchants"]
        merchant_id = merchants[0]["id"]
        
        response = requests.get(f"{BASE_URL}/api/merchants/{merchant_id}")
        assert response.status_code == 200
        data = response.json()
        
        assert "name" in data
        assert "business_type" in data
        assert "monthly_data" in data
        assert isinstance(data["monthly_data"], list)
        assert len(data["monthly_data"]) == 12
    
    def test_generate_merchant_narrative(self):
        """Test merchant narrative generation"""
        merchants_response = requests.get(f"{BASE_URL}/api/merchants")
        merchants = merchants_response.json()["merchants"]
        merchant_id = merchants[0]["id"]
        
        payload = {"merchant_id": merchant_id}
        
        response = requests.post(f"{BASE_URL}/api/generate-merchant-narrative", json=payload)
        assert response.status_code == 200
        data = response.json()
        
        assert data["success"] is True
        assert "narrative" in data
        assert "merchant_name" in data
        assert len(data["narrative"]) > 0
    
    def test_merchant_not_found(self):
        """Test retrieving non-existent merchant"""
        response = requests.get(f"{BASE_URL}/api/merchants/invalid-merchant-id")
        assert response.status_code == 404


class TestCustomerAPI:
    """Test customer profile endpoints"""
    
    def test_get_customers(self):
        """Test retrieving customer list"""
        response = requests.get(f"{BASE_URL}/api/customers")
        assert response.status_code == 200
        data = response.json()
        
        assert "customers" in data
        assert isinstance(data["customers"], list)
        assert len(data["customers"]) > 0
        
        customer = data["customers"][0]
        assert "customer_id" in customer or "id" in customer
        assert "name" in customer
        assert "card_type" in customer or "current_card" in customer
    
    def test_get_customer_detail(self):
        """Test retrieving specific customer profile"""
        customers_response = requests.get(f"{BASE_URL}/api/customers")
        customers = customers_response.json()["customers"]
        customer_id = customers[0].get("customer_id") or customers[0].get("id")
        
        response = requests.get(f"{BASE_URL}/api/customers/{customer_id}")
        assert response.status_code == 200
        data = response.json()
        
        assert "name" in data
        assert "age" in data
        assert "card_type" in data or "current_card" in data
        assert "spending_behavior" in data or "spending_patterns" in data or "monthly_spend" in data
    
    def test_analyze_customer_upgrade_executive(self):
        """Test customer upgrade analysis in Executive mode"""
        customers_response = requests.get(f"{BASE_URL}/api/customers")
        customers = customers_response.json()["customers"]
        customer_id = customers[0].get("customer_id") or customers[0].get("id")
        
        payload = {
            "customer_id": customer_id,
            "output_mode": "Executive",
            "format_mode": "Narrative"
        }
        
        response = requests.post(f"{BASE_URL}/api/analyze-customer-upgrade", json=payload)
        assert response.status_code == 200
        data = response.json()
        
        assert data["success"] is True
        assert "recommendation" in data
        assert "customer_name" in data
        assert data["output_mode"] == "Executive"
    
    def test_analyze_customer_upgrade_json_format(self):
        """Test customer upgrade analysis in JSON format"""
        customers_response = requests.get(f"{BASE_URL}/api/customers")
        customers = customers_response.json()["customers"]
        customer_id = customers[0].get("customer_id") or customers[0].get("id")
        
        payload = {
            "customer_id": customer_id,
            "output_mode": "Analyst",
            "format_mode": "JSON"
        }
        
        response = requests.post(f"{BASE_URL}/api/analyze-customer-upgrade", json=payload)
        assert response.status_code == 200
        data = response.json()
        
        assert data["success"] is True
        assert data["format_mode"] == "JSON"


class TestDisputeAPI:
    """Test dispute case endpoints"""
    
    def test_get_disputes(self):
        """Test retrieving dispute cases"""
        response = requests.get(f"{BASE_URL}/api/disputes")
        assert response.status_code == 200
        data = response.json()
        
        assert "disputes" in data
        assert isinstance(data["disputes"], list)
        assert len(data["disputes"]) > 0
        
        dispute = data["disputes"][0]
        assert "case_id" in dispute
        assert "customer_claim" in dispute or "customer_name" in dispute
        assert "item" in dispute or "dispute_amount" in dispute
    
    def test_get_dispute_detail(self):
        """Test retrieving specific dispute case"""
        disputes_response = requests.get(f"{BASE_URL}/api/disputes")
        disputes = disputes_response.json()["disputes"]
        case_id = disputes[0]["case_id"]
        
        response = requests.get(f"{BASE_URL}/api/disputes/{case_id}")
        assert response.status_code == 200
        data = response.json()
        
        assert "case_id" in data
        assert "dispute_details" in data or "customer_claim" in data
        assert "merchant_evidence" in data
        assert "status" in data
    
    def test_analyze_dispute(self):
        """Test dispute forensic analysis"""
        disputes_response = requests.get(f"{BASE_URL}/api/disputes")
        disputes = disputes_response.json()["disputes"]
        case_id = disputes[0]["case_id"]
        
        payload = {"case_id": case_id}
        
        response = requests.post(f"{BASE_URL}/api/analyze-dispute", json=payload)
        assert response.status_code == 200
        data = response.json()
        
        assert data["success"] is True
        assert "analysis" in data
        assert "case_id" in data
        assert len(data["analysis"]) > 0
    
    def test_dispute_not_found(self):
        """Test analyzing non-existent dispute"""
        payload = {"case_id": "invalid-case-id"}
        
        response = requests.post(f"{BASE_URL}/api/analyze-dispute", json=payload)
        assert response.status_code == 404


class TestErrorHandling:
    """Test error handling and edge cases"""
    
    def test_missing_required_fields(self):
        """Test API with missing required fields"""
        response = requests.post(f"{BASE_URL}/api/analyze-fraud", json={})
        assert response.status_code == 422
    
    def test_invalid_json(self):
        """Test API with invalid JSON"""
        response = requests.post(
            f"{BASE_URL}/api/analyze-fraud",
            data="invalid json",
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 422
    
    def test_nonexistent_endpoint(self):
        """Test calling non-existent endpoint"""
        response = requests.get(f"{BASE_URL}/api/nonexistent")
        assert response.status_code == 404


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
