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
brew bundle --file=Brewfile

# -----------------------------
# Set repo-level Git identity
# -----------------------------
echo "➡️ Running Git bootstrap..."
CURRENT_NAME=$(git config --get user.name)
CURRENT_EMAIL=$(git config --get user.email)

if [ "$CURRENT_NAME" != "$GIT_NAME" ] || [ "$CURRENT_EMAIL" != "$GIT_EMAIL" ]; then
    source "$CDIR/modules/git-config.sh"
    echo "✅ Git bootstrap complete!"
else
    echo "⚠️ Git identity already set."
fi

# -----------------------------
# Login Azure CLI
# -----------------------------
echo "➡️ Logging into Azure CLI..."
az login
echo "✅ Azure CLI login complete!"

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
