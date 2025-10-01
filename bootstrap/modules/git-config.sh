#!/usr/bin/env bash
set -euo pipefail

# -----------------------------
# Load configuration
# -----------------------------
REPO_ROOT="$(git rev-parse --show-toplevel)"
source "$REPO_ROOT/bootstrap/.config.sh"

# -----------------------------
# Set Git identity for the current repository
# -----------------------------
echo "  ➡️ Setting Git identity for repo..."
git config user.name "$GIT_NAME"
git config user.email "$GIT_EMAIL"

# -----------------------------
# Display the updated Git identity
# -----------------------------
echo "  ✅ Git identity updated!"
echo "    Name:  $(git config --get user.name)"
echo "    Email: $(git config --get user.email)"
