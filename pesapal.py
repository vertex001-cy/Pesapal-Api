import os
import requests
import json
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class PesapalAPI:
    def __init__(self):
        self.auth_url = "https://pay.pesapal.com/v3/api/Auth/RequestToken"
        self.ipn_base_url = "https://pay.pesapal.com/v3/api/"
        self.consumer_key = os.getenv("PESAPAL_CONSUMER_KEY", "default_key")
        self.consumer_secret = os.getenv("PESAPAL_CONSUMER_SECRET", "default_secret")
        self.cached_token = None #Cached the authentication token to avoid fetching it repeatedly for subsequent API requests
        self.cached_ipn_id = None 
    def authentication(self):
        """Authenticate with Pesapal and return an access token."""
        if self.cached_token:
            return self.cached_token

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        payload = json.dumps({
            "consumer_key": self.consumer_key,
            "consumer_secret": self.consumer_secret
        })

        try:
            response = requests.post(self.auth_url, headers=headers, data=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
            token = response.json().get('token')
            if token:
                self.cached_token = token  # Cache the token for later use
                return token
            else:
                logging.error("Token not found in the response.")
                return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Authentication failed: {e}")
            return None

    def initiate_payment(self, phone, bid_amount, order_id, Fname, Lname):
        """Initiate a payment with Pesapal."""
        token = self.authentication()
        if not token:
            logging.error("Failed to obtain token. Payment initiation aborted.")
            return None

        ipn_id = self.register_ipn()
        if not ipn_id:
            logging.error("Failed to register IPN. Payment initiation aborted.")
            return None

        endpoint = "Transactions/SubmitOrderRequest"
        payload = {
            "id": order_id,  # Use the order_id provided
            "currency": "KES",
            "amount": bid_amount,  # Use the bid_amount provided
            "description": "Payment For Product",
            "callback_url": "https://your-callback-url.com/pesapal/callback",  # Replace with actual callback URL
            "notification_id": ipn_id,
            "billing_address": {
                "phone_number": phone,
                "First_name": Fname,
                "Last_name": Lname,
                "country_code": "KE",
                "line_1": "Your Address",
                "city": "Nairobi",
                "postal_code": "00100"
            }
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {token}"
        }

        try:
            response = requests.post(self.ipn_base_url + endpoint, headers=headers, json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to initiate payment: {e}")
            return None

    def register_ipn(self):
        """Register the IPN (Instant Payment Notification) endpoint with Pesapal."""
        if self.cached_ipn_id:
            return self.cached_ipn_id

        ipn_endpoint = "URLSetup/RegisterIPN"
        payload = {
            "url": "https://your-ipn-url.com/pesapal/ipn",  # Replace with actual IPN URL
            "ipn_notification_type": "GET"
        }

        token = self.authentication()
        if not token:
            logging.error("Failed to obtain token for IPN registration.")
            return None

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {token}"
        }

        try:
            response = requests.post(self.ipn_base_url + ipn_endpoint, headers=headers, json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
            ipn_response = response.json()
            ipn_id = ipn_response.get("ipn_id")
            if ipn_id:
                self.cached_ipn_id = ipn_id  # Cache the IPN ID for later use
                return ipn_id
            else:
                logging.error("IPN ID not found in the response.")
                return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to register IPN: {e}")
            return None

# Initialize logging for debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
