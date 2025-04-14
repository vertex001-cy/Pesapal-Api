# Consume pesapal api with python(Initiate stk push)

## 💡 What is pesapal?
**Pesapal** is a payment processing platform that provides businesses and individuals in Africa with a convenient and secure way to handle online and mobile payments. It enables merchants to accept payments from customers using various methods such as mobile money (like M-Pesa, Airtel Money), debit and credit cards (Visa, Mastercard, American Express), and bank transfers.

## 💡 Key Features:
- **Payment Gateway**: Pesapal offers a payment gateway that integrates with websites, mobile apps, and e-commerce platforms, allowing businesses to accept payments online.
- **Mobile Money Integration**: It supports popular mobile money services in Africa, such as M-Pesa in Kenya, Tanzania, and Uganda, allowing seamless transactions through mobile phones.
- **Point of Sale (POS) Systems**: Pesapal provides hardware and software for businesses to accept payments in physical stores.
- **Recurring Payments**: It supports subscription-based services or recurring payments, which is useful for businesses that provide services like utilities, education, or content streaming.
- **Secure Payment**: Pesapal is PCI-DSS compliant, ensuring that customer card information and transactions are secure.
- **Pesapal API**: Developers can use Pesapal’s API to integrate its payment solutions into custom platforms, mobile apps, and websites.
- **STK Push Payments**: With services like M-Pesa, Pesapal supports STK Push, where a payment prompt is pushed to a customer’s phone for approval.

## 💡 Use Cases:
- **E-commerce stores**: Accept payments for online orders.
- **Service providers**: Bill customers for recurring services like utilities or subscriptions.
- **Event organizers**: Sell tickets online and collect payments.
- **Non-profits**: Collect donations through online platforms.
Pesapal has become popular in several African countries including:
- Kenya
- Malawi
- Rwanda
- Tanzania
- Uganda
- Zambia
- Zimbabwe, and Rwanda.

## 💡 Project Overview
In this repository, I'm going to demonstrate how the pesapal API can be consumed using python code and initiate an stk push to the users. This can be applied to python applications written in django, flask and streamlit to receive payments.

### Supported Countries
This implementation supports payments from:
- Kenya
- Malawi
- Rwanda
- Tanzania
- Uganda
- Zambia
- Zimbabwe
- Project code; https://github.com/SHIVOGOJOHN/Pesapal-Api/blob/main/pesapal.py
- For more info visit; https://developer.pesapal.com/how-to-integrate/e-commerce/api-30-json/api-reference

## 💡 Setup Instructions
1. Create a `.env` file in the project root directory
2. Add your Pesapal credentials to the `.env` file:
   ```
   PESAPAL_CONSUMER_KEY=your_consumer_key_here
   PESAPAL_CONSUMER_SECRET=your_consumer_secret_here
   ```
3. Run the project using the Run button
4. Check the logs to see if authentication was successful

## 💡 Deployment Instructions
To deploy this project:

1. Make sure all your files are committed to your repository
2. Set up environment variables in your deployment platform:
   - PESAPAL_CONSUMER_KEY
   - PESAPAL_CONSUMER_SECRET
   - FLASK_SECRET_KEY (optional, for session security)
3. The project will automatically use the PORT environment variable provided by the hosting platform
4. After deployment, update your PesaPal callback URLs to point to your new deployment domaint code in `main.py`

