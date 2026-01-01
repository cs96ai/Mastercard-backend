"""
Mastercard AI Demo Application - Backend API
Author: Chris Sutherland
Email: cs96ai@hotmail.com
Phone: 416-839-9499

FastAPI backend providing AI-powered financial analysis endpoints:
- Fraud case analysis with multi-audience explanations
- Merchant insights narrative generation
- Customer upgrade recommendations
- First-party fraud detection (friendly fraud)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import json
import os
from datetime import datetime
from fraud_scenarios import get_fraud_scenarios
from merchant_data import get_all_merchants, get_merchant_data
from customer_profiles import get_all_customers, get_customer_profile
from dispute_cases import get_all_disputes, get_dispute_case
import random

app = FastAPI(title="Mastercard Fraud Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "https://mastercard-csutherland.azurewebsites.net",
        "https://mastercard-backend-csutherland.azurewebsites.net"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def require_openai_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured on server")
    return api_key

class FraudAnalysisRequest(BaseModel):
    scenario_id: int
    audience: str

@app.get("/api/scenarios")
async def get_scenarios():
    scenarios = get_fraud_scenarios()
    return {"scenarios": scenarios, "total": len(scenarios)}

@app.post("/api/analyze-fraud")
async def analyze_fraud(request: FraudAnalysisRequest):
    api_key = require_openai_api_key()
    
    scenarios = get_fraud_scenarios()
    
    if request.scenario_id < 0 or request.scenario_id >= len(scenarios):
        raise HTTPException(status_code=404, detail="Scenario not found")
    
    scenario = scenarios[request.scenario_id]
    
    prompt = create_fraud_analysis_prompt(scenario, request.audience)
    
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a fraud analysis expert for Mastercard. Analyze transaction data and explain fraud risks clearly."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )
        
        analysis = response.choices[0].message.content
        
        return {
            "scenario": scenario,
            "analysis": analysis,
            "audience": request.audience
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")

def create_fraud_analysis_prompt(scenario: dict, audience: str) -> str:
    audience_instructions = {
        "Risk Analyst": "Provide a detailed technical analysis with specific fraud indicators, risk scores, and model reasoning. Use industry terminology.",
        "Executive Summary": "Provide a concise, high-level summary focusing on business impact and key risk factors. Keep it brief and actionable.",
        "Customer-friendly": "Explain in simple, non-technical language that a cardholder would understand. Be empathetic and clear."
    }
    
    instruction = audience_instructions.get(audience, audience_instructions["Risk Analyst"])
    
    scenario_json = json.dumps(scenario, indent=2)
    
    prompt = f"""Analyze this transaction that was flagged for potential fraud:

{scenario_json}

Audience: {audience}
Instructions: {instruction}

Please provide:
1. A risk score assessment (Low/Medium/High/Critical)
2. Key fraud indicators identified
3. Explanation of why this transaction was flagged
4. Recommended action

Format your response appropriately for the {audience} audience."""
    
    return prompt

@app.get("/")
async def root():
    return {"message": "Mastercard Fraud Analysis API", "status": "running"}

@app.get("/api/heartbeat")
async def heartbeat():
    """Health check endpoint that returns current server datetime"""
    return {
        "status": "running",
        "timestamp": datetime.now().isoformat(),
        "message": "Mastercard Fraud Analysis API is operational"
    }

@app.post("/api/test-connection")
async def test_connection():
    api_key = require_openai_api_key()
    
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'Connection successful!' if you can read this."}
            ],
            max_tokens=50
        )
        
        return {
            "success": True,
            "message": "API connection successful",
            "response": response.choices[0].message.content,
            "model": response.model
        }
    except Exception as e:
        return {
            "success": False,
            "message": "API connection failed",
            "error": str(e)
        }

@app.post("/api/test-prompt")
async def test_prompt(request: dict):
    api_key = require_openai_api_key()
    
    prompt = request.get("prompt", "Hello!")
    
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        
        return {
            "success": True,
            "response": response.choices[0].message.content,
            "model": response.model,
            "usage": {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/merchants")
async def get_merchants():
    """Get list of all merchant personas"""
    return get_all_merchants()

@app.get("/api/merchants/{merchant_id}")
async def get_merchant(merchant_id: str):
    """Get full merchant data including 12 months of KPIs"""
    merchant = get_merchant_data(merchant_id)
    if not merchant:
        raise HTTPException(status_code=404, detail="Merchant not found")
    return merchant

@app.post("/api/generate-merchant-narrative")
async def generate_merchant_narrative(request: dict):
    """Generate AI narrative report for a merchant"""
    api_key = require_openai_api_key()
    
    merchant_id = request.get("merchant_id")
    if not merchant_id:
        raise HTTPException(status_code=400, detail="merchant_id is required")
    
    merchant = get_merchant_data(merchant_id)
    if not merchant:
        raise HTTPException(status_code=404, detail="Merchant not found")
    
    try:
        # Build the prompt with merchant data
        prompt = build_merchant_narrative_prompt(merchant)
        
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Senior Strategic Fintech Consultant acting as a Virtual CFO."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        
        narrative = response.choices[0].message.content
        
        return {
            "success": True,
            "narrative": narrative,
            "merchant_name": merchant["name"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def build_merchant_narrative_prompt(merchant):
    """Build the master prompt for merchant narrative generation"""
    
    # Convert monthly data to JSON string
    monthly_data_json = json.dumps(merchant["monthly_data"], indent=2)
    
    prompt = f"""You are provided with a JSON dataset containing 12 months of KPI data for a specific merchant. Your task is to act as their 'Virtual CFO' and generate a highly structured, actionable 'Merchant Growth & Health Narrative.'

**Merchant Profile:**
- Name: {merchant["name"]}
- Business Type: {merchant["business_type"]}
- Location: {merchant["location"]}
- Known Business Challenge: {merchant["problem_statement"]}

**12-Month KPI Data:**
{monthly_data_json}

**Your Task:**
Generate a comprehensive strategic report with the following sections:

1. **Executive Scorecard**: A 2-sentence summary of the business's current state (e.g., 'Scaling Rapidly,' 'Efficiency Recovery Phase,' or 'Churn Risk Alert').

2. **The "Why" Behind the Numbers**: Explain one non-obvious correlation in the data (e.g., how a change in Average Ticket Size relates to transaction volume, or how Saturday revenue patterns affect overall performance).

3. **Anomaly Detection**: Identify the most significant outlier in the last 90 days (last 3 months of data) and hypothesize a business reason for it (e.g., a sudden spike in chargebacks, terminal latency issues, or seasonal patterns).

4. **Strategic Roadmap**: Provide 3 hyper-specific, actionable recommendations. Do NOT use generic advice like 'increase sales.' Instead, use the data to suggest concrete actions like:
   - "Implement a tiered loyalty program to capture the top 10% of high-frequency shoppers"
   - "Address terminal latency during peak hours to reduce walk-away losses"
   - "Investigate the correlation between refund rates and product descriptions"

5. **Risk Assessment**: Flag any brewing issues in Chargeback rates, Refund rates, Terminal Downtime, or Customer Retention that require immediate attention.

**Tone**: Professional, encouraging, and data-driven. Avoid fluff. Be specific and reference actual numbers from the data.

Format your response with clear section headers using **bold** for section titles."""
    
    return prompt

@app.get("/api/customers")
async def get_customers():
    """Get list of all customer profiles"""
    return get_all_customers()

@app.get("/api/customers/{customer_id}")
async def get_customer(customer_id: str):
    """Get full customer profile"""
    customer = get_customer_profile(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.post("/api/analyze-customer-upgrade")
async def analyze_customer_upgrade(request: dict):
    """Generate AI upgrade recommendations for a customer"""
    api_key = require_openai_api_key()
    
    customer_id = request.get("customer_id")
    output_mode = request.get("output_mode", "Executive")
    format_mode = request.get("format_mode", "JSON")
    
    if not customer_id:
        raise HTTPException(status_code=400, detail="customer_id is required")
    
    customer = get_customer_profile(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    try:
        prompt = build_customer_upgrade_prompt(customer, output_mode, format_mode)
        
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Mastercard AI – Internal Product Strategy Assistant. You analyze credit card customers to identify upgrade opportunities that increase revenue, retention, and cardholder satisfaction."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        
        recommendation = response.choices[0].message.content
        
        return {
            "success": True,
            "customer_name": customer["name"],
            "recommendation": recommendation,
            "output_mode": output_mode,
            "format_mode": format_mode
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def build_customer_upgrade_prompt(customer, output_mode, format_mode):
    """Build the prompt for customer upgrade recommendations"""
    
    customer_json = json.dumps(customer, indent=2)
    
    prompt = f"""SYSTEM:
You are Mastercard AI – Internal Product Strategy Assistant.
You analyze fictitious credit card customers to identify upgrade opportunities that increase revenue, retention, and cardholder satisfaction.
You NEVER reference Mastercard confidential data. All examples are generic / public-safe.
Respond using professional, concise wording suitable for an internal Mastercard strategy review.

USER INPUT:
CUSTOMER_PROFILE:
{customer_json}

OUTPUT_MODE: "{output_mode}"
FORMAT: "{format_mode}"

TASK:
Based on CUSTOMER_PROFILE, determine:

1. Their spending patterns
2. Their probable financial behavior
3. Which upgrade(s) would fit:
   - Premium card tier (cashback, travel rewards, concierge)
   - Fraud-protection or subscription-management add-ons
   - Credit limit increase or BNPL offers
4. Why the upgrade makes sense (business justification + customer value)
5. A 1-to-3 sentence pitch that could be emailed or shown in-app (OPTIONAL, only if OUTPUT_MODE is "Customer-friendly")

"""

    if format_mode == "JSON":
        prompt += """
Please provide your response in the following JSON structure:
{{
  "recommended_upgrades": [
    {{
      "offer": "Upgrade name",
      "reasoning": "Why this fits the customer's behavior",
      "business_value": "Revenue/retention impact for Mastercard",
      "customer_value_statement": "Customer-facing benefit statement"
    }}
  ]
}}
"""
    else:
        prompt += """
Please provide a narrative response with clear sections:
- **Spending Analysis**
- **Recommended Upgrades**
- **Business Justification**
- **Customer Pitch** (if Customer-friendly mode)
"""

    if output_mode == "Executive":
        prompt += "\nTone: Concise, strategic, business-focused. Highlight ROI and retention metrics."
    elif output_mode == "Analyst":
        prompt += "\nTone: Detailed, data-driven, analytical. Include specific numbers and behavioral patterns."
    elif output_mode == "Customer-friendly":
        prompt += "\nTone: Warm, benefit-focused, easy to understand. Emphasize value to the customer."
    
    return prompt

@app.get("/api/disputes")
async def get_disputes():
    """Get list of all dispute cases"""
    return get_all_disputes()

@app.get("/api/disputes/{case_id}")
async def get_dispute(case_id: str):
    """Get full dispute case details"""
    dispute = get_dispute_case(case_id)
    if not dispute:
        raise HTTPException(status_code=404, detail="Dispute case not found")
    return dispute

@app.post("/api/analyze-dispute")
async def analyze_dispute(request: dict):
    """Run forensic analysis on a dispute case to detect first-party fraud"""
    api_key = require_openai_api_key()
    
    case_id = request.get("case_id")
    if not case_id:
        raise HTTPException(status_code=400, detail="case_id is required")
    
    dispute = get_dispute_case(case_id)
    if not dispute:
        raise HTTPException(status_code=404, detail="Dispute case not found")
    
    try:
        prompt = build_dispute_analysis_prompt(dispute)
        
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are the 'Mastercard First-Party Trust AI,' a specialized forensic agent designed to identify 'Friendly Fraud' (First-Party Misuse). Your goal is to analyze transaction disputes by cross-referencing customer claims against merchant telemetry and carrier evidence."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        
        analysis = response.choices[0].message.content
        
        return {
            "success": True,
            "case_id": case_id,
            "analysis": analysis
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def build_dispute_analysis_prompt(dispute):
    """Build the forensic analysis prompt for dispute investigation"""
    
    dispute_json = json.dumps(dispute, indent=2)
    
    prompt = f"""You are analyzing a chargeback dispute to determine if it is legitimate or 'Friendly Fraud' (first-party misuse).

DISPUTE CASE:
{dispute_json}

INSTRUCTIONS:

1. **Analyze Inconsistencies**: Compare the 'Customer Dispute Reason' against the 'Merchant Evidence Bundle.' Look for contradictions, impossible claims, or suspicious patterns.

2. **Assign a Trust Score** (0-100):
   - 0-20: High-confidence fraud (customer is lying)
   - 21-40: Likely fraud (strong evidence against customer)
   - 41-60: Uncertain (conflicting evidence)
   - 61-80: Likely legitimate (customer claim seems valid)
   - 81-100: High-confidence legitimate (strong evidence supports customer)

3. **Draft an Evidence Summary**: Write a concise, professional summary to be sent to the issuing bank. This should be objective and evidence-based.

4. **Highlight Smoking Guns**: Explicitly point out specific data points that prove or disprove the customer's claim. Examples:
   - GPS coordinates matching home address
   - Signature matching cardholder name
   - Device activation logs
   - Social media posts
   - Usage patterns
   - Access logs

5. **Provide a Recommendation**: 
   - "Deny Chargeback" (if fraud detected)
   - "Approve Chargeback" (if legitimate)
   - "Request Additional Evidence" (if uncertain)

**TONE**: Objective, evidence-based, and authoritative. Act like a forensic investigator presenting findings to a judge.

**FORMAT YOUR RESPONSE AS**:

**AI Dispute Analysis: [CASE_ID]**
**Trust Score**: [0-100]/100 ([Risk Level])

**Evidence Summary**:
[Your analysis of what the evidence shows]

**Key Inconsistencies** (or **Supporting Evidence** if legitimate):
[Bullet points of specific contradictions or confirmations]

**Smoking Gun Evidence**:
[The most damning or exonerating piece of evidence]

**Recommendation**:
[Your final recommendation with brief justification]
"""
    
    return prompt
