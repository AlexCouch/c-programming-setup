@echo off

if not defined CMAN_PATH setx CMAN_PATH %~dp0
call refreshenv.cmd
python3 %~dp0\cinit.py