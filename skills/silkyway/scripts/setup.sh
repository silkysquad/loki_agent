#!/bin/bash
# Silkyway Setup Script for OpenClaw

set -e

echo "Installing Silkyway SDK..."
npm install -g https://silkyway.ai/sdk/silkyway-sdk-0.1.0.tgz

echo "Initializing Silkyway wallet..."
if command -v silk &> /dev/null; then
    silk init || echo "Wallet already initialized"
    
    echo "Checking wallet address..."
    silk wallet list
    
    echo ""
    echo "To set cluster to devnet for testing:"
    echo "  silk config set-cluster devnet"
    echo ""
    echo "To fund with test tokens:"
    echo "  silk wallet fund"
    echo "  silk balance"
else
    echo "Error: 'silk' command not found after install"
    exit 1
fi

echo ""
echo "Silkyway setup complete!"
