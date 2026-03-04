@echo off
:: How To Work A Cat — local launcher for Windows
:: Double-click run.bat (or run it from a terminal) to start the app.
:: The app will open in your browser at http://localhost:8501

title How To Work A Cat

echo.
echo  [32m=^> How To Work A Cat[0m
echo  ----------------------------------------

:: ── Check Python ────────────────────────────────────────────────────────────
where python >nul 2>&1
if errorlevel 1 (
    where python3 >nul 2>&1
    if errorlevel 1 (
        echo.
        echo  [31mERROR: Python not found.[0m
        echo.
        echo  Please install Python 3.8 or newer from:
        echo    https://www.python.org/downloads/
        echo.
        echo  During installation tick "Add Python to PATH".
        echo.
        pause
        exit /b 1
    )
    set PYTHON=python3
) else (
    set PYTHON=python
)

for /f "tokens=*" %%i in ('%PYTHON% -c "import sys; print(f\"{sys.version_info.major}.{sys.version_info.minor}\")"') do set PY_VER=%%i
echo   Python %PY_VER% found

:: ── Create / reuse virtual environment ──────────────────────────────────────
if not exist ".venv\" (
    echo   Creating virtual environment...
    %PYTHON% -m venv .venv
)

call .venv\Scripts\activate.bat

:: ── Install / upgrade dependencies ──────────────────────────────────────────
echo   Checking dependencies...
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt
echo   Dependencies ready

:: ── Launch ───────────────────────────────────────────────────────────────────
echo.
echo  [32mStarting app — opening http://localhost:8501 in your browser[0m
echo  Press Ctrl+C to stop.
echo.

:: Open browser after a short delay (runs in background via PowerShell)
start "" /b powershell -WindowStyle Hidden -Command "Start-Sleep 3; Start-Process 'http://localhost:8501'"

streamlit run app.py --server.headless true --server.port 8501

pause
