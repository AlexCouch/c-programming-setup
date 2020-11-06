@echo off
rem Check if %CMAN_PATH% is define, if not, set it to whatever the path of this script is
rem then call refreshenv
if not defined CMAN_PATH (
    setx CMAN_PATH %~dp0
    call refreshenv.cmd
)
rem Let the user know they're good to go!
echo All good to go!