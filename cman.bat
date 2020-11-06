@echo off

if "%1" == "build" (
    call "%~dp0\build.bat" %*
    goto :exit
)
if "%1" == "init" (
    call "%~dp0\init.bat"
    goto :exit
)

if "%1" == "clean" (
    call "%~dp0\clean.bat"
    goto :exit
)

if "%1" == "run" (
    call "%~dp0\run.bat" %*
    goto :exit
)

if "%1" == "new" (
    call "%CMAN_PATH%\new.bat" %2
    goto :exit
)

:exit
