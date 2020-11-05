import os
import json

cwd = os.getcwd()
headers = []
sources = []
global project_name

def build():
    global project_name
    libs = []
    ##Get the directories in the current working directory
    dirs = os.listdir(cwd)

    ##Check if 'includes' is not a directory and throw a fit
    if 'includes' not in dirs:
        print('Expected to find includes dir in current working directory but didnt!')
        return 1

    sources = os.listdir('src')
    for idx, src in enumerate(sources.copy()):
        sources[idx] = '../src/' + src

    if 'libs' in dirs:
        libs = os.listdir(dirs[dirs.index('libs')])

    # print(headers)
    # print(sources)
    # print(libs)

    if 'build' not in dirs:
        os.mkdir('build')
    os.chdir(cwd + '/build')
    cmd_str = 'cl -Zi /I ../includes '

    for header in headers:
        cmd_str += '/I ' + header + ' '

    for src in sources:
        cmd_str += src + ' '

    cmd_str += '/Fe' + cwd + '/build/' + project_name

    # print(cmd_str)
    import subprocess
    try:
        out = subprocess.call(cmd_str)
    except subprocess.CalledProcessError as e:
        print(e.stdout.decode())

    os.chdir(cwd)
        

def get_other_includes():
    global project_name
    build_json = os.path.join(cwd, 'build.json')

    if not os.path.exists(build_json):
        print('No build.json to update with!')
        return 1

    build_json_file = open(build_json, 'r')
    try:
        json_data = json.load(build_json_file)
    except json.JSONDecodeError as e:
        print(e)
        return 1

    if "name" not in json_data:
        print('"name" is a required field.')
        return 1
    
    project_name = json_data["name"]
    # print('found "name" field in build.json: {}'.format(project_name))

    if 'other_includes' not in json_data:
        return
    
    other_includes = json_data["other_includes"]
    if type(other_includes) is not list:
        print('"other_includes" key in build.json must be a list, not a {}'.format(type(other_includes)))
        return 1
    
    headers.extend(other_includes)
    for include in other_includes:
        if not os.path.isdir(include):
            print('{} is not a directory! Please specify a directory to add to additional includes')
            return 1

result = get_other_includes()
if result:
    exit(result)
result = build()
if result:
    exit(result)