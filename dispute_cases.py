"""
Dispute Cases for First-Party Fraud Detection (Friendly Fraud)
Realistic chargeback disputes with merchant evidence for forensic analysis
"""

DISPUTE_CASES = [
    {
        "case_id": "DISP-99283",
        "status": "Under Investigation",
        "dispute_details": {
            "customer_claim": "Item Not Received",
            "transaction_amount": "$850.00",
            "transaction_date": "2024-12-15",
            "item": "Limited Edition Air Jordan 1",
            "customer_statement": "The package never arrived. I checked my porch all day. I want a full refund."
        },
        "merchant_evidence": {
            "carrier": "FedEx",
            "tracking_number": "FDX8827364829",
            "tracking_status": "Delivered - Signed for by resident",
            "delivery_timestamp": "2024-12-17 14:32:00",
            "delivery_gps": "43.6532° N, 79.3832° W (Matches Customer Billing Address)",
            "delivery_photo_link": "img_772.jpg (Shows package placed inside open garage)",
            "signature": "J. Martinez (Resident)",
            "customer_history": {
                "total_orders": 12,
                "previous_disputes": 0,
                "account_age_days": 450,
                "average_order_value": "$320"
            }
        }
    },
    {
        "case_id": "DISP-88291",
        "status": "Under Investigation",
        "dispute_details": {
            "customer_claim": "Unauthorized Transaction",
            "transaction_amount": "$1,245.00",
            "transaction_date": "2024-12-20",
            "item": "PlayStation 5 Console Bundle",
            "customer_statement": "I never made this purchase. My card must have been stolen. I demand immediate reversal."
        },
        "merchant_evidence": {
            "carrier": "UPS",
            "tracking_number": "1Z9988776655",
            "tracking_status": "Delivered - Left at front door",
            "delivery_timestamp": "2024-12-22 11:15:00",
            "delivery_gps": "40.7128° N, 74.0060° W (Matches Customer Billing Address)",
            "delivery_photo_link": "ups_delivery_443.jpg (Package at front door)",
            "signature": "No signature required",
            "customer_history": {
                "total_orders": 8,
                "previous_disputes": 2,
                "account_age_days": 180,
                "average_order_value": "$890"
            },
            "additional_evidence": {
                "login_ip": "192.168.1.45 (Customer's home network)",
                "device_fingerprint": "Matches customer's registered iPhone 14",
                "shipping_address": "Same as billing address",
                "social_media": "Customer posted Instagram story unboxing PS5 on 2024-12-22"
            }
        }
    },
    {
        "case_id": "DISP-77234",
        "status": "Under Investigation",
        "dispute_details": {
            "customer_claim": "Item Significantly Not as Described",
            "transaction_amount": "$2,100.00",
            "transaction_date": "2024-12-10",
            "item": "MacBook Pro 16-inch M3",
            "customer_statement": "The laptop is defective and won't turn on. This is not what I ordered. I want a full refund, not a replacement."
        },
        "merchant_evidence": {
            "carrier": "DHL Express",
            "tracking_number": "DHL7766554433",
            "tracking_status": "Delivered - Signed for",
            "delivery_timestamp": "2024-12-12 09:45:00",
            "delivery_gps": "34.0522° N, 118.2437° W (Matches Customer Billing Address)",
            "signature": "Sarah Chen (Cardholder name)",
            "customer_history": {
                "total_orders": 3,
                "previous_disputes": 1,
                "account_age_days": 90,
                "average_order_value": "$1,800"
            },
            "additional_evidence": {
                "serial_number_activated": "Apple activation logs show device activated on 2024-12-12 at 10:30 AM",
                "icloud_account": "Device linked to customer's iCloud account",
                "return_policy": "Customer did not initiate return process within 14-day window",
                "merchant_notes": "Customer used device for 18 days before filing dispute"
            }
        }
    },
    {
        "case_id": "DISP-66789",
        "status": "Under Investigation",
        "dispute_details": {
            "customer_claim": "Duplicate Charge",
            "transaction_amount": "$450.00",
            "transaction_date": "2024-12-18",
            "item": "Dyson V15 Vacuum Cleaner",
            "customer_statement": "I was charged twice for the same order. I only received one vacuum. Please refund the duplicate charge."
        },
        "merchant_evidence": {
            "carrier": "Amazon Logistics",
            "tracking_number": "TBA998877665544",
            "tracking_status": "Delivered",
            "delivery_timestamp": "2024-12-20 16:20:00",
            "delivery_gps": "41.8781° N, 87.6298° W (Matches Customer Billing Address)",
            "delivery_photo_link": "amzl_photo_991.jpg",
            "customer_history": {
                "total_orders": 25,
                "previous_disputes": 3,
                "account_age_days": 720,
                "average_order_value": "$280"
            },
            "additional_evidence": {
                "transaction_analysis": "Two separate orders placed 3 minutes apart with different order IDs",
                "order_1": "ORD-445566 - Dyson V15 - $450 - Delivered 2024-12-20",
                "order_2": "ORD-445599 - Dyson V15 - $450 - Delivered 2024-12-21",
                "second_delivery_proof": "Second package delivered next day, signed for by same person",
                "merchant_notes": "Customer received both items on consecutive days"
            }
        }
    },
    {
        "case_id": "DISP-55123",
        "status": "Under Investigation",
        "dispute_details": {
            "customer_claim": "Service Not Rendered",
            "transaction_amount": "$3,500.00",
            "transaction_date": "2024-12-05",
            "item": "Premium Hotel Stay - 5 Nights",
            "customer_statement": "We never stayed at this hotel. We cancelled our trip due to illness. The hotel is refusing to refund."
        },
        "merchant_evidence": {
            "hotel_name": "Grand Luxury Resort & Spa",
            "reservation_number": "RES-998877",
            "check_in": "2024-12-08 15:00",
            "check_out": "2024-12-13 11:00",
            "customer_history": {
                "total_bookings": 6,
                "previous_disputes": 0,
                "account_age_days": 540,
                "average_booking_value": "$2,200"
            },
            "additional_evidence": {
                "keycard_access_logs": "Room accessed 47 times during stay period",
                "minibar_charges": "$180 in minibar purchases charged to room",
                "spa_services": "$420 spa treatment charged on 2024-12-10",
                "restaurant_charges": "$340 in restaurant charges",
                "checkout_signature": "Digital signature matches cardholder name",
                "cancellation_policy": "Non-refundable rate selected at booking",
                "social_media": "Customer tagged hotel location on Facebook on 2024-12-09"
            }
        }
    },
    {
        "case_id": "DISP-44567",
        "status": "Under Investigation",
        "dispute_details": {
            "customer_claim": "Item Not Received",
            "transaction_amount": "$680.00",
            "transaction_date": "2024-12-22",
            "item": "Samsung Galaxy Watch 6",
            "customer_statement": "Package was stolen from my porch. I never received it. Not my fault."
        },
        "merchant_evidence": {
            "carrier": "USPS",
            "tracking_number": "9400123456789",
            "tracking_status": "Delivered - In/At Mailbox",
            "delivery_timestamp": "2024-12-24 13:45:00",
            "delivery_gps": "33.4484° N, 112.0740° W (Matches Customer Billing Address)",
            "customer_history": {
                "total_orders": 15,
                "previous_disputes": 4,
                "account_age_days": 240,
                "average_order_value": "$520"
            },
            "additional_evidence": {
                "delivery_scan": "Package scanned as delivered to secure mailbox",
                "mailbox_type": "Locked parcel locker (requires key)",
                "customer_action": "Customer did not report theft to police",
                "device_activation": "Watch activated and paired with customer's phone on 2024-12-24 at 14:30",
                "pattern_analysis": "4 previous 'not received' claims in 8 months - all for high-value electronics"
            }
        }
    },
    {
        "case_id": "DISP-33891",
        "status": "Under Investigation",
        "dispute_details": {
            "customer_claim": "Quality Not as Expected",
            "transaction_amount": "$1,800.00",
            "transaction_date": "2024-11-28",
            "item": "Designer Leather Handbag",
            "customer_statement": "The bag is clearly a fake. I paid for authentic designer goods. This is fraud."
        },
        "merchant_evidence": {
            "carrier": "FedEx Priority",
            "tracking_number": "FDX1122334455",
            "tracking_status": "Delivered - Signed for",
            "delivery_timestamp": "2024-11-30 10:15:00",
            "delivery_gps": "37.7749° N, 122.4194° W (Matches Customer Billing Address)",
            "signature": "M. Johnson",
            "customer_history": {
                "total_orders": 7,
                "previous_disputes": 2,
                "account_age_days": 365,
                "average_order_value": "$1,200"
            },
            "additional_evidence": {
                "authenticity_certificate": "Certificate of Authenticity included with serial number",
                "serial_verification": "Serial number verified with brand manufacturer",
                "product_photos": "Customer posted photos of bag on Instagram with positive comments on 2024-12-01",
                "usage_evidence": "Customer used bag for 30 days before filing dispute",
                "return_window": "Return window expired 15 days before dispute filed",
                "merchant_notes": "Customer attempted to return worn item outside policy window"
            }
        }
    },
    {
        "case_id": "DISP-22456",
        "status": "Under Investigation",
        "dispute_details": {
            "customer_claim": "Cancelled Subscription",
            "transaction_amount": "$299.00",
            "transaction_date": "2024-12-01",
            "item": "Annual Gym Membership",
            "customer_statement": "I cancelled this membership in November. They charged me anyway. I want my money back."
        },
        "merchant_evidence": {
            "merchant_name": "Elite Fitness Center",
            "membership_type": "Annual Premium",
            "customer_history": {
                "member_since": "2023-12-01",
                "previous_disputes": 1,
                "account_age_days": 395
            },
            "additional_evidence": {
                "cancellation_policy": "30-day notice required before renewal date",
                "cancellation_request": "No cancellation request received",
                "facility_access": "Member accessed gym 18 times in December 2024",
                "last_visit": "2024-12-28 06:45 AM",
                "auto_renewal_notice": "Email sent 2024-11-15 confirming upcoming renewal",
                "email_opened": "Customer opened renewal notice email on 2024-11-16",
                "contract_terms": "Annual contract with auto-renewal clause signed digitally"
            }
        }
    },
    {
        "case_id": "DISP-11234",
        "status": "Under Investigation",
        "dispute_details": {
            "customer_claim": "Unauthorized Transaction",
            "transaction_amount": "$4,200.00",
            "transaction_date": "2024-12-14",
            "item": "4K OLED TV 77-inch",
            "customer_statement": "Someone hacked my account and ordered this TV. I never authorized this purchase."
        },
        "merchant_evidence": {
            "carrier": "Best Buy Delivery",
            "tracking_status": "Delivered - In-Home Setup Completed",
            "delivery_timestamp": "2024-12-16 14:00:00",
            "delivery_gps": "29.7604° N, 95.3698° W (Matches Customer Billing Address)",
            "signature": "Robert Williams (Cardholder name)",
            "customer_history": {
                "total_orders": 11,
                "previous_disputes": 0,
                "account_age_days": 820,
                "average_order_value": "$950"
            },
            "additional_evidence": {
                "in_home_setup": "Professional installer spent 90 minutes setting up TV in customer's living room",
                "installer_notes": "Customer present during entire installation, asked questions about features",
                "wifi_connection": "TV connected to customer's home WiFi network",
                "smart_tv_account": "TV linked to customer's streaming accounts (Netflix, Disney+)",
                "usage_data": "TV used for 45+ hours before dispute filed",
                "login_verification": "Purchase made from customer's verified device with saved password"
            }
        }
    },
    {
        "case_id": "DISP-00987",
        "status": "Under Investigation",
        "dispute_details": {
            "customer_claim": "Item Defective",
            "transaction_amount": "$950.00",
            "transaction_date": "2024-12-08",
            "item": "Espresso Machine - Commercial Grade",
            "customer_statement": "The machine broke after one use. It's clearly defective. I want a refund, not a repair."
        },
        "merchant_evidence": {
            "carrier": "FedEx Ground",
            "tracking_number": "FDX9988776655",
            "tracking_status": "Delivered",
            "delivery_timestamp": "2024-12-10 15:30:00",
            "delivery_gps": "39.7392° N, 104.9903° W (Matches Customer Billing Address)",
            "customer_history": {
                "total_orders": 4,
                "previous_disputes": 1,
                "account_age_days": 150,
                "average_order_value": "$780"
            },
            "additional_evidence": {
                "warranty_claim": "No warranty claim filed with manufacturer",
                "return_process": "Customer did not contact merchant support before filing dispute",
                "product_inspection": "Returned machine shows signs of improper use (wrong coffee grind, no descaling)",
                "usage_counter": "Internal counter shows 127 uses, not 'one use' as claimed",
                "manufacturer_report": "Damage caused by user error, not defect",
                "merchant_policy": "30-day return policy requires contacting support first"
            }
        }
    }
]

def get_all_disputes():
    """Return list of all dispute cases with summary info"""
    return [
        {
            "case_id": case["case_id"],
            "status": case["status"],
            "customer_claim": case["dispute_details"]["customer_claim"],
            "transaction_amount": case["dispute_details"]["transaction_amount"],
            "item": case["dispute_details"]["item"],
            "transaction_date": case["dispute_details"]["transaction_date"]
        }
        for case in DISPUTE_CASES
    ]

def get_dispute_case(case_id):
    """Get full dispute case by ID"""
    for case in DISPUTE_CASES:
        if case["case_id"] == case_id:
            return case
    return None
