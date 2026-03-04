#!/usr/bin/env bash
# How To Work A Cat — local launcher for Mac/Linux
# Double-click (or run: bash run.sh) to start the app.
# The app will open in your browser at http://localhost:8501

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"

# ── Colour helpers ──────────────────────────────────────────────────────────
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo ""
echo -e "${GREEN}🐱  How To Work A Cat${NC}"
echo "──────────────────────────────────────"

# ── Check Python ────────────────────────────────────────────────────────────
if command -v python3 &>/dev/null; then
    PYTHON=python3
elif command -v python &>/dev/null; then
    PYTHON=python
else
    echo -e "${RED}❌  Python not found.${NC}"
    echo ""
    echo "Please install Python 3.8 or newer:"
    echo "  Mac:   https://www.python.org/downloads/  (or: brew install python)"
    echo "  Linux: sudo apt install python3  (Debian/Ubuntu)"
    echo "         sudo dnf install python3  (Fedora/RHEL)"
    exit 1
fi

PYTHON_VERSION=$($PYTHON -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo -e "  Python $PYTHON_VERSION found ✓"

# ── Create / reuse virtual environment ──────────────────────────────────────
if [ ! -d "$VENV_DIR" ]; then
    echo -e "  ${YELLOW}Creating virtual environment…${NC}"
    $PYTHON -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

# ── Install / upgrade dependencies ──────────────────────────────────────────
echo -e "  ${YELLOW}Checking dependencies…${NC}"
pip install --quiet --upgrade pip
pip install --quiet -r "$SCRIPT_DIR/requirements.txt"
echo -e "  Dependencies ready ✓"

# ── Launch ───────────────────────────────────────────────────────────────────
echo ""
echo -e "${GREEN}✅  Starting app — opening http://localhost:8501 in your browser${NC}"
echo -e "    Press Ctrl+C to stop."
echo ""

# Open browser in background after a short delay so Streamlit has time to start
(sleep 3 && {
    if command -v xdg-open &>/dev/null; then
        xdg-open "http://localhost:8501" 2>/dev/null || true
    elif command -v open &>/dev/null; then
        open "http://localhost:8501" 2>/dev/null || true
    fi
}) &

streamlit run "$SCRIPT_DIR/app.py" \
    --server.headless true \
    --server.port 8501
