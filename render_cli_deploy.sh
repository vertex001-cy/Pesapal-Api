
#!/bin/bash
echo "Deploying to Render via CLI..."

# Install Render CLI the proper way
echo "Installing Render CLI..."
npm install -g @render/cli

# Check if installation was successful
if ! command -v render &> /dev/null; then
    echo "Failed to install Render CLI. Falling back to direct deployment method..."
    
    echo "Please visit the Render dashboard to deploy your application:"
    echo "1. Go to https://dashboard.render.com/"
    echo "2. Connect your GitHub repository"
    echo "3. Select 'Deploy from GitHub'"
    echo "4. Follow the prompts to complete the deployment"
    exit 1
fi

# Login to Render
echo "Logging into Render..."
render login

# Deploy using render.yaml
echo "Deploying using render.yaml configuration..."
render deploy

echo "Deployment initiated! Check the Render dashboard for progress."
echo "Make sure the following environment variables are set in your Render dashboard:"
echo "- PESAPAL_CONSUMER_KEY"
echo "- PESAPAL_CONSUMER_SECRET"
echo "- FLASK_SECRET_KEY"
