import random
from datetime import datetime, timedelta

def get_fraud_scenarios():
    scenarios = [
        {
            "id": 0,
            "case_name": "High-Value International Purchase",
            "account": {
                "account_number": "****-****-****-4521",
                "cardholder_name": "Sarah Johnson",
                "account_age_days": 1247,
                "address": "123 Oak Street, Boston, MA 02108",
                "typical_monthly_spend": 2840.50,
                "past_chargebacks": 0
            },
            "flagged_transaction": {
                "amount": 4599.99,
                "merchant": "Electronics Mega Store",
                "mcc": "5732",
                "mcc_description": "Electronics Stores",
                "location": "Tokyo, Japan",
                "timestamp": "2024-12-30T23:47:12Z",
                "device_id": "DEVICE_UNKNOWN_7X9K",
                "card_present": False,
                "ip_address": "103.45.221.89",
                "transaction_id": "TXN-2024-1230-894521"
            },
            "fraud_indicators": {
                "geographic_velocity": "High - Card used in Japan 2 hours after US transaction",
                "transaction_amount_anomaly": "162% above typical transaction size",
                "device_fingerprint": "New/Unknown device",
                "merchant_category_risk": "High-risk category for fraud",
                "time_of_day": "Unusual - Outside normal spending hours",
                "card_not_present": True,
                "ip_geolocation_mismatch": "IP location doesn't match billing address",
                "velocity_24h": "3 transactions in 24h vs avg 0.8",
                "spending_spike": "4.2x normal daily spend",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-30", "amount": 45.23, "merchant": "Coffee Shop", "location": "Boston, MA"},
                {"date": "2024-12-29", "amount": 127.50, "merchant": "Grocery Store", "location": "Boston, MA"},
                {"date": "2024-12-28", "amount": 89.99, "merchant": "Gas Station", "location": "Boston, MA"},
                {"date": "2024-12-27", "amount": 234.00, "merchant": "Restaurant", "location": "Boston, MA"}
            ]
        },
        {
            "id": 1,
            "case_name": "Rapid Small Transaction Pattern",
            "account": {
                "account_number": "****-****-****-8832",
                "cardholder_name": "Michael Chen",
                "account_age_days": 89,
                "address": "456 Pine Ave, Seattle, WA 98101",
                "typical_monthly_spend": 1250.00,
                "past_chargebacks": 1
            },
            "flagged_transaction": {
                "amount": 9.99,
                "merchant": "Online Gaming Store",
                "mcc": "5816",
                "mcc_description": "Digital Goods - Games",
                "location": "Online - Singapore",
                "timestamp": "2024-12-31T03:22:45Z",
                "device_id": "DEVICE_MOB_4K2L",
                "card_present": False,
                "ip_address": "185.220.101.47",
                "transaction_id": "TXN-2024-1231-003845"
            },
            "fraud_indicators": {
                "transaction_frequency": "15 transactions in 2 hours",
                "micro_transaction_pattern": "Multiple small amounts - card testing behavior",
                "new_account_risk": "Account less than 90 days old",
                "merchant_category_risk": "Digital goods - high fraud category",
                "time_of_day": "3 AM local time - unusual",
                "card_not_present": True,
                "ip_geolocation_mismatch": "VPN/Proxy detected",
                "velocity_24h": "15 transactions vs avg 2.1",
                "spending_spike": "Normal amount but abnormal frequency",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-30", "amount": 52.30, "merchant": "Supermarket", "location": "Seattle, WA"},
                {"date": "2024-12-28", "amount": 125.00, "merchant": "Clothing Store", "location": "Seattle, WA"},
                {"date": "2024-12-26", "amount": 78.45, "merchant": "Restaurant", "location": "Seattle, WA"}
            ]
        },
        {
            "id": 2,
            "case_name": "Luxury Goods Purchase - New Merchant",
            "account": {
                "account_number": "****-****-****-2109",
                "cardholder_name": "Emily Rodriguez",
                "account_age_days": 2156,
                "address": "789 Maple Dr, Miami, FL 33101",
                "typical_monthly_spend": 3200.00,
                "past_chargebacks": 0
            },
            "flagged_transaction": {
                "amount": 8750.00,
                "merchant": "Luxury Watches International",
                "mcc": "5944",
                "mcc_description": "Jewelry Stores",
                "location": "Dubai, UAE",
                "timestamp": "2024-12-30T18:15:33Z",
                "device_id": "DEVICE_WEB_9M3N",
                "card_present": False,
                "ip_address": "94.200.45.123",
                "transaction_id": "TXN-2024-1230-781533"
            },
            "fraud_indicators": {
                "high_value_transaction": "2.7x monthly average spend",
                "new_merchant": "First transaction with this merchant",
                "luxury_goods_category": "High-risk category for fraud",
                "geographic_anomaly": "Transaction in UAE, no travel history",
                "card_not_present": True,
                "device_fingerprint": "Browser fingerprint not recognized",
                "ip_geolocation_mismatch": "IP in UAE, billing in USA",
                "velocity_24h": "1 large transaction vs typical pattern",
                "spending_spike": "Significantly above normal",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-29", "amount": 156.78, "merchant": "Department Store", "location": "Miami, FL"},
                {"date": "2024-12-28", "amount": 89.50, "merchant": "Gas Station", "location": "Miami, FL"},
                {"date": "2024-12-27", "amount": 245.00, "merchant": "Spa & Salon", "location": "Miami, FL"},
                {"date": "2024-12-25", "amount": 432.10, "merchant": "Restaurant", "location": "Miami, FL"}
            ]
        },
        {
            "id": 3,
            "case_name": "ATM Cash Withdrawal Spike",
            "account": {
                "account_number": "****-****-****-6754",
                "cardholder_name": "David Thompson",
                "account_age_days": 892,
                "address": "321 Elm St, Chicago, IL 60601",
                "typical_monthly_spend": 1890.00,
                "past_chargebacks": 2
            },
            "flagged_transaction": {
                "amount": 1000.00,
                "merchant": "ATM Withdrawal",
                "mcc": "6011",
                "mcc_description": "ATM Cash Disbursement",
                "location": "Mexico City, Mexico",
                "timestamp": "2024-12-31T01:45:22Z",
                "device_id": "ATM_7845KL",
                "card_present": True,
                "ip_address": "N/A",
                "transaction_id": "TXN-2024-1231-014522"
            },
            "fraud_indicators": {
                "atm_withdrawal_pattern": "3 max withdrawals in 4 hours",
                "geographic_velocity": "Card in Mexico 6 hours after Chicago use",
                "high_value_cash": "Maximum daily withdrawal amount",
                "past_chargeback_history": "2 previous chargebacks on account",
                "time_of_day": "1:45 AM - unusual for cardholder",
                "card_present": True,
                "foreign_atm": "International ATM usage without travel notice",
                "velocity_24h": "3 ATM withdrawals vs avg 0.2",
                "spending_spike": "Cash withdrawal pattern unusual",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-30", "amount": 67.89, "merchant": "Coffee Shop", "location": "Chicago, IL"},
                {"date": "2024-12-29", "amount": 145.23, "merchant": "Grocery Store", "location": "Chicago, IL"},
                {"date": "2024-12-28", "amount": 95.00, "merchant": "Gas Station", "location": "Chicago, IL"},
                {"date": "2024-12-27", "amount": 189.50, "merchant": "Restaurant", "location": "Chicago, IL"}
            ]
        },
        {
            "id": 4,
            "case_name": "Gift Card Purchase Pattern",
            "account": {
                "account_number": "****-****-****-3398",
                "cardholder_name": "Jennifer Lee",
                "account_age_days": 1567,
                "address": "654 Birch Ln, Austin, TX 78701",
                "typical_monthly_spend": 2100.00,
                "past_chargebacks": 0
            },
            "flagged_transaction": {
                "amount": 500.00,
                "merchant": "Big Box Retailer",
                "mcc": "5311",
                "mcc_description": "Department Stores",
                "location": "Austin, TX",
                "timestamp": "2024-12-30T22:33:18Z",
                "device_id": "DEVICE_POS_8N4M",
                "card_present": True,
                "ip_address": "N/A",
                "transaction_id": "TXN-2024-1230-223318"
            },
            "fraud_indicators": {
                "gift_card_indicator": "Transaction flagged as likely gift card purchase",
                "round_amount": "Exact round number - $500.00",
                "transaction_frequency": "5 similar transactions in 3 hours",
                "same_merchant_velocity": "Multiple transactions same location",
                "time_of_day": "Late evening - 10:33 PM",
                "card_present": True,
                "unusual_pattern": "Cardholder rarely purchases gift cards",
                "velocity_24h": "5 transactions vs avg 1.8",
                "spending_spike": "2.4x daily average",
                "cross_border_transaction": False
            },
            "historical_transactions": [
                {"date": "2024-12-29", "amount": 78.45, "merchant": "Coffee Shop", "location": "Austin, TX"},
                {"date": "2024-12-28", "amount": 134.67, "merchant": "Grocery Store", "location": "Austin, TX"},
                {"date": "2024-12-27", "amount": 56.90, "merchant": "Gas Station", "location": "Austin, TX"},
                {"date": "2024-12-26", "amount": 212.30, "merchant": "Restaurant", "location": "Austin, TX"}
            ]
        },
        {
            "id": 5,
            "case_name": "Cryptocurrency Exchange Transaction",
            "account": {
                "account_number": "****-****-****-7621",
                "cardholder_name": "Robert Martinez",
                "account_age_days": 445,
                "address": "987 Cedar Ave, Portland, OR 97201",
                "typical_monthly_spend": 1650.00,
                "past_chargebacks": 1
            },
            "flagged_transaction": {
                "amount": 3200.00,
                "merchant": "CryptoExchange Global",
                "mcc": "6051",
                "mcc_description": "Cryptocurrency",
                "location": "Online - Estonia",
                "timestamp": "2024-12-31T04:12:09Z",
                "device_id": "DEVICE_WEB_2P7K",
                "card_present": False,
                "ip_address": "178.62.201.45",
                "transaction_id": "TXN-2024-1231-041209"
            },
            "fraud_indicators": {
                "high_risk_mcc": "Cryptocurrency - elevated fraud risk",
                "high_value_transaction": "1.9x monthly average",
                "new_merchant_category": "First crypto transaction on account",
                "time_of_day": "4 AM - unusual activity time",
                "card_not_present": True,
                "ip_geolocation_mismatch": "IP in Estonia, billing in USA",
                "past_chargeback_history": "1 previous chargeback",
                "velocity_24h": "First crypto transaction",
                "spending_spike": "Significantly above normal",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-30", "amount": 92.15, "merchant": "Grocery Store", "location": "Portland, OR"},
                {"date": "2024-12-29", "amount": 156.78, "merchant": "Electronics Store", "location": "Portland, OR"},
                {"date": "2024-12-28", "amount": 67.50, "merchant": "Gas Station", "location": "Portland, OR"},
                {"date": "2024-12-27", "amount": 189.00, "merchant": "Restaurant", "location": "Portland, OR"}
            ]
        },
        {
            "id": 6,
            "case_name": "Account Takeover Pattern",
            "account": {
                "account_number": "****-****-****-9043",
                "cardholder_name": "Amanda Wilson",
                "account_age_days": 2890,
                "address": "147 Willow St, Denver, CO 80201",
                "typical_monthly_spend": 2450.00,
                "past_chargebacks": 0
            },
            "flagged_transaction": {
                "amount": 1250.00,
                "merchant": "Premium Electronics",
                "mcc": "5732",
                "mcc_description": "Electronics Stores",
                "location": "Los Angeles, CA",
                "timestamp": "2024-12-30T19:28:44Z",
                "device_id": "DEVICE_NEW_5R8T",
                "card_present": False,
                "ip_address": "72.45.198.234",
                "transaction_id": "TXN-2024-1230-192844"
            },
            "fraud_indicators": {
                "device_change": "New device never seen before",
                "shipping_address_change": "Delivery address changed 1 hour before purchase",
                "password_reset": "Account password reset 2 hours ago",
                "email_change_attempt": "Email change requested (blocked)",
                "geographic_anomaly": "Transaction in CA, cardholder in CO",
                "card_not_present": True,
                "behavioral_anomaly": "Purchase pattern completely different",
                "velocity_24h": "Unusual activity spike",
                "spending_spike": "Above normal range",
                "cross_border_transaction": False
            },
            "historical_transactions": [
                {"date": "2024-12-28", "amount": 145.67, "merchant": "Grocery Store", "location": "Denver, CO"},
                {"date": "2024-12-26", "amount": 89.23, "merchant": "Coffee Shop", "location": "Denver, CO"},
                {"date": "2024-12-24", "amount": 234.50, "merchant": "Department Store", "location": "Denver, CO"},
                {"date": "2024-12-22", "amount": 67.80, "merchant": "Gas Station", "location": "Denver, CO"}
            ]
        },
        {
            "id": 7,
            "case_name": "Travel Booking Fraud",
            "account": {
                "account_number": "****-****-****-5127",
                "cardholder_name": "Christopher Brown",
                "account_age_days": 156,
                "address": "258 Oak Ridge, Nashville, TN 37201",
                "typical_monthly_spend": 1780.00,
                "past_chargebacks": 0
            },
            "flagged_transaction": {
                "amount": 6890.00,
                "merchant": "Global Travel Agency",
                "mcc": "4722",
                "mcc_description": "Travel Agencies",
                "location": "Online - Netherlands",
                "timestamp": "2024-12-31T02:47:55Z",
                "device_id": "DEVICE_WEB_3K9L",
                "card_present": False,
                "ip_address": "91.198.174.92",
                "transaction_id": "TXN-2024-1231-024755"
            },
            "fraud_indicators": {
                "high_value_transaction": "3.9x monthly average spend",
                "new_account_risk": "Account less than 6 months old",
                "travel_booking_risk": "High-value travel - common fraud target",
                "time_of_day": "2:47 AM - unusual booking time",
                "card_not_present": True,
                "ip_geolocation_mismatch": "IP in Netherlands, billing in USA",
                "new_merchant": "First transaction with this merchant",
                "velocity_24h": "Largest transaction on account",
                "spending_spike": "Extreme deviation from normal",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-30", "amount": 78.90, "merchant": "Restaurant", "location": "Nashville, TN"},
                {"date": "2024-12-29", "amount": 145.23, "merchant": "Grocery Store", "location": "Nashville, TN"},
                {"date": "2024-12-28", "amount": 56.78, "merchant": "Gas Station", "location": "Nashville, TN"},
                {"date": "2024-12-27", "amount": 234.00, "merchant": "Clothing Store", "location": "Nashville, TN"}
            ]
        },
        {
            "id": 8,
            "case_name": "Subscription Service Fraud",
            "account": {
                "account_number": "****-****-****-8214",
                "cardholder_name": "Lisa Anderson",
                "account_age_days": 1123,
                "address": "369 Sunset Blvd, Phoenix, AZ 85001",
                "typical_monthly_spend": 1950.00,
                "past_chargebacks": 3
            },
            "flagged_transaction": {
                "amount": 299.99,
                "merchant": "Premium Streaming Service",
                "mcc": "5815",
                "mcc_description": "Digital Media Services",
                "location": "Online - Romania",
                "timestamp": "2024-12-30T23:15:28Z",
                "device_id": "DEVICE_MOB_7L2K",
                "card_present": False,
                "ip_address": "185.243.112.67",
                "transaction_id": "TXN-2024-1230-231528"
            },
            "fraud_indicators": {
                "subscription_anomaly": "Annual plan purchased, cardholder uses monthly",
                "past_chargeback_history": "3 previous chargebacks - high risk",
                "ip_geolocation_mismatch": "IP in Romania, billing in USA",
                "device_fingerprint": "Mobile device not recognized",
                "merchant_category_risk": "Digital services - chargeback prone",
                "card_not_present": True,
                "behavioral_anomaly": "Unusual upgrade pattern",
                "velocity_24h": "Multiple subscription attempts",
                "spending_spike": "Normal for category but suspicious context",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-29", "amount": 112.45, "merchant": "Grocery Store", "location": "Phoenix, AZ"},
                {"date": "2024-12-28", "amount": 67.89, "merchant": "Coffee Shop", "location": "Phoenix, AZ"},
                {"date": "2024-12-27", "amount": 189.50, "merchant": "Restaurant", "location": "Phoenix, AZ"},
                {"date": "2024-12-26", "amount": 45.00, "merchant": "Gas Station", "location": "Phoenix, AZ"}
            ]
        },
        {
            "id": 9,
            "case_name": "Wire Transfer Fraud Attempt",
            "account": {
                "account_number": "****-****-****-4567",
                "cardholder_name": "Kevin O'Brien",
                "account_age_days": 2345,
                "address": "741 Mountain View, San Diego, CA 92101",
                "typical_monthly_spend": 3100.00,
                "past_chargebacks": 0
            },
            "flagged_transaction": {
                "amount": 9500.00,
                "merchant": "International Wire Service",
                "mcc": "4829",
                "mcc_description": "Wire Transfer",
                "location": "Online - Nigeria",
                "timestamp": "2024-12-31T05:33:17Z",
                "device_id": "DEVICE_WEB_9X4M",
                "card_present": False,
                "ip_address": "197.210.53.142",
                "transaction_id": "TXN-2024-1231-053317"
            },
            "fraud_indicators": {
                "wire_transfer_risk": "Wire transfers - extremely high fraud risk",
                "high_value_transaction": "3.1x monthly average",
                "high_risk_country": "Transaction originating from high-risk region",
                "time_of_day": "5:33 AM - unusual activity time",
                "card_not_present": True,
                "ip_geolocation_mismatch": "IP in Nigeria, billing in USA",
                "new_merchant_category": "First wire transfer on account",
                "velocity_24h": "Unusual large transaction",
                "spending_spike": "Extreme deviation",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-30", "amount": 189.45, "merchant": "Restaurant", "location": "San Diego, CA"},
                {"date": "2024-12-29", "amount": 234.67, "merchant": "Grocery Store", "location": "San Diego, CA"},
                {"date": "2024-12-28", "amount": 78.90, "merchant": "Gas Station", "location": "San Diego, CA"},
                {"date": "2024-12-27", "amount": 456.00, "merchant": "Department Store", "location": "San Diego, CA"}
            ]
        },
        {
            "id": 10,
            "case_name": "Fuel Purchase Velocity",
            "account": {
                "account_number": "****-****-****-2983",
                "cardholder_name": "Patricia Davis",
                "account_age_days": 678,
                "address": "852 River Road, Atlanta, GA 30301",
                "typical_monthly_spend": 1420.00,
                "past_chargebacks": 1
            },
            "flagged_transaction": {
                "amount": 125.00,
                "merchant": "Gas Station Express",
                "mcc": "5541",
                "mcc_description": "Service Stations",
                "location": "Birmingham, AL",
                "timestamp": "2024-12-30T20:45:33Z",
                "device_id": "DEVICE_POS_4M8N",
                "card_present": True,
                "ip_address": "N/A",
                "transaction_id": "TXN-2024-1230-204533"
            },
            "fraud_indicators": {
                "fuel_velocity": "6 fuel purchases in 8 hours across 3 states",
                "geographic_velocity": "Impossible travel - 300 miles in 2 hours",
                "same_mcc_pattern": "All transactions at gas stations",
                "round_amounts": "All purchases exactly $125.00",
                "card_present": True,
                "skimming_indicator": "Pattern consistent with card skimming",
                "velocity_24h": "6 fuel purchases vs avg 1.2 weekly",
                "spending_spike": "Unusual fuel spending pattern",
                "cross_border_transaction": False,
                "past_chargeback_history": "1 previous chargeback"
            },
            "historical_transactions": [
                {"date": "2024-12-29", "amount": 89.34, "merchant": "Grocery Store", "location": "Atlanta, GA"},
                {"date": "2024-12-28", "amount": 156.78, "merchant": "Restaurant", "location": "Atlanta, GA"},
                {"date": "2024-12-27", "amount": 45.67, "merchant": "Coffee Shop", "location": "Atlanta, GA"},
                {"date": "2024-12-26", "amount": 67.90, "merchant": "Gas Station", "location": "Atlanta, GA"}
            ]
        },
        {
            "id": 11,
            "case_name": "Online Pharmacy Fraud",
            "account": {
                "account_number": "****-****-****-7156",
                "cardholder_name": "James Taylor",
                "account_age_days": 1890,
                "address": "963 Park Place, Philadelphia, PA 19101",
                "typical_monthly_spend": 2200.00,
                "past_chargebacks": 0
            },
            "flagged_transaction": {
                "amount": 875.00,
                "merchant": "Online Pharmacy Direct",
                "mcc": "5912",
                "mcc_description": "Drug Stores and Pharmacies",
                "location": "Online - India",
                "timestamp": "2024-12-31T03:18:42Z",
                "device_id": "DEVICE_WEB_6K3L",
                "card_present": False,
                "ip_address": "103.76.228.91",
                "transaction_id": "TXN-2024-1231-031842"
            },
            "fraud_indicators": {
                "online_pharmacy_risk": "Online pharmacy - high fraud category",
                "high_risk_country": "Merchant in India - elevated risk",
                "new_merchant": "First transaction with this merchant",
                "time_of_day": "3:18 AM - unusual purchase time",
                "card_not_present": True,
                "ip_geolocation_mismatch": "IP in India, billing in USA",
                "high_value_transaction": "Above typical pharmacy spend",
                "velocity_24h": "Unusual pharmacy transaction",
                "spending_spike": "Elevated for category",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-30", "amount": 123.45, "merchant": "Grocery Store", "location": "Philadelphia, PA"},
                {"date": "2024-12-29", "amount": 78.90, "merchant": "Coffee Shop", "location": "Philadelphia, PA"},
                {"date": "2024-12-28", "amount": 234.56, "merchant": "Restaurant", "location": "Philadelphia, PA"},
                {"date": "2024-12-27", "amount": 89.00, "merchant": "Gas Station", "location": "Philadelphia, PA"}
            ]
        },
        {
            "id": 12,
            "case_name": "Peer-to-Peer Payment Scam",
            "account": {
                "account_number": "****-****-****-3421",
                "cardholder_name": "Michelle Garcia",
                "account_age_days": 234,
                "address": "159 Lake Shore Dr, Minneapolis, MN 55401",
                "typical_monthly_spend": 1680.00,
                "past_chargebacks": 2
            },
            "flagged_transaction": {
                "amount": 1500.00,
                "merchant": "P2P Payment App",
                "mcc": "6538",
                "mcc_description": "P2P Payments",
                "location": "Online - USA",
                "timestamp": "2024-12-30T21:52:19Z",
                "device_id": "DEVICE_MOB_8N2K",
                "card_present": False,
                "ip_address": "198.51.100.45",
                "transaction_id": "TXN-2024-1230-215219"
            },
            "fraud_indicators": {
                "p2p_fraud_risk": "P2P payments - common fraud vector",
                "new_account_risk": "Account less than 1 year old",
                "past_chargeback_history": "2 previous chargebacks - elevated risk",
                "high_value_p2p": "Large P2P transfer - unusual",
                "new_recipient": "Payment to unknown recipient",
                "card_not_present": True,
                "behavioral_anomaly": "First large P2P transaction",
                "velocity_24h": "Unusual P2P activity",
                "spending_spike": "Above normal range",
                "cross_border_transaction": False
            },
            "historical_transactions": [
                {"date": "2024-12-29", "amount": 67.89, "merchant": "Coffee Shop", "location": "Minneapolis, MN"},
                {"date": "2024-12-28", "amount": 134.56, "merchant": "Grocery Store", "location": "Minneapolis, MN"},
                {"date": "2024-12-27", "amount": 89.00, "merchant": "Restaurant", "location": "Minneapolis, MN"},
                {"date": "2024-12-26", "amount": 56.78, "merchant": "Gas Station", "location": "Minneapolis, MN"}
            ]
        },
        {
            "id": 13,
            "case_name": "Charity Donation Fraud",
            "account": {
                "account_number": "****-****-****-9087",
                "cardholder_name": "Daniel White",
                "account_age_days": 1456,
                "address": "753 Oakwood Ave, Detroit, MI 48201",
                "typical_monthly_spend": 1920.00,
                "past_chargebacks": 0
            },
            "flagged_transaction": {
                "amount": 2500.00,
                "merchant": "International Relief Fund",
                "mcc": "8398",
                "mcc_description": "Charitable Organizations",
                "location": "Online - Cyprus",
                "timestamp": "2024-12-31T04:27:51Z",
                "device_id": "DEVICE_WEB_5L9M",
                "card_present": False,
                "ip_address": "185.125.190.36",
                "transaction_id": "TXN-2024-1231-042751"
            },
            "fraud_indicators": {
                "charity_fraud_risk": "Unverified charity - potential scam",
                "high_value_donation": "Unusually large donation amount",
                "new_merchant": "First donation to this organization",
                "time_of_day": "4:27 AM - unusual donation time",
                "card_not_present": True,
                "ip_geolocation_mismatch": "IP in Cyprus, billing in USA",
                "merchant_verification": "Charity not in verified database",
                "velocity_24h": "First charity donation on account",
                "spending_spike": "Significantly above normal",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-30", "amount": 98.76, "merchant": "Grocery Store", "location": "Detroit, MI"},
                {"date": "2024-12-29", "amount": 156.34, "merchant": "Restaurant", "location": "Detroit, MI"},
                {"date": "2024-12-28", "amount": 67.89, "merchant": "Gas Station", "location": "Detroit, MI"},
                {"date": "2024-12-27", "amount": 234.00, "merchant": "Department Store", "location": "Detroit, MI"}
            ]
        },
        {
            "id": 14,
            "case_name": "Rental Car Fraud",
            "account": {
                "account_number": "****-****-****-5632",
                "cardholder_name": "Sandra Miller",
                "account_age_days": 567,
                "address": "486 Hillside Rd, Las Vegas, NV 89101",
                "typical_monthly_spend": 2350.00,
                "past_chargebacks": 1
            },
            "flagged_transaction": {
                "amount": 3200.00,
                "merchant": "Luxury Car Rentals",
                "mcc": "7512",
                "mcc_description": "Car Rental",
                "location": "Miami, FL",
                "timestamp": "2024-12-30T22:14:05Z",
                "device_id": "DEVICE_WEB_7M4K",
                "card_present": False,
                "ip_address": "23.94.157.88",
                "transaction_id": "TXN-2024-1230-221405"
            },
            "fraud_indicators": {
                "rental_fraud_risk": "High-value rental - common fraud target",
                "geographic_anomaly": "Rental in FL, cardholder in NV",
                "no_travel_history": "No flight/hotel bookings detected",
                "high_value_transaction": "1.4x monthly average",
                "card_not_present": True,
                "new_merchant": "First transaction with this rental company",
                "past_chargeback_history": "1 previous chargeback",
                "velocity_24h": "Unusual rental activity",
                "spending_spike": "Above normal range",
                "cross_border_transaction": False
            },
            "historical_transactions": [
                {"date": "2024-12-29", "amount": 145.67, "merchant": "Restaurant", "location": "Las Vegas, NV"},
                {"date": "2024-12-28", "amount": 89.34, "merchant": "Grocery Store", "location": "Las Vegas, NV"},
                {"date": "2024-12-27", "amount": 234.00, "merchant": "Entertainment", "location": "Las Vegas, NV"},
                {"date": "2024-12-26", "amount": 67.89, "merchant": "Coffee Shop", "location": "Las Vegas, NV"}
            ]
        },
        {
            "id": 15,
            "case_name": "Software License Fraud",
            "account": {
                "account_number": "****-****-****-8901",
                "cardholder_name": "Brian Johnson",
                "account_age_days": 2100,
                "address": "321 Tech Park, San Jose, CA 95101",
                "typical_monthly_spend": 2780.00,
                "past_chargebacks": 0
            },
            "flagged_transaction": {
                "amount": 1899.00,
                "merchant": "Software Licensing Portal",
                "mcc": "5734",
                "mcc_description": "Computer Software Stores",
                "location": "Online - Russia",
                "timestamp": "2024-12-31T02:38:27Z",
                "device_id": "DEVICE_WEB_3N7K",
                "card_present": False,
                "ip_address": "185.220.101.23",
                "transaction_id": "TXN-2024-1231-023827"
            },
            "fraud_indicators": {
                "software_fraud_risk": "Software licenses - high fraud category",
                "high_risk_country": "Merchant in Russia - elevated risk",
                "time_of_day": "2:38 AM - unusual purchase time",
                "new_merchant": "First transaction with this vendor",
                "card_not_present": True,
                "ip_geolocation_mismatch": "IP in Russia, billing in USA",
                "high_value_transaction": "Above typical software spend",
                "velocity_24h": "Unusual software purchase",
                "spending_spike": "Elevated for category",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-30", "amount": 178.90, "merchant": "Restaurant", "location": "San Jose, CA"},
                {"date": "2024-12-29", "amount": 234.56, "merchant": "Grocery Store", "location": "San Jose, CA"},
                {"date": "2024-12-28", "amount": 89.00, "merchant": "Coffee Shop", "location": "San Jose, CA"},
                {"date": "2024-12-27", "amount": 456.78, "merchant": "Electronics Store", "location": "San Jose, CA"}
            ]
        },
        {
            "id": 16,
            "case_name": "Hotel Booking Scam",
            "account": {
                "account_number": "****-****-****-4523",
                "cardholder_name": "Karen Anderson",
                "account_age_days": 890,
                "address": "654 Beach Blvd, Tampa, FL 33601",
                "typical_monthly_spend": 2050.00,
                "past_chargebacks": 2
            },
            "flagged_transaction": {
                "amount": 4200.00,
                "merchant": "Luxury Resort Booking",
                "mcc": "7011",
                "mcc_description": "Hotels and Motels",
                "location": "Online - Thailand",
                "timestamp": "2024-12-30T23:42:18Z",
                "device_id": "DEVICE_WEB_9K5L",
                "card_present": False,
                "ip_address": "103.28.154.72",
                "transaction_id": "TXN-2024-1230-234218"
            },
            "fraud_indicators": {
                "hotel_fraud_risk": "High-value hotel booking - fraud target",
                "high_value_transaction": "2.0x monthly average",
                "past_chargeback_history": "2 previous chargebacks - high risk",
                "time_of_day": "11:42 PM - unusual booking time",
                "card_not_present": True,
                "ip_geolocation_mismatch": "IP in Thailand, billing in USA",
                "new_merchant": "First booking with this hotel",
                "velocity_24h": "Unusual hotel booking activity",
                "spending_spike": "Significantly above normal",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-29", "amount": 123.45, "merchant": "Grocery Store", "location": "Tampa, FL"},
                {"date": "2024-12-28", "amount": 89.67, "merchant": "Restaurant", "location": "Tampa, FL"},
                {"date": "2024-12-27", "amount": 156.78, "merchant": "Gas Station", "location": "Tampa, FL"},
                {"date": "2024-12-26", "amount": 234.00, "merchant": "Department Store", "location": "Tampa, FL"}
            ]
        },
        {
            "id": 17,
            "case_name": "Auction Site Fraud",
            "account": {
                "account_number": "****-****-****-7834",
                "cardholder_name": "Thomas Moore",
                "account_age_days": 345,
                "address": "987 Valley View, Salt Lake City, UT 84101",
                "typical_monthly_spend": 1590.00,
                "past_chargebacks": 1
            },
            "flagged_transaction": {
                "amount": 2750.00,
                "merchant": "Online Auction House",
                "mcc": "5999",
                "mcc_description": "Miscellaneous Retail",
                "location": "Online - Ukraine",
                "timestamp": "2024-12-31T01:15:33Z",
                "device_id": "DEVICE_WEB_4L8M",
                "card_present": False,
                "ip_address": "91.213.8.96",
                "transaction_id": "TXN-2024-1231-011533"
            },
            "fraud_indicators": {
                "auction_fraud_risk": "Online auction - high fraud category",
                "high_value_transaction": "1.7x monthly average",
                "new_account_risk": "Account less than 1 year old",
                "time_of_day": "1:15 AM - unusual bidding time",
                "card_not_present": True,
                "ip_geolocation_mismatch": "IP in Ukraine, billing in USA",
                "past_chargeback_history": "1 previous chargeback",
                "velocity_24h": "First auction purchase",
                "spending_spike": "Above normal range",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-30", "amount": 89.45, "merchant": "Coffee Shop", "location": "Salt Lake City, UT"},
                {"date": "2024-12-29", "amount": 156.78, "merchant": "Grocery Store", "location": "Salt Lake City, UT"},
                {"date": "2024-12-28", "amount": 67.90, "merchant": "Gas Station", "location": "Salt Lake City, UT"},
                {"date": "2024-12-27", "amount": 234.56, "merchant": "Restaurant", "location": "Salt Lake City, UT"}
            ]
        },
        {
            "id": 18,
            "case_name": "Ticket Resale Scam",
            "account": {
                "account_number": "****-****-****-2156",
                "cardholder_name": "Nancy Harris",
                "account_age_days": 1678,
                "address": "258 Broadway, New York, NY 10001",
                "typical_monthly_spend": 3100.00,
                "past_chargebacks": 0
            },
            "flagged_transaction": {
                "amount": 1850.00,
                "merchant": "Event Tickets Resale",
                "mcc": "7922",
                "mcc_description": "Theatrical Producers",
                "location": "Online - Bulgaria",
                "timestamp": "2024-12-30T20:33:47Z",
                "device_id": "DEVICE_WEB_6M2K",
                "card_present": False,
                "ip_address": "95.87.212.45",
                "transaction_id": "TXN-2024-1230-203347"
            },
            "fraud_indicators": {
                "ticket_resale_risk": "Ticket resale - common fraud vector",
                "new_merchant": "First transaction with this reseller",
                "high_risk_country": "Merchant in Bulgaria - elevated risk",
                "card_not_present": True,
                "ip_geolocation_mismatch": "IP in Bulgaria, billing in USA",
                "merchant_verification": "Reseller not in verified database",
                "high_value_transaction": "Above typical entertainment spend",
                "velocity_24h": "Unusual ticket purchase",
                "spending_spike": "Elevated for category",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-29", "amount": 189.45, "merchant": "Restaurant", "location": "New York, NY"},
                {"date": "2024-12-28", "amount": 234.67, "merchant": "Department Store", "location": "New York, NY"},
                {"date": "2024-12-27", "amount": 78.90, "merchant": "Coffee Shop", "location": "New York, NY"},
                {"date": "2024-12-26", "amount": 456.00, "merchant": "Grocery Store", "location": "New York, NY"}
            ]
        },
        {
            "id": 19,
            "case_name": "Medical Equipment Fraud",
            "account": {
                "account_number": "****-****-****-6789",
                "cardholder_name": "George Wilson",
                "account_age_days": 2234,
                "address": "741 Medical Plaza, Houston, TX 77001",
                "typical_monthly_spend": 2450.00,
                "past_chargebacks": 0
            },
            "flagged_transaction": {
                "amount": 5600.00,
                "merchant": "Medical Supplies Direct",
                "mcc": "5047",
                "mcc_description": "Medical Equipment",
                "location": "Online - Pakistan",
                "timestamp": "2024-12-31T03:52:14Z",
                "device_id": "DEVICE_WEB_8N3L",
                "card_present": False,
                "ip_address": "119.73.96.45",
                "transaction_id": "TXN-2024-1231-035214"
            },
            "fraud_indicators": {
                "medical_equipment_risk": "High-value medical equipment - fraud target",
                "high_value_transaction": "2.3x monthly average",
                "high_risk_country": "Merchant in Pakistan - elevated risk",
                "time_of_day": "3:52 AM - unusual purchase time",
                "card_not_present": True,
                "ip_geolocation_mismatch": "IP in Pakistan, billing in USA",
                "new_merchant": "First transaction with this supplier",
                "velocity_24h": "Unusual medical purchase",
                "spending_spike": "Significantly above normal",
                "cross_border_transaction": True
            },
            "historical_transactions": [
                {"date": "2024-12-30", "amount": 167.89, "merchant": "Grocery Store", "location": "Houston, TX"},
                {"date": "2024-12-29", "amount": 234.56, "merchant": "Restaurant", "location": "Houston, TX"},
                {"date": "2024-12-28", "amount": 89.00, "merchant": "Gas Station", "location": "Houston, TX"},
                {"date": "2024-12-27", "amount": 345.67, "merchant": "Department Store", "location": "Houston, TX"}
            ]
        }
    ]
    
    return scenarios
