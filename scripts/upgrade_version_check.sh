#!/bin/sh

# Get the current branch
current_branch=$(git rev-parse --abbrev-ref HEAD)

# Read the commit message
commit_msg=$(cat $1)

# If on main or develop branch and commit message starts with 'feat' or 'fix', exit with failure
if [[ ("$current_branch" == "main" || "$current_branch" == "test/versoning-script") && ($commit_msg == feat* || $commit_msg == fix*) ]]; then
    echo "Committing with 'feat' or 'fix' prefixes is not allowed on the $current_branch branch."
    exit 1
fi
