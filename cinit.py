import os

cwd = os.getcwd()

##Make build dir
print('Creating the build dir')
build = os.path.join(cwd, 'build')
if not os.path.exists(build):
    os.mkdir(build)
    print('Build dir created!')
##Make includes dir
print('Creating the includes dir')
includes = os.path.join(cwd, 'includes')
if not os.path.exists(includes):
    os.mkdir(includes)
    print('Includes dir created!')
##Make src dir
print('Creating the src dir')
src = os.path.join(cwd, 'src')
if not os.path.exists(src):
    os.mkdir(src)
    print('Src dir created!')
##Make libs dir
print('Creating the libs dir')
libs = os.path.join(cwd, 'libs')
if not os.path.exists(libs):
    os.mkdir(libs)
    print('Libs dir created!')
