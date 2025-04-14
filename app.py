
from flask import Flask, render_template, request, redirect, url_for, flash
from pesapal import PesapalAPI
import logging
import uuid
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "vertex-trading-secret")

pesapal = PesapalAPI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        try:
            # Get form data
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            phone = request.form.get('phone')
            amount = float(request.form.get('amount'))
            
            # Generate a unique order ID
            order_id = f"VTX-{uuid.uuid4().hex[:8]}"
            
            # Initialize payment
            response = pesapal.initiate_payment(
                phone=phone,
                bid_amount=amount,
                order_id=order_id,
                Fname=first_name,
                Lname=last_name
            )
            
            if response and 'redirect_url' in response:
                # Log the successful payment initiation
                logging.info(f"Payment initiated: {response}")
                # Redirect to PesaPal payment page
                return redirect(response['redirect_url'])
            else:
                # Handle error
                flash("Payment initiation failed. Please try again.", "error")
                return redirect(url_for('deposit'))
        
        except Exception as e:
            logging.error(f"Error processing deposit: {str(e)}")
            flash("An error occurred. Please try again.", "error")
            return redirect(url_for('deposit'))
    
    return render_template('deposit.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/callback')
def callback():
    # Handle PesaPal callback
    # This should match the callback URL set in the PesaPal API
    order_tracking_id = request.args.get('OrderTrackingId')
    merchant_reference = request.args.get('OrderMerchantReference')
    
    if order_tracking_id and merchant_reference:
        # Log the callback information
        logging.info(f"Payment callback received: OrderTrackingId={order_tracking_id}, MerchantReference={merchant_reference}")
        return redirect(url_for('success'))
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
    # Note: When deployed to Render, the gunicorn command will be used instead
    # The PORT environment variable will be set automatically by Render
