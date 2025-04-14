
#!/bin/bash
echo "Preparing for Render deployment..."

# Ensure all files are committed to git
git add .
git commit -m "Prepare for Render deployment" || echo "No changes to commit"

echo "Your application is ready to be deployed to Render."
echo "Follow these steps to complete the deployment:"
echo "1. Go to https://dashboard.render.com/register or login"
echo "2. Choose 'New +' and select 'Web Service'"
echo "3. Connect your GitHub repository"
echo "4. Render will automatically detect the render.yaml file"
echo "5. Configure the following environment variables in the Render dashboard:"
echo "   - PESAPAL_CONSUMER_KEY"
echo "   - PESAPAL_CONSUMER_SECRET"
echo "   - FLASK_SECRET_KEY"
echo "6. Click 'Create Web Service'"
echo "7. Your application will be deployed automatically"
