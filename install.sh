
#!/bin/bash

echo " Setting up Numerology Automation Project..."


# Update & install Python
sudo apt update
sudo apt install -y python3 python3-pip git


# Install dependencies (if any in the future)
if [ -f "requirements.txt" ]; then 
	pip install -r requirements.txt
else
	echo " No requirement.txt found. Skipping dependency installation."
fi 


echo "Setup complete! Run python3 numerology.py to start."
