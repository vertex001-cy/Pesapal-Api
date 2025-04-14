
#!/bin/bash
echo "Preparing for Render deployment..."

# Ensure all files are committed to git
git add .
git commit -m "Prepare for Render deployment" || echo "No changes to commit"

# Check if render.yaml exists
if [ ! -f "render.yaml" ]; then
  echo "ERROR: render.yaml file is missing. Please create it first."
  exit 1
fi

# Check runtime.txt exists
if [ ! -f "runtime.txt" ]; then
  echo "WARNING: runtime.txt file is missing. Consider adding it to specify Python version."
fi

# Check if gunicorn is in requirements.txt
if ! grep -q "gunicorn" requirements.txt; then
  echo "WARNING: gunicorn is not in requirements.txt. Adding it..."
  echo "gunicorn>=21.2.0" >> requirements.txt
fi

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
echo "7. Wait for the build and deployment to complete"
echo ""
echo "TROUBLESHOOTING:"
echo "If your deployment fails, check the build logs for errors."
echo "Common issues include:"
echo "- Missing dependencies in requirements.txt"
echo "- Incorrect start command format in render.yaml"
echo "- Port configuration issues (Render assigns PORT env variable automatically)"
