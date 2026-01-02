"""
Customer Profile Data for Upgrade Recommendations Demo
15 diverse customer personas with realistic spending patterns and upgrade opportunities
"""

CUSTOMER_PROFILES = [
    {
        "customer_id": "CUST001",
        "name": "Sarah Chen",
        "age": 42,
        "occupation": "Marketing Director",
        "monthly_spend": 2150,
        "spend_categories": {
            "travel": 600,
            "groceries": 450,
            "gas": 220,
            "online_retail": 880
        },
        "credit_utilization": 84,
        "payment_behavior": "Pays minimum balance",
        "chargebacks_last_12mo": 1,
        "income_band": "75k - 120k",
        "card_type": "Standard Mastercard",
        "location": "Ontario, Canada",
        "account_age_months": 36,
        "credit_score_band": "Good (670-739)"
    },
    {
        "customer_id": "CUST002",
        "name": "James Rodriguez",
        "age": 28,
        "occupation": "Software Engineer",
        "monthly_spend": 4200,
        "spend_categories": {
            "dining": 1200,
            "entertainment": 800,
            "travel": 1500,
            "online_subscriptions": 700
        },
        "credit_utilization": 35,
        "payment_behavior": "Pays full balance",
        "chargebacks_last_12mo": 0,
        "income_band": "120k - 200k",
        "card_type": "Standard Mastercard",
        "location": "San Francisco, CA",
        "account_age_months": 18,
        "credit_score_band": "Excellent (740+)"
    },
    {
        "customer_id": "CUST003",
        "name": "Patricia Williams",
        "age": 67,
        "occupation": "Retired Teacher",
        "monthly_spend": 850,
        "spend_categories": {
            "groceries": 400,
            "pharmacy": 200,
            "utilities": 150,
            "gas": 100
        },
        "credit_utilization": 15,
        "payment_behavior": "Pays full balance",
        "chargebacks_last_12mo": 0,
        "income_band": "30k - 50k",
        "card_type": "Standard Mastercard",
        "location": "Phoenix, AZ",
        "account_age_months": 144,
        "credit_score_band": "Excellent (740+)"
    },
    {
        "customer_id": "CUST004",
        "name": "Michael Thompson",
        "age": 35,
        "occupation": "Sales Manager",
        "monthly_spend": 5800,
        "spend_categories": {
            "travel": 3200,
            "dining": 1400,
            "gas": 600,
            "hotels": 600
        },
        "credit_utilization": 62,
        "payment_behavior": "Pays full balance",
        "chargebacks_last_12mo": 0,
        "income_band": "120k - 200k",
        "card_type": "Gold Mastercard",
        "location": "Chicago, IL",
        "account_age_months": 48,
        "credit_score_band": "Very Good (700-739)"
    },
    {
        "customer_id": "CUST005",
        "name": "Emily Nguyen",
        "age": 24,
        "occupation": "Graduate Student",
        "monthly_spend": 1100,
        "spend_categories": {
            "groceries": 300,
            "online_retail": 400,
            "streaming_services": 150,
            "coffee_shops": 250
        },
        "credit_utilization": 78,
        "payment_behavior": "Pays minimum balance",
        "chargebacks_last_12mo": 2,
        "income_band": "20k - 40k",
        "card_type": "Student Mastercard",
        "location": "Boston, MA",
        "account_age_months": 12,
        "credit_score_band": "Fair (580-669)"
    },
    {
        "customer_id": "CUST006",
        "name": "Robert Martinez",
        "age": 51,
        "occupation": "Business Owner",
        "monthly_spend": 8500,
        "spend_categories": {
            "business_supplies": 3500,
            "dining": 2000,
            "travel": 2000,
            "gas": 1000
        },
        "credit_utilization": 45,
        "payment_behavior": "Pays full balance",
        "chargebacks_last_12mo": 1,
        "income_band": "200k+",
        "card_type": "Gold Mastercard",
        "location": "Miami, FL",
        "account_age_months": 72,
        "credit_score_band": "Excellent (740+)"
    },
    {
        "customer_id": "CUST007",
        "name": "Jennifer Lee",
        "age": 39,
        "occupation": "Nurse Practitioner",
        "monthly_spend": 2800,
        "spend_categories": {
            "groceries": 600,
            "gas": 400,
            "childcare": 1200,
            "online_retail": 600
        },
        "credit_utilization": 72,
        "payment_behavior": "Pays more than minimum",
        "chargebacks_last_12mo": 0,
        "income_band": "75k - 120k",
        "card_type": "Standard Mastercard",
        "location": "Seattle, WA",
        "account_age_months": 60,
        "credit_score_band": "Good (670-739)"
    },
    {
        "customer_id": "CUST008",
        "name": "David Kim",
        "age": 45,
        "occupation": "Airline Pilot",
        "monthly_spend": 6200,
        "spend_categories": {
            "travel": 2800,
            "dining": 1500,
            "hotels": 1200,
            "car_rental": 700
        },
        "credit_utilization": 28,
        "payment_behavior": "Pays full balance",
        "chargebacks_last_12mo": 0,
        "income_band": "120k - 200k",
        "card_type": "Gold Mastercard",
        "location": "Dallas, TX",
        "account_age_months": 84,
        "credit_score_band": "Excellent (740+)"
    },
    {
        "customer_id": "CUST009",
        "name": "Amanda Foster",
        "age": 31,
        "occupation": "Freelance Designer",
        "monthly_spend": 1850,
        "spend_categories": {
            "online_subscriptions": 450,
            "coffee_shops": 300,
            "groceries": 400,
            "online_retail": 700
        },
        "credit_utilization": 88,
        "payment_behavior": "Pays minimum balance",
        "chargebacks_last_12mo": 3,
        "income_band": "40k - 75k",
        "card_type": "Standard Mastercard",
        "location": "Portland, OR",
        "account_age_months": 24,
        "credit_score_band": "Fair (580-669)"
    },
    {
        "customer_id": "CUST010",
        "name": "Christopher Brown",
        "age": 58,
        "occupation": "Attorney",
        "monthly_spend": 7200,
        "spend_categories": {
            "dining": 2500,
            "travel": 2200,
            "professional_services": 1500,
            "entertainment": 1000
        },
        "credit_utilization": 22,
        "payment_behavior": "Pays full balance",
        "chargebacks_last_12mo": 0,
        "income_band": "200k+",
        "card_type": "Platinum Mastercard",
        "location": "New York, NY",
        "account_age_months": 120,
        "credit_score_band": "Excellent (740+)"
    },
    {
        "customer_id": "CUST011",
        "name": "Lisa Anderson",
        "age": 29,
        "occupation": "Fitness Instructor",
        "monthly_spend": 1650,
        "spend_categories": {
            "groceries": 500,
            "gas": 250,
            "fitness_equipment": 400,
            "online_retail": 500
        },
        "credit_utilization": 55,
        "payment_behavior": "Pays full balance",
        "chargebacks_last_12mo": 0,
        "income_band": "40k - 75k",
        "card_type": "Standard Mastercard",
        "location": "Austin, TX",
        "account_age_months": 30,
        "credit_score_band": "Good (670-739)"
    },
    {
        "customer_id": "CUST012",
        "name": "Kevin O'Brien",
        "age": 36,
        "occupation": "Construction Manager",
        "monthly_spend": 3200,
        "spend_categories": {
            "gas": 800,
            "home_improvement": 1200,
            "groceries": 600,
            "dining": 600
        },
        "credit_utilization": 68,
        "payment_behavior": "Pays more than minimum",
        "chargebacks_last_12mo": 1,
        "income_band": "75k - 120k",
        "card_type": "Standard Mastercard",
        "location": "Denver, CO",
        "account_age_months": 42,
        "credit_score_band": "Good (670-739)"
    },
    {
        "customer_id": "CUST013",
        "name": "Sophia Patel",
        "age": 33,
        "occupation": "Data Scientist",
        "monthly_spend": 3800,
        "spend_categories": {
            "online_retail": 1200,
            "dining": 900,
            "travel": 1000,
            "entertainment": 700
        },
        "credit_utilization": 42,
        "payment_behavior": "Pays full balance",
        "chargebacks_last_12mo": 0,
        "income_band": "120k - 200k",
        "card_type": "Gold Mastercard",
        "location": "San Jose, CA",
        "account_age_months": 36,
        "credit_score_band": "Excellent (740+)"
    },
    {
        "customer_id": "CUST014",
        "name": "Thomas Jackson",
        "age": 72,
        "occupation": "Retired Executive",
        "monthly_spend": 4500,
        "spend_categories": {
            "travel": 2000,
            "dining": 1200,
            "healthcare": 800,
            "entertainment": 500
        },
        "credit_utilization": 18,
        "payment_behavior": "Pays full balance",
        "chargebacks_last_12mo": 0,
        "income_band": "120k - 200k",
        "card_type": "Platinum Mastercard",
        "location": "Naples, FL",
        "account_age_months": 180,
        "credit_score_band": "Excellent (740+)"
    },
    {
        "customer_id": "CUST015",
        "name": "Rachel Green",
        "age": 26,
        "occupation": "Social Media Manager",
        "monthly_spend": 2400,
        "spend_categories": {
            "online_subscriptions": 600,
            "dining": 800,
            "online_retail": 700,
            "entertainment": 300
        },
        "credit_utilization": 65,
        "payment_behavior": "Pays more than minimum",
        "chargebacks_last_12mo": 1,
        "income_band": "40k - 75k",
        "card_type": "Standard Mastercard",
        "location": "Los Angeles, CA",
        "account_age_months": 20,
        "credit_score_band": "Good (670-739)"
    }
]

def get_all_customers():
    """Return list of all customer profiles with summary info"""
    return [
        {
            "customer_id": customer["customer_id"],
            "name": customer["name"],
            "age": customer["age"],
            "occupation": customer["occupation"],
            "monthly_spend": customer["monthly_spend"],
            "card_type": customer["card_type"],
            "location": customer["location"],
            "credit_utilization": customer["credit_utilization"]
        }
        for customer in CUSTOMER_PROFILES
    ]

def get_customer_profile(customer_id):
    """Get full customer profile by ID"""
    for customer in CUSTOMER_PROFILES:
        if customer["customer_id"] == customer_id:
            return customer
    return None
