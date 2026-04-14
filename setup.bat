@echo off

REM Automatically installs Python dependencies using pip

python -m pip install --upgrade pip
pip install -r requirements.txt
pause