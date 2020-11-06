import os
import sys
import shutil
import json

if 'CMAN_PATH' not in os.environ:
    print('CMAN_PATH not set, please run "cman init" to generate it or report to author.')
    exit(1)

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

shutil.copy(os.path.join(os.environ["CMAN_PATH"], '.gitignore'), '.gitignore')

build_json = os.path.join(cwd, 'build.json')
if not os.path.exists(build_json):
    with open(build_json, 'x') as f:
        try:
            data = {
                "name": "",
                "other_includes": [],
                "other_libs": []
            }
            json_data = json.dump(data, f, indent=4)
        except json.JSONEncodError as e:
            print('Failed to encode dict to json')
            print(e)
            exit(1)