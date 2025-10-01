#!/usr/bin/env bash
set -euo pipefail

# -----------------------------
# Load configuration
# -----------------------------
CDIR="$(git rev-parse --show-toplevel)/bootstrap"
source "$CDIR/.config.sh"

# -----------------------------
# Sync system environment with Brewfile
# -----------------------------
echo "➡️ Syncing system environment with Brewfile..."
brew bundle --file="$CDIR/Brewfile"

# -----------------------------
# Set repo-level Git identity
# -----------------------------
CURRENT_GH_NAME=$(git config --get user.name)
CURRENT_GH_EMAIL=$(git config --get user.email)
if [ "$CURRENT_GH_NAME" != "$GIT_NAME" ] || [ "$CURRENT_GH_EMAIL" != "$GIT_EMAIL" ]; then
    echo "➡️ Setting repo-level Git identity..."
    source "$CDIR/modules/git-config.sh"
    echo "✅ Git identity set!"
else
    echo "✅ Git identity already set!"
fi

# -----------------------------
# Login Azure CLI
# -----------------------------
CURRENT_AZ_ACCOUNT=$(az account show --query "{user:user.name}" -o tsv)
if [ "$CURRENT_AZ_ACCOUNT" != "$AZ_ACCOUNT" ]; then
    echo "➡️ Logging in to Azure CLI..."
    az login

    CURRENT_AZ_ACCOUNT=$(az account show --query "{user:user.name}" -o tsv)
    if [ "$CURRENT_AZ_ACCOUNT" != "$AZ_ACCOUNT" ]; then
        echo "❌ Login failed or incorrect account. Please try again."
        exit 1
    fi

    echo "✅ Azure CLI login complete!"
else
    echo "✅ Already logged in to the correct Azure account!"
fi

# -----------------------------
# Syncing virtual environment
# -----------------------------
echo "➡️ Syncing virtual environment..."
uv sync
echo "✅ Virtual environment synced!"

# -----------------------------
# Installing pre-commit hooks
# -----------------------------
echo "➡️ Installing pre-commit hooks..."
uv run pre-commit clean
uv run pre-commit install
echo "✅ Pre-commit hooks installed!"

# -----------------------------
# Bootstrap complete
# -----------------------------
echo "✅ Bootstrap complete!"
