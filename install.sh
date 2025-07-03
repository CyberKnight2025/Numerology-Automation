#!/bin/bash

# install.sh - Setup script for the Numerology Backend Project

echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

echo "Installing Python 3 venv and development tools..."
sudo apt install -y python3 python3-venv python3-pip python3-dev build-essential

echo "Installing PostgreSQL and client libraries..."
sudo apt install -y postgresql postgresql-contrib libpq-dev

echo "Creating virtual environment and installing Python dependencies..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "(Optional) Installing Docker..."
read -p "Do you want to install Docker? [y/N]: " install_docker
if [[ "$install_docker" =~ ^[Yy]$ ]]; then
    sudo apt install -y docker.io docker-compose
    sudo usermod -aG docker $USER
    echo " Docker installed. You may need to restart your system."
fi

echo "(Optional) Installing Microsoft ODBC tools (for MSSQL compatibility)..."
read -p "Do you want to install Microsoft ODBC tools? [y/N]: " install_odbc
if [[ "$install_odbc" =~ ^[Yy]$ ]]; then
    sudo apt install -y unixodbc-dev msodbcsql17
fi

echo "(Optional) Install MongoDB tools..."
read -p "Do you want to install MongoDB tools? [y/N]: " install_mongo
if [[ "$install_mongo" =~ ^[Yy]$ ]]; then
    sudo apt install -y mongodb-clients
fi

echo "(Optional) Install MySQL/MariaDB client tools..."
read -p "Do you want to install MySQL/MariaDB client tools? [y/N]: " install_mysql
if [[ "$install_mysql" =~ ^[Yy]$ ]]; then
    sudo apt install -y mysql-client mariadb-client
fi

echo "Installing GitHub CLI and logging in..."
sudo apt install -y gh
gh auth login

echo "Setup complete!"
