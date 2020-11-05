import os
import subprocess
import time
import cbuilder

project_name = cbuilder.project_name
cwd = os.getcwd()
build = os.path.join(cwd, 'build')
exe = os.path.join(build, '{}.exe'.format(project_name))

print('')
print('Running {}\n'.format(project_name))

start_time = time.time() * 1000
try:
    out = subprocess.call(exe)
except subprocess.CalledProcessError as e:
    print(e.stdout.decode())
    exit(1)

end_time = time.time() * 1000
diff = int(end_time - start_time)
print('')
print('Finished in {} ms'.format(diff))