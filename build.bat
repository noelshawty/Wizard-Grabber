@ECHO OFF
@MODE 101,50

ECHO REMOVING INTERFERENCES && PY -3.10 -m pip uninstall -r interferences.txt
ECHO INSTALLING REQUIREMENTS && PY -3.10 -m pip install --force-reinstall -r requirements.txt
CLS && PY -3.10 builder.py
PAUSE && COLOR 07 && EXIT