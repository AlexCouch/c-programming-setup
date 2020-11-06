@echo off

if not exist "%1" (
    mkdir %1
)
pushd %1
call init.bat
popd