
#!/bin/bash
echo "Preparing for Railway deployment..."

# Ensure all files are committed to git
git add .
git commit -m "Prepare for Railway deployment"

# Deploy to Railway (requires Railway CLI)
# First, install Railway CLI if not installed
if ! command -v railway &> /dev/null; then
    echo "Installing Railway CLI..."
    curl -fsSL https://railway.app/install.sh | sh
fi

# Login to Railway (opens browser)
railway login

# Create a new project or link to existing one
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
