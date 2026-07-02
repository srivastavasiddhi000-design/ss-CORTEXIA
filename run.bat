@echo off
title CORTEXIA Launcher

cd /d "%~dp0"

call .venv\Scripts\activate.bat

python -m streamlit run app\main.py

pause