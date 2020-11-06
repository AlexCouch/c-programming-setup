@echo off

rem Check if %1 exists, if not, create the directory
if not exist "%1" (
    mkdir %1
)
rem Push the current directory and cd into %1
pushd %1
rem call init.bat
call init.bat
rem return to cwd
popd