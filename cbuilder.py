import os
import json
import sys

global cwd
cwd = os.getcwd()
headers = []
sources = []
libs = []
global project_name

global json_data
json_data = {}
global workspaces
workspaces = []

def load_json_data():
    global json_data
    global cwd

    json_path = os.path.join(cwd, 'build.json')
    if not os.path.exists(json_path):
        print('No build.json to update with!')
        return 1
    try:
        with open(json_path, 'r') as build_json:
            json_data = json.load(build_json)
    except json.JSONDecodeError as e:
        print(e)
        return 1

def dispatch_kind():
    global json_data
    global workspaces
    global cwd

    if "kind" not in json_data:
        print('Please specify a "kind" property in build.json! Either "app", "lib", or "container"')
        return 1
    kind = json_data["kind"]
    if kind not in ("app", "lib", "container"):
        print('Please specify a kind of either app, lib, or container, not {}'.format(kind))
        return 1

    if kind == "app":
        ##Load the other includes and libs
        result = get_other_includes()
        if result:
            return result

        ##Build
        result = build()
        if result:
            return result
    elif kind == "lib":
        ##Load the other includes and libs
        result = get_other_includes()
        if result:
            return result

        ##Build
        result = build(True)
        if result:
            return result
    elif kind == "container":
        get_workspaces()
        print(json_data)
        ws_name = sys.argv[2]
        if ws_name not in workspaces:
            print('{} is not a workspace!'.format(ws_name))
            return 1

        ws_path = cwd + '/' + ws_name
        if not os.path.exists(ws_path):
            print('Workspace {} does not exist!'.format(ws_name))
            return 1
        
        os.chdir(ws_path)
        cwd = os.getcwd()
        result = get_other_includes()
        if result:
            return result

        result = build()
        if result:
            return result

def get_workspaces():
    global json_data
    global workspaces

    if "workspaces" not in json_data:
        print('Please specify a "workspaces" property in build.json!')
        return 1

    workspaces = json_data["workspaces"]

    

def build(lib=False):
    global project_name
    global cwd

    print('Building {}...\n'.format(project_name))
    ##Get the directories in the current working directory
    dirs = os.listdir(cwd)

    ##Check if 'includes' is not a directory and throw a fit
    if 'includes' not in dirs:
        print('Expected to find includes dir in current working directory but didnt!')
        return 1

    sources = os.listdir('src')
    if not sources:
        print('src cannot be empty while also being built!')
        return 1

    for idx, src in enumerate(sources.copy()):
        sources[idx] = '../src/' + src

    if 'libs' in dirs:
        libs_dir = os.listdir(dirs[dirs.index('libs')])
        for lib in libs_dir:
            if os.isfile(lib):
                libs.append(lib)


    if 'build' not in dirs:
        os.mkdir('build')
    os.chdir(cwd + '/build')
    cmd_str = ''
    if lib is True:
        cmd_str = 'cl /c -Zi /I ../includes '

        for header in headers:
            cmd_str += '/I ' + header + ' '

        for src in sources:
            cmd_str += src + ' '
    else:
        cmd_str = 'cl -Zi /I ../includes '

        for header in headers:
            cmd_str += '/I ' + header + ' '

        for src in sources:
            cmd_str += src + ' '

        cmd_str += '/Fe' + cwd + '/build/' + project_name

    # print(cmd_str)
    import subprocess
    import time

    ##Build object files before linking them into a lib
    start_time = time.time() * 1000
    try:
        out = subprocess.call(cmd_str)
    except subprocess.CalledProcessError as e:
        print(e.stdout.decode())
    
    end_time = time.time() * 1000
    diff = int(end_time - start_time)
    
    print('')
    print('Obj built in {} ms'.format(diff))

    ##Link object files into lib
    link_str = 'lib /out:' + cwd + '/build/' + project_name + '.lib '
    for file in os.listdir(cwd + '/build'):
        filename, ext = os.path.splitext(file)
        print('filename: {}, ext: {}'.format(filename, ext))
        if ext == ".obj":
            link_str += cwd + '/build/' + file + ' '
    
    # print('link_str', link_str)
    start_time = time.time() * 1000
    try:
        out = subprocess.call(link_str)
    except subprocess.CalledProcessError as e:
        print(e.stdout.decode())
    
    end_time = time.time() * 1000
    diff = int(end_time - start_time)
    
    print('')
    print('Lib built in {} ms'.format(diff))

    

    os.chdir(cwd)
        

def get_other_includes():
    global project_name
    global json_data

    if "name" not in json_data:
        print('"name" is a required field.')
        return 1

    name = json_data["name"]
    print(json_data['name'])
    if name == "":
        print('"name" cannot be empty!')
        return 1

    project_name = name
    # print('found "name" field in build.json: {}'.format(project_name))

    if 'other_includes' not in json_data:
        return
    
    other_includes = json_data["other_includes"]
    if type(other_includes) is not list:
        print('"other_includes" key in build.json must be a list, not a {}'.format(type(other_includes)))
        return 1
    
    for include in other_includes:
        if not os.path.isdir(include):
            print('{} is not a directory! Please specify a directory to add to additional includes')
            return 1
    headers.extend(other_includes)

    if "other_libs" not in json_data:
        return

    other_libs = json_data["other_libs"]
    if type(other_libs) is not list:
        print('"other_libs" key in build.json must be a list, not a {}'.format(type(other_libs)))
        return 1
    libs.extend(other_libs)

##Load the json data
result = load_json_data()
if result:
    exit(result)

##Dispatch based on what 'kind' of project this is
result = dispatch_kind()
if result:
    exit(result)

