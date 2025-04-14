
from pesapal import PesapalAPI
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    # Initialize the PesapalAPI class
    pesapal = PesapalAPI()
    
    # Test authentication
    token = pesapal.authentication()
    if token:
        logging.info(f"Authentication successful! Token received.")
    else:
        logging.error("Authentication failed.")
        return
    
    # Test payment initiation
    response = pesapal.initiate_payment(
        phone="254700000000",  # Test phone number
        bid_amount=100.00,     # Test amount
        order_id="test-order-123",  # Test order ID
        Fname="Test",          # First name
        Lname="User"           # Last name
    )
    
    if response:
        logging.info(f"Payment initiation successful: {response}")
    else:
        logging.error("Payment initiation failed.")

if __name__ == "__main__":
    main()
