
#!/bin/bash
echo "Deploying to Render via CLI..."

# Check if render-cli is installed
if ! command -v render &> /dev/null; then
    echo "Render CLI not found. Installing..."
    curl -s https://render.com/download-cli.sh | bash
fi

# Login to Render (may open browser)
echo "Logging into Render..."
render login

# Check if we have the required env variables
if [ -z "$PESAPAL_CONSUMER_KEY" ] || [ -z "$PESAPAL_CONSUMER_SECRET" ] || [ -z "$FLASK_SECRET_KEY" ]; then
    echo "Warning: One or more required environment variables are not set."
    echo "You'll need to set them in the Render dashboard after deployment."
fi

# Deploy using the render.yaml file
echo "Deploying using render.yaml configuration..."
render deploy

echo "Deployment initiated! Check the Render dashboard for progress."
echo "Once deployed, make sure to set up the following environment variables if not already set:"
echo "- PESAPAL_CONSUMER_KEY"
echo "- PESAPAL_CONSUMER_SECRET"
echo "- FLASK_SECRET_KEY"
