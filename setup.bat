@echo off
if not defined CMAN_PATH (
    setx CMAN_PATH %~dp0
    call refreshenv.cmd
)
echo All good to go!