import os

cwd = os.getcwd()
build_json = os.path.join(cwd, 'build.json')

if not os.path.exists(build_json):
    print('No build.json to update with!')
    return

