
#!/bin/bash
echo "Preparing for Railway deployment..."

# Ensure all files are committed to git
git add .
git commit -m "Prepare for Railway deployment" || echo "No changes to commit"

# Install Railway CLI via npm
echo "Installing Railway CLI via npm..."
npm install -g @railway/cli

# Login to Railway (opens browser)
echo "Please login to Railway..."
railway login

# Create a new project or link to existing one
echo "Initializing Railway project..."
railway init

# Set environment variables
echo "Setting up environment variables..."
railway variables set PESAPAL_CONSUMER_KEY="$PESAPAL_CONSUMER_KEY"
railway variables set PESAPAL_CONSUMER_SECRET="$PESAPAL_CONSUMER_SECRET" 
railway variables set FLASK_SECRET_KEY="$FLASK_SECRET_KEY"

# Deploy
echo "Deploying application to Railway..."
railway up

echo "Deployment complete! Check your Railway dashboard for details."
