import os

cwd = os.getcwd()

dirs = os.listdir(cwd)
if "build" not in dirs:
    exit(1)

build = os.path.join(cwd, "build")
# build_dir = open('build', 'w')
os.chdir(build)
files = os.listdir(build)
for file in files:
    os.remove(file)
os.chdir(cwd)