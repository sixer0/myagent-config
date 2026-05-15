#!/bin/bash
# Script to push to GitHub - requires proper authentication

cd "$(dirname "$0")/.."

# Check if authenticated
if ! git push origin master 2>&1 | grep -q "Everything up-to-date\|done"; then
    echo "Authentication required. Please run:"
    echo "  gh auth login --hostname github.com"
    echo "Then authenticate with a PAT that has 'repo' scope"
    exit 1
fi

echo "Successfully pushed to GitHub!"