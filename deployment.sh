#!/bin/bash

# Update the package list and install prerequisites
sudo apt-get update
sudo apt-get install -y software-properties-common

# Add the wkhtmltopdf repository and install it
sudo apt-add-repository -y ppa:ubuntu-security-proposed/ppa
sudo apt-get update
sudo apt-get install -y wkhtmltopdf
