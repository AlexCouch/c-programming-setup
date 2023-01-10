# Cman
This is a "build system" I've made for myself for the purpose of efficiently writing C code.
This will give you access to scripts that will allow you to easily create, manage, compile, and run C projects (or C++).

## Installation
Clone this repo anywhere on your machine. Then cd into the cloned directory and run `setup`.
```
git clone https://github.com/alexcouch/cman
cd cman
setup
```
It should then say something about setting an environment variable following by refreshing the command prompt. This is setup.bat creating and setting CMAN_PATH environ variable to be used by init.bat and cinit.py for copying the default template .gitignore and build.json files into your current directory whenever you call init.

If you don't have cl command enabled on windows then there is a start.bat file which you can run, or you can make it be executed every time you start command prompt. I currently use the following 'target' value:
```
%windir%\system32\cmd.exe /k cd C:\ && %CMAN_PATH%\start.bat
```

This is ofc assuming you've already ran setup.bat.

## Commands

### Cman
All the following commands can also be invoked under a superalias called 'cman'. The reason for this is to make it more clear that these commands are grouped together under the same umbrella.

### Build
```python
#Either of these commands will work just fine
build
cman build
```

Running build.bat will handle running the 'cl' command for you. If you don't have a 'build' directory in your project, it will make one for you and put all your build files in there. It will also keep stdout piped to stdout instead of python subprocess, so that way you can still have the typical output of a compiler. This will also attempt to load up a build.json file for additional info (complexity may grow over time). The general structure looks like this:

```
{
    "name": "some_name_of_executable",
    "other_includes": [
        "...",
        "...",
        "..."
    ],
    "other_libs": [
        "...",
        "...",
        "..."
    ]
}
```
This will be used to add additional includes outside of the project. This is good for if you have your own personal libraries you like to use, or if you like to keep a certain set of libraries at a certain location and you just add their paths to this file. "name" is used for naming the final executable.

This will also tell you how long it took to build.

### New
```
cman new some_dir_name
new some_dir_name
```
This command will create a new directory using the first argument new gets. It will then cd into that directory, call the init script, then pop back into the original current working directory.

### Init
```python
#Either of these commands will work just fine
init
cman init
```

Running init.bat will create a new project setup in your current working directory for you that's structured to work with build.bat. It will create a build, includes, src, and libs dirs for you. The reason I made this was in case it grows in complexity which I expect it will.

The `project` directory is a test directory you can use to play around with this tool.

### Clean
```python
#Either of these commands will work just fine
clean
cman clean
```

Clean will clean out the build directory. Not much else to say. Use it if you wish.

### Run
```python
#Either of these commands will work just fine
run
cman run
```

Run will first call build script followed by running the built executable. This will also tell you how long it took to run.

## Project Kind
Inside the build.json file is a key called `kind`
```json
{
    "name": "test",
    "kind": "app",
    "other_includes": [],
    "other_libs": []
}
```

This tells the script how to build your project. There are three different kinds of projects:

- App
    - Apps are built into executables. This can rely on other libraries that you specify in "other_libs" or "other_includes".
- Lib
    - Libs are built into static libs. There is currently no way to build into a dll.
- Container
    - This is a project with other projects inside. The build too will skip over any includes/src dirs/files you may have at the root of the project. If you give the build command the name of a workspace declared in "workspaces" property in build.json, it will build that workspace. Same with run command.