#! /usr/bin/env bash

# Install Python and pip
sudo pacman -S --noconfirm --needed python-pip python-virtualenv

# Install necessary packages
sudo pip install -r pyyaml

# Make necessary directories
sudo mkdir /opt/AnchorCLI
sudo mkdir /etc/opt/AnchorCLI

# Set ownership on new directories
sudo chown -R $USER:$USER /opt/AnchorCLI
sudo chown -R $USER:$USER /etc/opt/AnchorCLI

# Create Anchors.yml
sudo touch /etc/opt/AnchorCLI/Anchors.yml

# Download AnchorCLI
cd /opt/AnchorCLI
git clone https://github.com/3lackC4t/AnchorCLI.git

sudo chmod +x /opt/AnchorCLI/AnchorCLI/AnchorCLI.py
