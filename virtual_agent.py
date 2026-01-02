"""
Virtual Agent endpoints for Mastercard Contact Center
Handles authentication, chat, and customer support capabilities
"""

from fastapi import HTTPException
import openai
from models import (
    AuthenticationRequest, AuthenticationResponse,
    VirtualAgentChatRequest, VirtualAgentChatResponse,
    CapabilitiesResponse
)

def get_api_key():
    """Import API key from main module"""
    from main import require_openai_api_key
    return require_openai_api_key()

# Card state tracking (in-memory for demo purposes)
card_state = {
    "card_1115": {
        "status": "active",  # active, frozen, lost_stolen, deactivated
        "last_updated": None
    }
}


def get_capabilities():
    """
    Get the list of capabilities the virtual agent can help with
    """
    capabilities = [
        {"id": "1", "icon": "💰", "text": "Check account balance"},
        {"id": "2", "icon": "🚨", "text": "Report a lost or stolen card"},
        {"id": "3", "icon": "❄️", "text": "Freeze / unfreeze your Mastercard"},
        {"id": "9", "icon": "✅", "text": "Activate a new Mastercard"},
        {"id": "8", "icon": "✈️", "text": "Update travel notification for card use abroad"}
        # Commented out for demo - can be re-enabled later:
        # {"id": "4", "icon": "💳", "text": "Request a new card or replacement card"},
        # {"id": "5", "icon": "⚠️", "text": "Dispute a transaction"},
        # {"id": "6", "icon": "📍", "text": "View or update billing address / personal details"},
        # {"id": "7", "icon": "🎁", "text": "Review loyalty rewards or cashback summary"},
        # {"id": "10", "icon": "👤", "text": "Transfer to a live agent"}
    ]
    
    greeting = "Hello! I'm Tracy, your Mastercard Virtual Assistant. For security purposes, I need to verify your identity before we proceed. Please enter your phone number associated with your Mastercard."
    
    return CapabilitiesResponse(capabilities=capabilities, greeting=greeting)


def authenticate_user(request: AuthenticationRequest):
    """
    Authenticate user with SMS code (demo uses 999 as valid code)
    """
    if request.code == "999":
        return AuthenticationResponse(
            success=True,
            verified=True,
            customer_name="Michael Miebach",
            account_number="8765309",
            message="Thank you, Michael. You are now verified."
        )
    else:
        return AuthenticationResponse(
            success=False,
            verified=False,
            attempts_remaining=2,
            message="The code you entered is incorrect. Please try again."
        )


def process_chat(request: VirtualAgentChatRequest):
    """
    Process chat message with sentiment detection and intent recognition
    """
    try:
        sentiment = detect_sentiment(request.message)
        intent = detect_intent(request.message)
        
        off_topic_count = sum(1 for msg in request.conversation_history 
                             if hasattr(msg, 'sentiment') and msg.sentiment == "off_topic")
        
        if is_off_topic(request.message):
            off_topic_count += 1
            
            if off_topic_count >= 3:
                return VirtualAgentChatResponse(
                    response="I understand you may have other questions, but I'm specifically here to help with Mastercard-related inquiries. Let me transfer you to a live agent who can better assist you.",
                    sentiment="neutral",
                    intent="transfer",
                    suggested_actions=[],
                    transfer_to_agent=True,
                    off_topic_count=off_topic_count
                )
            else:
                return VirtualAgentChatResponse(
                    response=f"I appreciate your message, but I'm here specifically to help with Mastercard support. Is there anything related to your Mastercard account I can help you with today?",
                    sentiment="neutral",
                    intent="off_topic",
                    suggested_actions=["Check account balance", "Report lost card", "Dispute transaction"],
                    transfer_to_agent=False,
                    off_topic_count=off_topic_count
                )
        
        # Update card state based on detected intent and conversation
        message_lower = request.message.lower()
        if intent == "lost_card" and "confirm" in message_lower:
            card_state["card_1115"]["status"] = "lost_stolen"
        elif intent == "freeze_card":
            if "unfreeze" in message_lower or "unlock" in message_lower:
                card_state["card_1115"]["status"] = "active"
            else:
                card_state["card_1115"]["status"] = "frozen"
        
        # Get current card status
        old_card_status = card_state["card_1115"]["status"]
        
        conversation_context = "\n".join([
            f"{msg.role}: {msg.content}" 
            for msg in request.conversation_history[-5:]
        ])
        
        system_prompt = f"""You are Tracy, a professional and empathetic Mastercard Contact Center Virtual Assistant helping customer Michael Miebach.

CUSTOMER DATA (CONFIDENTIAL):
- Name: Michael Miebach
- Card ending in: 1115 (NEVER show full number 5555 3412 4444 1115)
- Old Card Status: {old_card_status} (active, frozen, lost_stolen, or deactivated)
- Address: 1 King Street West, Toronto, Ontario, M3J 3P8
- Account Status: Good Standing
- Current Balance: $16,475.00
- Minimum Payment: $403.32
- Next Payment Date: January 29th, 2026
- Last Purchase: $2.35 at Starbucks - Store #2456
- Number of Cards: 1

DETECTED INTENT: {intent}
USER SENTIMENT: {sentiment}

CAPABILITY-SPECIFIC INSTRUCTIONS:

1. CHECK BALANCE (intent: check_balance):
   - Simply provide the current balance: $16,475.00
   - Mention next payment date and minimum payment if relevant

2. REPORT LOST/STOLEN CARD (intent: lost_card):
   - Ask user to type "confirm" to report card ending in 1115 as lost/stolen
   - Once confirmed, tell them card is reported and new card will arrive in 48 hours
   - Be empathetic about the situation

3. FREEZE/UNFREEZE CARD (intent: freeze_card):
   - If freezing: Confirm card ending in 1115 is now frozen
   - If unfreezing: Confirm card ending in 1115 is now unfrozen and ready to use
   - Keep response brief and clear

4. ACTIVATE NEW CARD (intent: activate):
   - Ask for activation code from the new card packaging
   - Accept any code they provide
   - Confirm new card ending in 1234 is now activated
   - IMPORTANT: Check old card status:
     * If old_card_status is "lost_stolen", "deactivated", or "frozen": DO NOT mention the old card or ask about deactivating it. Just confirm the new card is activated.
     * If old_card_status is "active": Ask if they want to deactivate old card ending in 1115

5. TRAVEL NOTIFICATION (intent: travel):
   - Ask for: City, State/Province, Country they're traveling to
   - Once provided, confirm travel note added to their file
   - Wish them a happy and safe trip

TONE: Professional, warm, concise. Use short clear sentences. Enhanced empathy if sentiment is frustrated or negative.

Provide a helpful, concise response based on the detected intent."""
        
        api_key = get_api_key()
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Previous conversation:\n{conversation_context}\n\nUser: {request.message}"}
            ],
            temperature=0.7,
            max_tokens=300
        )
        
        agent_response = response.choices[0].message.content
        suggested_actions = get_suggested_actions(intent)
        
        return VirtualAgentChatResponse(
            response=agent_response,
            sentiment=sentiment,
            intent=intent,
            suggested_actions=suggested_actions,
            transfer_to_agent=False,
            off_topic_count=off_topic_count
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")


def detect_sentiment(message: str) -> str:
    """Detect sentiment from user message"""
    message_lower = message.lower()
    
    frustrated_keywords = ["angry", "upset", "frustrated", "terrible", "awful", 
                          "horrible", "worst", "ridiculous", "unacceptable"]
    if any(keyword in message_lower for keyword in frustrated_keywords):
        return "frustrated"
    
    negative_keywords = ["problem", "issue", "error", "wrong", "not working", 
                        "help", "lost", "stolen"]
    if any(keyword in message_lower for keyword in negative_keywords):
        return "negative"
    
    positive_keywords = ["thank", "thanks", "great", "good", "perfect", 
                        "excellent", "appreciate"]
    if any(keyword in message_lower for keyword in positive_keywords):
        return "positive"
    
    return "neutral"


def detect_intent(message: str) -> str:
    """Detect user intent from message"""
    message_lower = message.lower()
    
    intent_patterns = {
        "check_balance": ["balance", "how much", "account balance"],
        "lost_card": ["lost", "stolen", "missing card", "lost my card", "lost wallet"],
        "freeze_card": ["freeze", "lock", "disable", "turn off"],
        "dispute": ["dispute", "charge", "transaction", "didn't make", "unauthorized"],
        "new_card": ["new card", "replacement", "replace card"],
        "rewards": ["rewards", "points", "cashback", "cash back"],
        "travel": ["travel", "abroad", "overseas", "international"],
        "activate": ["activate", "activation"],
        "live_agent": ["agent", "human", "person", "representative", "speak to someone"],
        "address": ["address", "billing address", "update address"]
    }
    
    for intent, keywords in intent_patterns.items():
        if any(keyword in message_lower for keyword in keywords):
            return intent
    
    return "general_inquiry"


def is_off_topic(message: str) -> bool:
    """Check if message is off-topic"""
    message_lower = message.lower()
    
    off_topic_patterns = [
        "weather", "joke", "tell me a joke", "how are you", "what's your name",
        "where do you live", "personal life", "hobby", "favorite", "movie",
        "sports", "politics", "news"
    ]
    
    return any(pattern in message_lower for pattern in off_topic_patterns)


def get_suggested_actions(intent: str) -> list:
    """Get suggested actions based on detected intent"""
    suggestions = {
        "lost_card": ["Freeze card immediately", "Order replacement card", "Review recent transactions"],
        "dispute": ["View transaction details", "File dispute claim", "Contact merchant"],
        "check_balance": ["View recent transactions", "Download statement", "Set up alerts"],
        "freeze_card": ["Freeze card now", "Unfreeze card", "Order replacement"],
        "rewards": ["View rewards balance", "Redeem points", "View earning history"],
        "travel": ["Set travel dates", "View travel benefits", "Check foreign transaction fees"],
        "live_agent": ["Transfer to agent", "Schedule callback", "Send secure message"],
        "general_inquiry": ["Check balance", "View transactions", "Contact support"]
    }
    
    return suggestions.get(intent, ["Check account balance", "View recent activity", "Contact support"])
