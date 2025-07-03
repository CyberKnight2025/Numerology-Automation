#!/bin/bash

echo "Updating APT and installing dependencies..."
sudo apt update -y
sudo apt install -y curl gpg

echo "Removing duplicate Elastic source list if it exists..."
if [ -f /etc/apt/sources.list.d/elastic-6.x.list ]; then
    sudo rm /etc/apt/sources.list.d/elastic-6.x.list
    echo "Removed elastic-6.x.list"
else
    echo "elastic-6.x.list not found, skipping..."
fi

echo "Adding MongoDB GPG key..."
curl -fsSL https://pgp.mongodb.com/server-7.0.asc | sudo gpg --dearmor -o /usr/share/keyrings/mongodb-server-7.0.gpg

echo "Installing psycopg2-binary in your virtual environment..."
source myenv/bin/activate
pip install psycopg2-binary

echo "All tasks completed successfully."
