"""
VisionGuide AI - Sprint 9 Payments
Stripe integration (MVP skeleton)
"""

import os
import stripe
from fastapi import APIRouter, HTTPException, Request

router = APIRouter(prefix="/payments", tags=["payments"])

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "sk_test_dummy")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "whsec_dummy")

stripe.api_key = STRIPE_SECRET_KEY

# ----------------------------
# Create Checkout Session
# ----------------------------

@router.post("/create-checkout-session")
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "VisionGuide AI Pro",
                        },
                        "unit_amount": 999,
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )

        return {"checkout_url": session.url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----------------------------
# Stripe Webhook
# ----------------------------

@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid webhook")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        print("Payment successful:", session["id"])

    return {"status": "success"}
