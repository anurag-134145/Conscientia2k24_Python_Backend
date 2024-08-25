#!/bin/bash

# Update the package list and install prerequisites
apt-get update
apt-get install -y software-properties-common

# Add the wkhtmltopdf repository and install it
apt-add-repository -y ppa:ubuntu-security-proposed/ppa
apt-get update
apt-get install -y wkhtmltopdf
