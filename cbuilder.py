import os

cwd = os.getcwd()
headers = []
sources = []
libs = []

##Get the directories in the current working directory
dirs = os.listdir(cwd)

##Check if 'includes' is not a directory and throw a fit
if 'includes' not in dirs:
    print('Expected to find includes dir in current working directory but didnt!')
    exit(1)

sources = os.listdir('src')
for idx, src in enumerate(sources.copy()):
    sources[idx] = '../src/' + src

if 'libs' in dirs:
    libs = os.listidr(dirs[dirs.index('libs')])

print(headers)
print(sources)
print(libs)

if 'build' not in dirs:
    os.mkdir('build')
os.chdir(cwd + '/build')
cmd_str = 'cl -Zi /I ../includes '

for header in headers:
    cmd_str += header + ' '

for src in sources:
    cmd_str += src + ' '

print(cmd_str)
import subprocess
try:
    out = subprocess.check_output(cmd_str, shell=True)
    print(out.decode())
except subprocess.CalledProcessError as e:
    print(e.stdout.decode())