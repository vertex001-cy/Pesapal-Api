
#!/bin/bash
echo "Preparing for Heroku deployment..."

# Install Heroku CLI
curl https://cli-assets.heroku.com/install.sh | sh

# Login to Heroku
heroku login

# Create a new Heroku app if it doesn't exist
heroku create vertex-trading || echo "App already exists"

# Set environment variables
heroku config:set PESAPAL_CONSUMER_KEY="$PESAPAL_CONSUMER_KEY"
heroku config:set PESAPAL_CONSUMER_SECRET="$PESAPAL_CONSUMER_SECRET" 
heroku config:set FLASK_SECRET_KEY="$FLASK_SECRET_KEY"

# Deploy to Heroku
git push heroku main

echo "Deployment complete! Check your Heroku dashboard for details."
